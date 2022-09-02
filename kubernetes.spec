# Generated by go2rpm 1.8.0
%bcond_without check

# https://github.com/kubernetes/kubernetes
%global goipath         k8s.io/kubernetes
%global forgeurl        https://github.com/kubernetes/kubernetes
Version:                1.25.1-rc.0

# REMOVE BEFORE SUBMITTING THIS FOR REVIEW
# ---
# New Fedora packages should use %%gometa -f, which makes the package
# ExclusiveArch to %%golang_arches_future and thus excludes the package from
# %%ix86. If the new package is needed as a dependency for another pacage,
# please consider removing that package from %%ix86 in the same way, instead of
# building more go packages for i686. If your package is not a leaf package,
# you'll need to coordinate the removal of the package's dependents first.
# ---
# REMOVE BEFORE SUBMITTING THIS FOR REVIEW
%gometa -f

%global common_description %{expand:
Production-Grade Container Scheduling and Management.}

%global golicenses      LICENSE LICENSES/LICENSE\\\
                        LICENSES/third_party/forked/golang/LICENSE\\\
                        LICENSES/third_party/forked/gonum/graph/LICENSE\\\
                        LICENSES/third_party/forked/gotestsum/LICENSE\\\
                        LICENSES/third_party/forked/gotestsum/NOTICE\\\
                        LICENSES/third_party/forked/shell2junit/LICENSE\\\
                        LICENSES/third_party/multiarch/qemu-user-\\\
                        static/LICENSE logo/LICENSE\\\
                        staging/src/k8s.io/api/LICENSE\\\
                        staging/src/k8s.io/apiextensions-apiserver/LICENSE\\\
                        staging/src/k8s.io/apiextensions-\\\
                        apiserver/third_party/forked/celopenapi/LICENSE\\\
                        staging/src/k8s.io/apimachinery/LICENSE staging/src/k\\\
                        8s.io/apimachinery/third_party/forked/golang/LICENSE \\\
                        staging/src/k8s.io/apimachinery/third_party/forked/go\\\
                        lang/PATENTS staging/src/k8s.io/apiserver/LICENSE\\\
                        staging/src/k8s.io/cli-runtime/LICENSE\\\
                        staging/src/k8s.io/client-go/LICENSE\\\
                        staging/src/k8s.io/client-\\\
                        go/third_party/forked/golang/LICENSE\\\
                        staging/src/k8s.io/client-\\\
                        go/third_party/forked/golang/PATENTS\\\
                        staging/src/k8s.io/cloud-provider/LICENSE\\\
                        staging/src/k8s.io/cluster-bootstrap/LICENSE\\\
                        staging/src/k8s.io/code-generator/LICENSE\\\
                        staging/src/k8s.io/code-\\\
                        generator/third_party/forked/golang/LICENSE\\\
                        staging/src/k8s.io/code-\\\
                        generator/third_party/forked/golang/PATENTS\\\
                        staging/src/k8s.io/component-base/LICENSE\\\
                        staging/src/k8s.io/component-helpers/LICENSE\\\
                        staging/src/k8s.io/controller-manager/LICENSE\\\
                        staging/src/k8s.io/cri-api/LICENSE\\\
                        staging/src/k8s.io/csi-translation-lib/LICENSE\\\
                        staging/src/k8s.io/kube-aggregator/LICENSE\\\
                        staging/src/k8s.io/kube-controller-manager/LICENSE\\\
                        staging/src/k8s.io/kube-proxy/LICENSE\\\
                        staging/src/k8s.io/kube-scheduler/LICENSE\\\
                        staging/src/k8s.io/kubectl/LICENSE\\\
                        staging/src/k8s.io/kubelet/LICENSE\\\
                        staging/src/k8s.io/legacy-cloud-providers/LICENSE\\\
                        staging/src/k8s.io/metrics/LICENSE\\\
                        staging/src/k8s.io/mount-utils/LICENSE\\\
                        staging/src/k8s.io/pod-security-admission/LICENSE\\\
                        staging/src/k8s.io/sample-apiserver/LICENSE\\\
                        staging/src/k8s.io/sample-cli-plugin/LICENSE\\\
                        staging/src/k8s.io/sample-controller/LICENSE\\\
                        third_party/forked/golang/LICENSE\\\
                        third_party/forked/golang/PATENTS\\\
                        third_party/forked/gonum/graph/LICENSE\\\
                        third_party/forked/gotestsum/LICENSE\\\
                        third_party/forked/gotestsum/NOTICE\\\
                        third_party/forked/shell2junit/LICENSE\\\
                        third_party/multiarch/qemu-user-static/LICENSE
