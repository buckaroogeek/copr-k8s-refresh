# Master kubernetes spec file

# global settings
%global provider                github
%global provider_tld            com
%global project                 kubernetes
%global repo                    kubernetes
%global provider_prefix         %{provider}.%{provider_tld}/%{project}/%{repo}

# specific release metadata - relver is release version
%global relver                  1.24.5
%global commit                  e4d4e1ab7cf1bf15273ef97303551b279f0920a9
%global shortcommit             %(c=%{commit}; echo ${c:0:7})

# Needed otherwise "version_ldflags=$(kube::version_ldflags)" doesn't work
%global _buildshell  /bin/bash
%global _checkshell  /bin/bash

# preamble
Name:           kubernetes
Version:        %{relver}
Release:        %autorelease
Summary:        Production-Grade Container Scheduling and Management

License:        Apache-2.0 and BSD-3-Clause and MIT
URL:            https://kubernetes.io
ExclusiveArch:  x86_64 aarch64 ppc64le s390x %{arm}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

Source105:      kubelet.service
Source107:      environ-config
Source109:      environ-kubelet
Source110:      environ-kubelet.kubeconfig
Source113:      kubernetes-accounting.conf
Source114:      kubeadm.conf
Source115:      kubernetes.conf
Source116:      %{name}.sysusers

%description
%{summary}
Includes the three (3) basic components needed to create, run, and manage
a cluster which are kubeadm, kubelet, and kubectl respectively. Kubeadm and
kubelet are installed by the main package. Kubectl is installed by a subpackage.

## 'master' subpackage removed. It contained legacy systemd services
## for control planes such as api-server that are now
## provisioned as static pods on each control plane.

## node and kubeadm subpackages condenses into main package.

##############################################
############################################

# Kubernetes obsoletes cadvisor but needs its source code (literally integrated)
# the version number is arbitrary but old enough to catch any version in supported
# Fedora releases
Obsoletes:      cadvisor >= 0.31

## kubernetes requirements - installs kubeadm and kubelet

# generic build requirements for kubelet, kubeadm
BuildRequires: golang >= 1.18.5
BuildRequires: go-bindata
BuildRequires: make
BuildRequires: go-md2man

# additonal kubelet requirements
Requires: (containerd or cri-o)
Suggests: containerd
Requires: conntrack-tools

BuildRequires: systemd
BuildRequires: rsync

Requires(pre): shadow-utils
Requires:      socat
Requires:      kubernetes-client = %{version}-%{release}

# additional kubeadm requirements
Requires: containernetworking-plugins
Requires: cri-tools

##############################################
## client subpackage
%package client
Summary: Kubernetes command line interface tools

BuildRequires: golang >= 1.18.5
BuildRequires: go-bindata
BuildRequires: make
BuildRequires: go-md2man

%description client
Kubernetes command line interface tools like kubectl

#############################################
#############################################
%prep
%setup -q -n %{repo}-%{commit}

mkdir -p src/k8s.io/kubernetes
mv $(ls | grep -v "^src$") src/k8s.io/kubernetes/.


%build
pushd src/k8s.io/kubernetes/
# 'make all cmd/XYZ' results in sourcing init.sh
# Not sure why setup_env is called as make just works
# but will review in COPR
# source hack/lib/init.sh
# kube::golang::setup_env

export KUBE_GIT_TREE_STATE="clean"
export KUBE_GIT_COMMIT=%{commit}
export KUBE_GIT_VERSION=v{version}
export KUBE_EXTRA_GOPATH=$(pwd)/Godeps/_workspace

# Build each binary separately to generate a unique build-id.
# Otherwise: Duplicate build-ids /builddir/build/BUILDROOT/.../usr/bin/kube-apiserver and /builddir/build/BUILDROOT/.../usr/bin/kubeadm
# CHANGE - added all to make
make all WHAT="cmd/kubelet"
make all WHAT="cmd/kubeadm"
make all WHAT="cmd/kubectl"

# Gen docs
make all WHAT="cmd/gendocs"
make all WHAT="cmd/genkubedocs"
make all WHAT="cmd/genman"
make all WHAT="cmd/genyaml"
kube::util::gen-docs .


%install
pushd src/k8s.io/kubernetes/
# needed to make kube::golang::host_platforms available
source hack/lib/init.sh
kube::golang::setup_env

%ifarch ppc64le
output_path="_output/local/go/bin"
%else
output_path="${KUBE_OUTPUT_BINPATH}/$(kube::golang::host_platform)"
%endif

echo "+++ INSTALLING binaries"
install -m 755 -d %{buildroot}%{_bindir}
install -p -m 755 -t %{buildroot}%{_bindir} ${output_path}/kubelet
install -p -m 755 -t %{buildroot}%{_bindir} ${output_path}/kubeadm
install -p -m 755 -t %{buildroot}%{_bindir} ${output_path}/kubectl

# kubeadm configuration file
echo "+++ INSTALLING kubeadm config"
install -d -m 0755 %{buildroot}/%{_unitdir}/kubelet.service.d
install -p -m 0644 -t %{buildroot}/%{_unitdir}/kubelet.service.d %{SOURCE114}

