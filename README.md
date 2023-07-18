COPR-K8S-REFRESH
================

Revise kuberntes spec file for Fedora

## Motivation

There are two primary drivers that mandate a revision of the kubernetes spec file used in Fedora. First, multiple versions of Kubernetes will be generated for each release of Fedora following the [Multiple packages with the same base name](https://docs.fedoraproject.org/en-US/packaging-guidelines/Naming/#multiple) standard. The spec file will be revised with automation in mind similar to that used for nodejs packages. 

Second, The current kubernetes spec file contains a number of artifacts that may no longer be useful or needed. 

## Goals

We aim to provide first class support for Kubernetes packages in Fedora. Packages that allow Fedora machines, whether physical or virtual, to be used as host OS in Kubernetes clusters. This explicitly includes Fedora CoreOS. 

We also aim to provide packages of all supported versions of Kubernetes available for a current release of Fedora. The go language is the used to develop Kubernetes with each Kubernetes release based on a specific version of go (major:minor version). Each release of Fedora has a specific version of go. Fedora 36, for example, provides go 1.18.x and Fedora 37 provides go 1.19.x. The goal for Kubernetes then would be to provide a default version of Kubernetes that aligns with the go version, and parallel installable versions of other Kubernetes releases that are still supported.

Example Availability Matrix. Each Fedora release annotated with the go version available. D - default; A- available parallel version; O - obsolete; -- - absent.

| Kubernetes Version | K8s Go Version | F39 (1.21) | F38 (1.20) | F37 (1.19) |
| :--- | --- | --- | --- | ---: |
| 1.28 | 1.20 | D | -- | -- |
| 1.27 | 1.20 | A | A | -- |
| 1.26 | 1.20 (1.19) | A | D | -- |
| 1.25 | 1.19 | A | A | D |
| 1.24 | 1.18 | A | A | A |


## Requirements

1. Provide a default version of Kubernetes for each Fedora release (see also tranistion notes below). The default version of Kubernetes utilizes the same go language version that is default for the Fedora release.
1. Provide alternate parallel versions of Kubernetes for each Fedora release, where the alternate version is still supported upstream and based on an earlier version of the go language.
1. For Fedora based Kubernetes cluster node, only one version of Kubernetes is expected to be installed. Either the default or an earlier version available as a parallel alternate.
1. For Fedora machines used to host the Kubernetes command line client (kubectl) multiple versions of the client package could be installed so that the user can manage multiple Kubernetes clusters with differing versions.
1. (provisional) Provide environment-module files to enable easy switching between kubectl versions.
1. Provide the legacy systemd unit files for Kubernetes services as a separate rpm.

## Transitions

Versions of the go language and Fedora and Kubernetes do not synchronize. During the life cycle of a Fedora release, the target version of go may go end-of-life before the Fedora end-of-life. Similarly, the default version of Kubernetes may also go end of life. The following guidelines will apply in these scenarios:

1. If go is EOL, work with the Fedora go-sig on any plans to update the version of go in Fedora. Update the default version to the next release of Kubernetes only if upstream releases security patch releases. Otherwise retain the current Kubernetes version until the Fedora release goes EOL.
1. If the default version of Kubernetes goes EOL, update to the next version of Kubernetes only if a security patch is released. Otherwise retain the current version of Kubernetes until the Fedora release goes EOL.

Upstream Kubernetes changes the go language version for a given Kubernetes release. The following guidelines will apply in this scenario.

1. The version of go is unchanged in Fedora but not current enough for Kubernetes. Work with the go maintainers in Fedora and create COPR repositories for these new versions of Kubernetes.
1. The major:minor version of go is updated in a Fedora release and current enough for Kuberentes. Syncronize updated packages with the release of the new version of go.

## Workflow

1. Use the repository issue tracker to post questions, bugs, and issues that need resolution.
1. COPR is used as the build engine until the revised spec file is formally moved to Fedora Package Sources (https://src.fedoraproject.org/rpms/kubernetes) and incorporated into Fedora.


## Useful Links

Upstream: https://kubernetes.io

The repository for the Fedora Kubernetes package is https://src.fedoraproject.org/rpms/kubernetes.