%global godocs          docs CHANGELOG.md CONTRIBUTING.md README.md\\\
                        SUPPORT.md code-of-conduct.md\\\
                        CHANGELOG/CHANGELOG-1.10.md\\\
                        CHANGELOG/CHANGELOG-1.11.md\\\
                        CHANGELOG/CHANGELOG-1.12.md\\\
                        CHANGELOG/CHANGELOG-1.13.md\\\
                        CHANGELOG/CHANGELOG-1.14.md\\\
                        CHANGELOG/CHANGELOG-1.15.md\\\
                        CHANGELOG/CHANGELOG-1.16.md\\\
                        CHANGELOG/CHANGELOG-1.17.md\\\
                        CHANGELOG/CHANGELOG-1.18.md\\\
                        CHANGELOG/CHANGELOG-1.19.md\\\
                        CHANGELOG/CHANGELOG-1.2.md\\\
                        CHANGELOG/CHANGELOG-1.20.md\\\
                        CHANGELOG/CHANGELOG-1.21.md\\\
                        CHANGELOG/CHANGELOG-1.22.md\\\
                        CHANGELOG/CHANGELOG-1.23.md\\\
                        CHANGELOG/CHANGELOG-1.24.md\\\
                        CHANGELOG/CHANGELOG-1.3.md CHANGELOG/CHANGELOG-1.4.md\\\
                        CHANGELOG/CHANGELOG-1.5.md CHANGELOG/CHANGELOG-1.6.md\\\
                        CHANGELOG/CHANGELOG-1.7.md CHANGELOG/CHANGELOG-1.8.md\\\
                        CHANGELOG/CHANGELOG-1.9.md CHANGELOG/README.md\\\
                        CHANGELOG/CHANGELOG-1.25.md api/api-rules/README.md\\\
                        api/openapi-spec/README.md build/README.md\\\
                        build/pause/CHANGELOG.md cluster/README.md\\\
                        cluster/addons/README.md cluster/addons/addon-\\\
                        manager/CHANGELOG.md cluster/addons/addon-\\\
                        manager/README.md cluster/addons/calico-policy-\\\
                        controller/README.md cluster/addons/cluster-\\\
                        loadbalancing/glbc/README.md cluster/addons/dns-\\\
                        horizontal-autoscaler/MAINTAINERS.md\\\
                        cluster/addons/dns-horizontal-autoscaler/README.md\\\
                        cluster/addons/dns/kube-dns/README.md\\\
                        cluster/addons/dns/nodelocaldns/README.md\\\
                        cluster/addons/fluentd-gcp/README.md\\\
                        cluster/addons/fluentd-gcp/fluentd-gcp-\\\
                        image/README.md cluster/addons/metadata-\\\
                        agent/README.md cluster/addons/metadata-\\\
                        proxy/README.md cluster/addons/metrics-\\\
                        server/README.md cluster/addons/node-problem-\\\
                        detector/MAINTAINERS.md cluster/addons/node-problem-\\\
                        detector/README.md cluster/gce/addons/README.md\\\
                        cluster/gce/gci/README.md\\\
                        cluster/gce/gci/mounter/Changelog\\\
                        cluster/gce/windows/README-GCE-Windows-kube-up.md\\\
                        cluster/images/etcd-version-monitor/README.md\\\
                        cluster/images/etcd/README.md cluster/log-\\\
                        dump/README.md cmd/cloud-controller-manager/README.md\\\
                        hack/README.md\\\
                        hack/boilerplate/boilerplate.Dockerfile.txt\\\
                        hack/boilerplate/boilerplate.Makefile.txt\\\
                        hack/boilerplate/boilerplate.generatego.txt\\\
                        hack/boilerplate/boilerplate.go.txt\\\
                        hack/boilerplate/boilerplate.py.txt\\\
                        hack/boilerplate/boilerplate.sh.txt\\\
                        hack/jenkins/README.md hack/tools/README.md\\\
                        hack/verify-flags/excluded-flags.txt logo/colors.md\\\
                        logo/usage_guidelines.md pkg/cloudprovider/README.md\\\
                        pkg/kubelet/checkpointmanager/README.md\\\
                        pkg/kubelet/pluginmanager/pluginwatcher/README.md\\\
                        pkg/proxy/ipvs/README.md examples\\\
                        pkg/scheduler/framework/plugins/README.md\\\
                        staging/README.md\\\
                        staging/src/k8s.io/api/CONTRIBUTING.md\\\
                        staging/src/k8s.io/api/README.md\\\
                        staging/src/k8s.io/api/code-of-conduct.md examples\\\
                        staging/src/k8s.io/apiextensions-\\\
                        apiserver/CONTRIBUTING.md\\\
                        staging/src/k8s.io/apiextensions-apiserver/README.md\\\
                        staging/src/k8s.io/apiextensions-apiserver/code-of-\\\
                        conduct.md staging/src/k8s.io/apiextensions-\\\
                        apiserver/hack/boilerplate.go.txt\\\
                        staging/src/k8s.io/apiextensions-apiserver/third_part\\\
                        y/forked/celopenapi/model/README.md\\\
                        staging/src/k8s.io/apimachinery/CONTRIBUTING.md\\\
                        staging/src/k8s.io/apimachinery/README.md\\\
                        staging/src/k8s.io/apimachinery/code-of-conduct.md\\\
                        staging/src/k8s.io/apiserver/CONTRIBUTING.md\\\
                        staging/src/k8s.io/apiserver/README.md\\\
                        staging/src/k8s.io/apiserver/code-of-conduct.md\\\
                        example staging/src/k8s.io/cli-\\\
                        runtime/CONTRIBUTING.md staging/src/k8s.io/cli-\\\
                        runtime/README.md staging/src/k8s.io/cli-\\\
                        runtime/code-of-conduct.md examples\\\
                        staging/src/k8s.io/client-go/CONTRIBUTING.md\\\
                        staging/src/k8s.io/client-go/INSTALL.md\\\
                        staging/src/k8s.io/client-go/code-of-conduct.md\\\
                        staging/src/k8s.io/client-\\\
                        go/plugin/pkg/client/auth/azure/README.md\\\
                        staging/src/k8s.io/cloud-provider/CONTRIBUTING.md\\\
                        staging/src/k8s.io/cloud-provider/README.md\\\
                        staging/src/k8s.io/cloud-provider/code-of-conduct.md\\\
                        staging/src/k8s.io/cloud-provider/sample/README.md\\\
                        staging/src/k8s.io/cluster-bootstrap/CONTRIBUTING.md\\\
                        staging/src/k8s.io/cluster-bootstrap/README.md\\\
                        staging/src/k8s.io/cluster-bootstrap/code-of-\\\
                        conduct.md examples staging/src/k8s.io/code-\\\
                        generator/CONTRIBUTING.md staging/src/k8s.io/code-\\\
                        generator/code-of-conduct.md staging/src/k8s.io/code-\\\
                        generator/README.md staging/src/k8s.io/code-\\\
                        generator/cmd/client-gen/README.md\\\
                        staging/src/k8s.io/code-generator/cmd/import-\\\
                        boss/README.md staging/src/k8s.io/code-\\\
                        generator/hack/boilerplate.go.txt\\\
                        staging/src/k8s.io/component-base/CONTRIBUTING.md\\\
                        staging/src/k8s.io/component-base/README.md\\\
                        staging/src/k8s.io/component-base/code-of-conduct.md\\\
                        example staging/src/k8s.io/component-base/logs/kube-\\\
                        log-runner/README.md staging/src/k8s.io/component-\\\
                        helpers/CONTRIBUTING.md staging/src/k8s.io/component-\\\
                        helpers/README.md staging/src/k8s.io/component-\\\
                        helpers/code-of-conduct.md\\\
                        staging/src/k8s.io/controller-manager/CONTRIBUTING.md\\\
                        staging/src/k8s.io/controller-manager/README.md\\\
                        staging/src/k8s.io/controller-manager/code-of-\\\
                        conduct.md staging/src/k8s.io/cri-api/CONTRIBUTING.md\\\
                        staging/src/k8s.io/cri-api/README.md\\\
                        staging/src/k8s.io/cri-api/code-of-conduct.md\\\
                        staging/src/k8s.io/csi-translation-\\\
                        lib/CONTRIBUTING.md staging/src/k8s.io/csi-\\\
                        translation-lib/README.md staging/src/k8s.io/csi-\\\
                        translation-lib/code-of-conduct.md\\\
                        staging/src/k8s.io/kube-aggregator/CONTRIBUTING.md\\\
                        staging/src/k8s.io/kube-aggregator/README.md\\\
                        staging/src/k8s.io/kube-aggregator/code-of-conduct.md\\\
                        staging/src/k8s.io/kube-\\\
                        aggregator/hack/boilerplate.go.txt\\\
                        staging/src/k8s.io/kube-controller-\\\
                        manager/CONTRIBUTING.md staging/src/k8s.io/kube-\\\
                        controller-manager/README.md staging/src/k8s.io/kube-\\\
                        controller-manager/code-of-conduct.md\\\
                        staging/src/k8s.io/kube-proxy/CONTRIBUTING.md\\\
                        staging/src/k8s.io/kube-proxy/README.md\\\
                        staging/src/k8s.io/kube-proxy/code-of-conduct.md\\\
                        staging/src/k8s.io/kube-scheduler/CONTRIBUTING.md\\\
                        staging/src/k8s.io/kube-scheduler/README.md\\\
                        staging/src/k8s.io/kube-scheduler/code-of-conduct.md\\\
                        docs staging/src/k8s.io/kubectl/CONTRIBUTING.md\\\
                        staging/src/k8s.io/kubectl/README.md\\\
                        staging/src/k8s.io/kubectl/code-of-conduct.md staging\\\
                        /src/k8s.io/kubectl/pkg/util/i18n/translations/README\\\
                        .md staging/src/k8s.io/kubelet/CONTRIBUTING.md\\\
                        staging/src/k8s.io/kubelet/README.md\\\
                        staging/src/k8s.io/kubelet/code-of-conduct.md\\\
                        staging/src/k8s.io/legacy-cloud-providers/README.md\\\
                        staging/src/k8s.io/legacy-cloud-providers/code-of-\\\
                        conduct.md staging/src/k8s.io/legacy-cloud-\\\
                        providers/openstack/MAINTAINERS.md\\\
                        staging/src/k8s.io/metrics/CONTRIBUTING.md\\\
                        staging/src/k8s.io/metrics/README.md\\\
                        staging/src/k8s.io/metrics/code-of-conduct.md\\\
                        staging/src/k8s.io/metrics/hack/boilerplate.go.txt\\\
                        staging/src/k8s.io/mount-utils/README.md\\\
                        staging/src/k8s.io/mount-utils/code-of-conduct.md\\\
                        staging/src/k8s.io/pod-security-\\\
                        admission/CONTRIBUTING.md staging/src/k8s.io/pod-\\\
                        security-admission/README.md staging/src/k8s.io/pod-\\\
                        security-admission/code-of-conduct.md\\\
                        staging/src/k8s.io/pod-security-\\\
                        admission/webhook/README.md docs\\\
                        staging/src/k8s.io/sample-apiserver/CONTRIBUTING.md\\\
                        staging/src/k8s.io/sample-apiserver/README.md\\\
                        staging/src/k8s.io/sample-apiserver/code-of-\\\
                        conduct.md example staging/src/k8s.io/sample-\\\
                        apiserver/hack/boilerplate.go.txt\\\
                        staging/src/k8s.io/sample-apiserver/hack/custom-\\\
                        boilerplate.go.txt staging/src/k8s.io/sample-cli-\\\
                        plugin/CONTRIBUTING.md staging/src/k8s.io/sample-cli-\\\
                        plugin/README.md staging/src/k8s.io/sample-cli-\\\
                        plugin/code-of-conduct.md docs\\\
                        staging/src/k8s.io/sample-controller/CONTRIBUTING.md\\\
                        staging/src/k8s.io/sample-controller/README.md\\\
                        staging/src/k8s.io/sample-controller/code-of-\\\
                        conduct.md examples staging/src/k8s.io/sample-\\\
                        controller/hack/boilerplate.go.txt\\\
                        staging/src/k8s.io/sample-controller/hack/custom-\\\
                        boilerplate.go.txt\\\
                        third_party/forked/gonum/graph/README.md\\\
                        third_party/multiarch/qemu-user-\\\
                        static/README.kubernetes