echo "+++ INSTALLING shell completion"
install -d -m 0755 %{buildroot}%{_datadir}/bash-completion/completions/
%{buildroot}%{_bindir}/kubectl completion bash > %{buildroot}%{_datadir}/bash-completion/completions/kubectl
install -d -m 0755 %{buildroot}%{_datadir}/zsh-completion/completions/
%{buildroot}%{_bindir}/kubectl completion zsh > %{buildroot}%{_datadir}/zsh-completion/completions/kubectl
install -d -m 0755 %{buildroot}%{_datadir}/fish-completion/completions/
%{buildroot}%{_bindir}/kubectl completion fish > %{buildroot}%{_datadir}/fish-completion/completions/kubectl

echo "+++ CREATING manifests directory"
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}
install -d -m 0700 %{buildroot}%{_sysconfdir}/%{name}/manifests

echo "+++ INSTALLING config files"
%define remove_environ_prefix() %(echo -n %1|sed 's/.*environ-//g')
install -m 644 -T %{SOURCE107} %{buildroot}%{_sysconfdir}/%{name}/%{remove_environ_prefix %{SOURCE107}}
install -m 644 -T %{SOURCE109} %{buildroot}%{_sysconfdir}/%{name}/%{remove_environ_prefix %{SOURCE109}}
install -m 644 -T %{SOURCE110} %{buildroot}%{_sysconfdir}/%{name}/%{remove_environ_prefix %{SOURCE110}}

# place systemd/tmpfiles.d/kubernetes.conf to /usr/lib/tmpfiles.d/kubernetes.conf
install -d -m 0755 %{buildroot}%{_tmpfilesdir}
install -p -m 0644 -t %{buildroot}/%{_tmpfilesdir} %{SOURCE115}

echo "+++ INSTALLING sysusers.d"
install -D -m644 -vp %{SOURCE116}       %{buildroot}%{_sysusersdir}/%{name}.conf

# enable CPU and Memory accounting
install -d -m 0755 %{buildroot}/%{_sysconfdir}/systemd/system.conf.d
install -p -m 0644 -t %{buildroot}/%{_sysconfdir}/systemd/system.conf.d %{SOURCE113}

echo "+++ INSTALLING service files"
install -d -m 0755 %{buildroot}%{_unitdir}
install -m 0644 -t %{buildroot}%{_unitdir} %{SOURCE105}

echo "+++ INSTALLING manpages"
install -d %{buildroot}%{_mandir}/man1
# from k8s tarball copied docs/man/man1/*.1
install -p -m 644 docs/man/man1/*.1 %{buildroot}%{_mandir}/man1

# install the place the kubelet defaults to put volumes and default folder structure
install -d %{buildroot}%{_sharedstatedir}/kubelet

mkdir -p %{buildroot}/run
install -d -m 0755 %{buildroot}/run/%{name}/
popd

mv src/k8s.io/kubernetes/CHANGELOG/CHANGELOG-*.md .
mv src/k8s.io/kubernetes/*.md .
mv src/k8s.io/kubernetes/LICENSE .
# CHANGELOG.md is symlink to CHANGELOG/README.md and not actual
# change log. no need to include generated rpms
rm CHANGELOG.md

%check
if [ 1 != 1 ]; then
echo "******Testing the commands*****"
hack/test-cmd.sh
echo "******Benchmarking kube********"
hack/benchmark-go.sh

# In Fedora 20 and RHEL7 the go cover tools isn't available correctly
echo "******Testing the go code******"
hack/test-go.sh
echo "******Testing integration******"
hack/test-integration.sh --use_go_build
fi


#############################################
#############################################

%files
## kubelet files
%license LICENSE
%doc *.md
%{_mandir}/man1/kubelet.1*
%{_mandir}/man1/kube-proxy.1*
%{_bindir}/kubelet
%{_unitdir}/kubelet.service
%{_sysusersdir}/%{name}.conf
%dir %{_sharedstatedir}/kubelet
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/manifests
%config(noreplace) %{_sysconfdir}/%{name}/config
%config(noreplace) %{_sysconfdir}/%{name}/kubelet
%config(noreplace) %{_sysconfdir}/%{name}/proxy
%config(noreplace) %{_sysconfdir}/%{name}/kubelet.kubeconfig
%config(noreplace) %{_sysconfdir}/systemd/system.conf.d/kubernetes-accounting.conf
%{_tmpfilesdir}/kubernetes.conf
%verify(not size mtime md5) %attr(755, kube,kube) %dir /run/%{name}

# kubeadm files
%license LICENSE
%doc *.md
%{_mandir}/man1/kubeadm.1*
%{_mandir}/man1/kubeadm-*
%{_bindir}/kubeadm
%dir %{_sysconfdir}/systemd/system/kubelet.service.d
%config(noreplace) %{_sysconfdir}/systemd/system/kubelet.service.d/kubeadm.conf

## client package files
%files client
%{_mandir}/man1/kubectl.1*
%{_mandir}/man1/kubectl-*
%{_bindir}/kubectl
%{_datadir}/bash-completion/completions/kubectl
%{_datadir}/zsh-completion/completions/kubectl
%{_datadir}/fish-completion/completions/kubectl

############################################

%pre
%sysusers_create_compat %{SOURCE116}

%post
%systemd_post kubelet
# If accounting is not currently enabled systemd reexec
if [[ `systemctl show kubelet | grep -q -e CPUAccounting=no -e MemoryAccounting=no; e
cho $?` -eq 0 ]]; then
  systemctl daemon-reexec
fi

%preun
%systemd_preun kubelet

%postun
%systemd_postun kubelet


############################################
############################################
%changelog
%autochangelog