Name:           %{goname}
Release:        %autorelease
Summary:        Production-Grade Container Scheduling and Management

License:        Apache-2.0 and BSD-3-Clause and MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
for cmd in cluster/images/etcd/cp staging/src/k8s.io/sample-controller staging/src/k8s.io/apiextensions-apiserver cluster/images/etcd/migrate staging/src/k8s.io/sample-apiserver cluster/images/etcd-version-monitor cluster/gce/gci/mounter hack/conformance staging/src/k8s.io/apiserver/pkg/admission/plugin/webhook/testing/main staging/src/k8s.io/kube-aggregator staging/src/k8s.io/cloud-provider/sample hack/make-rules/helpers/go2make staging/src/k8s.io/component-base/logs/kube-log-runner build/pause/windows/wincat; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE LICENSES/LICENSE LICENSES/third_party/forked/golang/LICENSE
%license LICENSES/third_party/forked/gonum/graph/LICENSE
%license LICENSES/third_party/forked/gotestsum/LICENSE
%license LICENSES/third_party/forked/gotestsum/NOTICE
%license LICENSES/third_party/forked/shell2junit/LICENSE
%license LICENSES/third_party/multiarch/qemu-user-static/LICENSE logo/LICENSE
%license staging/src/k8s.io/api/LICENSE
%license staging/src/k8s.io/apiextensions-apiserver/LICENSE
%license staging/src/k8s.io/apiextensions-apiserver/third_party/forked/celopenapi/LICENSE
%license staging/src/k8s.io/apimachinery/LICENSE
%license staging/src/k8s.io/apimachinery/third_party/forked/golang/LICENSE
%license staging/src/k8s.io/apimachinery/third_party/forked/golang/PATENTS
%license staging/src/k8s.io/apiserver/LICENSE
%license staging/src/k8s.io/cli-runtime/LICENSE
%license staging/src/k8s.io/client-go/LICENSE
%license staging/src/k8s.io/client-go/third_party/forked/golang/LICENSE
%license staging/src/k8s.io/client-go/third_party/forked/golang/PATENTS
%license staging/src/k8s.io/cloud-provider/LICENSE
%license staging/src/k8s.io/cluster-bootstrap/LICENSE
%license staging/src/k8s.io/code-generator/LICENSE
%license staging/src/k8s.io/code-generator/third_party/forked/golang/LICENSE
%license staging/src/k8s.io/code-generator/third_party/forked/golang/PATENTS
%license staging/src/k8s.io/component-base/LICENSE
%license staging/src/k8s.io/component-helpers/LICENSE
%license staging/src/k8s.io/controller-manager/LICENSE
%license staging/src/k8s.io/cri-api/LICENSE
%license staging/src/k8s.io/csi-translation-lib/LICENSE
%license staging/src/k8s.io/kube-aggregator/LICENSE
%license staging/src/k8s.io/kube-controller-manager/LICENSE
%license staging/src/k8s.io/kube-proxy/LICENSE
%license staging/src/k8s.io/kube-scheduler/LICENSE
%license staging/src/k8s.io/kubectl/LICENSE staging/src/k8s.io/kubelet/LICENSE
%license staging/src/k8s.io/legacy-cloud-providers/LICENSE
%license staging/src/k8s.io/metrics/LICENSE
%license staging/src/k8s.io/mount-utils/LICENSE
%license staging/src/k8s.io/pod-security-admission/LICENSE
%license staging/src/k8s.io/sample-apiserver/LICENSE
%license staging/src/k8s.io/sample-cli-plugin/LICENSE
%license staging/src/k8s.io/sample-controller/LICENSE
%license third_party/forked/golang/LICENSE third_party/forked/golang/PATENTS
%license third_party/forked/gonum/graph/LICENSE
%license third_party/forked/gotestsum/LICENSE
%license third_party/forked/gotestsum/NOTICE
%license third_party/forked/shell2junit/LICENSE
%license third_party/multiarch/qemu-user-static/LICENSE
%doc docs CHANGELOG.md CONTRIBUTING.md README.md SUPPORT.md code-of-conduct.md
%doc CHANGELOG/CHANGELOG-1.10.md CHANGELOG/CHANGELOG-1.11.md
%doc CHANGELOG/CHANGELOG-1.12.md CHANGELOG/CHANGELOG-1.13.md
%doc CHANGELOG/CHANGELOG-1.14.md CHANGELOG/CHANGELOG-1.15.md
%doc CHANGELOG/CHANGELOG-1.16.md CHANGELOG/CHANGELOG-1.17.md
%doc CHANGELOG/CHANGELOG-1.18.md CHANGELOG/CHANGELOG-1.19.md
%doc CHANGELOG/CHANGELOG-1.2.md CHANGELOG/CHANGELOG-1.20.md
%doc CHANGELOG/CHANGELOG-1.21.md CHANGELOG/CHANGELOG-1.22.md
%doc CHANGELOG/CHANGELOG-1.23.md CHANGELOG/CHANGELOG-1.24.md
%doc CHANGELOG/CHANGELOG-1.3.md CHANGELOG/CHANGELOG-1.4.md
%doc CHANGELOG/CHANGELOG-1.5.md CHANGELOG/CHANGELOG-1.6.md
%doc CHANGELOG/CHANGELOG-1.7.md CHANGELOG/CHANGELOG-1.8.md
%doc CHANGELOG/CHANGELOG-1.9.md CHANGELOG/README.md CHANGELOG/CHANGELOG-1.25.md
%doc api/api-rules/README.md api/openapi-spec/README.md build/README.md
%doc build/pause/CHANGELOG.md cluster/README.md cluster/addons/README.md
%doc cluster/addons/addon-manager/CHANGELOG.md
%doc cluster/addons/addon-manager/README.md
%doc cluster/addons/calico-policy-controller/README.md
%doc cluster/addons/cluster-loadbalancing/glbc/README.md
%doc cluster/addons/dns-horizontal-autoscaler/MAINTAINERS.md
%doc cluster/addons/dns-horizontal-autoscaler/README.md
%doc cluster/addons/dns/kube-dns/README.md
%doc cluster/addons/dns/nodelocaldns/README.md
%doc cluster/addons/fluentd-gcp/README.md
%doc cluster/addons/fluentd-gcp/fluentd-gcp-image/README.md
%doc cluster/addons/metadata-agent/README.md
%doc cluster/addons/metadata-proxy/README.md
%doc cluster/addons/metrics-server/README.md
%doc cluster/addons/node-problem-detector/MAINTAINERS.md
%doc cluster/addons/node-problem-detector/README.md cluster/gce/addons/README.md
%doc cluster/gce/gci/README.md cluster/gce/gci/mounter/Changelog
%doc cluster/gce/windows/README-GCE-Windows-kube-up.md
%doc cluster/images/etcd-version-monitor/README.md cluster/images/etcd/README.md
%doc cluster/log-dump/README.md cmd/cloud-controller-manager/README.md
%doc hack/README.md hack/boilerplate/boilerplate.Dockerfile.txt
%doc hack/boilerplate/boilerplate.Makefile.txt
%doc hack/boilerplate/boilerplate.generatego.txt
%doc hack/boilerplate/boilerplate.go.txt hack/boilerplate/boilerplate.py.txt
%doc hack/boilerplate/boilerplate.sh.txt hack/jenkins/README.md
%doc hack/tools/README.md hack/verify-flags/excluded-flags.txt logo/colors.md
%doc logo/usage_guidelines.md pkg/cloudprovider/README.md
%doc pkg/kubelet/checkpointmanager/README.md
%doc pkg/kubelet/pluginmanager/pluginwatcher/README.md pkg/proxy/ipvs/README.md
%doc examples pkg/scheduler/framework/plugins/README.md staging/README.md
%doc staging/src/k8s.io/api/CONTRIBUTING.md staging/src/k8s.io/api/README.md
%doc staging/src/k8s.io/api/code-of-conduct.md examples
%doc staging/src/k8s.io/apiextensions-apiserver/CONTRIBUTING.md
%doc staging/src/k8s.io/apiextensions-apiserver/README.md
%doc staging/src/k8s.io/apiextensions-apiserver/code-of-conduct.md
%doc staging/src/k8s.io/apiextensions-apiserver/hack/boilerplate.go.txt
%doc staging/src/k8s.io/apiextensions-apiserver/third_party/forked/celopenapi/model/README.md
%doc staging/src/k8s.io/apimachinery/CONTRIBUTING.md
%doc staging/src/k8s.io/apimachinery/README.md
%doc staging/src/k8s.io/apimachinery/code-of-conduct.md
%doc staging/src/k8s.io/apiserver/CONTRIBUTING.md
%doc staging/src/k8s.io/apiserver/README.md
%doc staging/src/k8s.io/apiserver/code-of-conduct.md example
%doc staging/src/k8s.io/cli-runtime/CONTRIBUTING.md
%doc staging/src/k8s.io/cli-runtime/README.md
%doc staging/src/k8s.io/cli-runtime/code-of-conduct.md examples
%doc staging/src/k8s.io/client-go/CONTRIBUTING.md
%doc staging/src/k8s.io/client-go/INSTALL.md
%doc staging/src/k8s.io/client-go/code-of-conduct.md
%doc staging/src/k8s.io/client-go/plugin/pkg/client/auth/azure/README.md
%doc staging/src/k8s.io/cloud-provider/CONTRIBUTING.md
%doc staging/src/k8s.io/cloud-provider/README.md
%doc staging/src/k8s.io/cloud-provider/code-of-conduct.md
%doc staging/src/k8s.io/cloud-provider/sample/README.md
%doc staging/src/k8s.io/cluster-bootstrap/CONTRIBUTING.md
%doc staging/src/k8s.io/cluster-bootstrap/README.md
%doc staging/src/k8s.io/cluster-bootstrap/code-of-conduct.md examples
%doc staging/src/k8s.io/code-generator/CONTRIBUTING.md
%doc staging/src/k8s.io/code-generator/code-of-conduct.md
%doc staging/src/k8s.io/code-generator/README.md
%doc staging/src/k8s.io/code-generator/cmd/client-gen/README.md
%doc staging/src/k8s.io/code-generator/cmd/import-boss/README.md
%doc staging/src/k8s.io/code-generator/hack/boilerplate.go.txt
%doc staging/src/k8s.io/component-base/CONTRIBUTING.md
%doc staging/src/k8s.io/component-base/README.md
%doc staging/src/k8s.io/component-base/code-of-conduct.md example
%doc staging/src/k8s.io/component-base/logs/kube-log-runner/README.md
%doc staging/src/k8s.io/component-helpers/CONTRIBUTING.md
%doc staging/src/k8s.io/component-helpers/README.md
%doc staging/src/k8s.io/component-helpers/code-of-conduct.md
%doc staging/src/k8s.io/controller-manager/CONTRIBUTING.md
%doc staging/src/k8s.io/controller-manager/README.md
%doc staging/src/k8s.io/controller-manager/code-of-conduct.md
%doc staging/src/k8s.io/cri-api/CONTRIBUTING.md
%doc staging/src/k8s.io/cri-api/README.md
%doc staging/src/k8s.io/cri-api/code-of-conduct.md
%doc staging/src/k8s.io/csi-translation-lib/CONTRIBUTING.md
%doc staging/src/k8s.io/csi-translation-lib/README.md
%doc staging/src/k8s.io/csi-translation-lib/code-of-conduct.md
%doc staging/src/k8s.io/kube-aggregator/CONTRIBUTING.md
%doc staging/src/k8s.io/kube-aggregator/README.md
%doc staging/src/k8s.io/kube-aggregator/code-of-conduct.md
%doc staging/src/k8s.io/kube-aggregator/hack/boilerplate.go.txt
%doc staging/src/k8s.io/kube-controller-manager/CONTRIBUTING.md
%doc staging/src/k8s.io/kube-controller-manager/README.md
%doc staging/src/k8s.io/kube-controller-manager/code-of-conduct.md
%doc staging/src/k8s.io/kube-proxy/CONTRIBUTING.md
%doc staging/src/k8s.io/kube-proxy/README.md
%doc staging/src/k8s.io/kube-proxy/code-of-conduct.md
%doc staging/src/k8s.io/kube-scheduler/CONTRIBUTING.md
%doc staging/src/k8s.io/kube-scheduler/README.md
%doc staging/src/k8s.io/kube-scheduler/code-of-conduct.md docs
%doc staging/src/k8s.io/kubectl/CONTRIBUTING.md
%doc staging/src/k8s.io/kubectl/README.md
%doc staging/src/k8s.io/kubectl/code-of-conduct.md
%doc staging/src/k8s.io/kubectl/pkg/util/i18n/translations/README.md
%doc staging/src/k8s.io/kubelet/CONTRIBUTING.md
%doc staging/src/k8s.io/kubelet/README.md
%doc staging/src/k8s.io/kubelet/code-of-conduct.md
%doc staging/src/k8s.io/legacy-cloud-providers/README.md
%doc staging/src/k8s.io/legacy-cloud-providers/code-of-conduct.md
%doc staging/src/k8s.io/legacy-cloud-providers/openstack/MAINTAINERS.md
%doc staging/src/k8s.io/metrics/CONTRIBUTING.md
%doc staging/src/k8s.io/metrics/README.md
%doc staging/src/k8s.io/metrics/code-of-conduct.md
%doc staging/src/k8s.io/metrics/hack/boilerplate.go.txt
%doc staging/src/k8s.io/mount-utils/README.md
%doc staging/src/k8s.io/mount-utils/code-of-conduct.md
%doc staging/src/k8s.io/pod-security-admission/CONTRIBUTING.md
%doc staging/src/k8s.io/pod-security-admission/README.md
%doc staging/src/k8s.io/pod-security-admission/code-of-conduct.md
%doc staging/src/k8s.io/pod-security-admission/webhook/README.md docs
%doc staging/src/k8s.io/sample-apiserver/CONTRIBUTING.md
%doc staging/src/k8s.io/sample-apiserver/README.md
%doc staging/src/k8s.io/sample-apiserver/code-of-conduct.md example
%doc staging/src/k8s.io/sample-apiserver/hack/boilerplate.go.txt
%doc staging/src/k8s.io/sample-apiserver/hack/custom-boilerplate.go.txt
%doc staging/src/k8s.io/sample-cli-plugin/CONTRIBUTING.md
%doc staging/src/k8s.io/sample-cli-plugin/README.md
%doc staging/src/k8s.io/sample-cli-plugin/code-of-conduct.md docs
%doc staging/src/k8s.io/sample-controller/CONTRIBUTING.md
%doc staging/src/k8s.io/sample-controller/README.md
%doc staging/src/k8s.io/sample-controller/code-of-conduct.md examples
%doc staging/src/k8s.io/sample-controller/hack/boilerplate.go.txt
%doc staging/src/k8s.io/sample-controller/hack/custom-boilerplate.go.txt
%doc third_party/forked/gonum/graph/README.md
%doc third_party/multiarch/qemu-user-static/README.kubernetes
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog
