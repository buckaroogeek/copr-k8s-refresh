COPR-K8S-REFRESH
================

Revise Kubernetes spec file for Fedora

## Motivation

Two primary drivers mandate a revision of the Kubernetes spec file used in Fedora. First, multiple versions of Kubernetes will be generated for each release of Fedora following the [Multiple packages with the same base name](https://docs.fedoraproject.org/en-US/packaging-guidelines/Naming/#multiple) standard. The spec file will be revised with automation in mind similar to that used for nodejs packages.

Second, The current Kubernetes spec file contains a number of artifacts that may no longer be useful or needed.

## Goals

Provide first class support for Kubernetes packages in Fedora. Packages that allow Fedora machines, whether physical or virtual, to be used as host OS in Kubernetes clusters. This explicitly includes Fedora CoreOS.

We also aim to provide packages of all supported versions of Kubernetes available for a current release of Fedora. The go language is the used to develop Kubernetes with each Kubernetes release based on a specific version of go (major:minor version). Each release of Fedora has a specific version of go. Fedora 36, for example, provides go 1.18.x and Fedora 37 provides go 1.19.x. The goal for Kubernetes then would be to provide a default version of Kubernetes that aligns with the go version, and parallel installable versions of other Kubernetes releases that are still supported.

Example Availability Matrix. Each Fedora release annotated with the go version available. D - default; A- available parallel version; O - obsolete; -- - absent.

| Kubernetes Version | K8S Go Version | F39 (1.21) | F38 (1.20) | F37 (1.19) |
| --- | --- | --- | --- | --- |
| 1.28 | 1.20 | D | -- | -- |
| 1.27 | 1.20 | A | A | -- |
| 1.26 | 1.20 | A | D | -- |
| 1.25 | 1.19 | A | A | D |
| 1.24 | 1.18 | A | A | A |


## Requirements

1. No longer provide a default version of Kubernetes for each Fedora release (see also transition notes below). 
1. Provide alternate versions of Kubernetes for each Fedora release, where the alternate version is still supported upstream and based on a version of the go language that satisfies the BuildRequires constraint.
1. For Fedora node in a Kubernetes cluster, only one version of Kubernetes can beinstalled. Alternate version packages will include symlinks to unversioned binary names. These symlinks will force dnf/rpm to reject installing more than one package (except for the client - see below).
1. The spec file will generate two (2) versions of the commandline sub-package. One version is the sibling to other sub-packages. This version will allow one one client per host. The second version of the command line client will Require EnvironmentModules and allow for multitple clients on a host. Environment module is needed to set the default value in the shell. For Fedora machines used to host the Kubernetes command line client (kubectl) multiple versions of the client package could be installed so that the user can manage multiple Kubernetes clusters with differing versions.
1. ~~(provisional) Provide an environment-module configuration to enable a standard mechanism for switching between kubectl versions.~~ kubernetes-client will not include symlinks from alternate version to ...bin/kubectl.
1. Potentially drop the service subpackages from the alternates?

## Transition Guidelines

Versions of the go language and Fedora and Kubernetes do not synchronize. During the life cycle of a Fedora release, the original target version of go may become end-of-life before the Fedora end-of-life. Similarly, the default version of Kubernetes may also go end of life before the Fedora release goes end-of-life. The following guidelines will apply in these scenarios:

1. If go is EOL, work with the Fedora go-sig on any plans to update the version of go in Fedora. Update the default version to the next release of Kubernetes only if upstream releases security patch releases. Otherwise retain the current Kubernetes version until the Fedora release goes EOL.
1. If the default version of Kubernetes goes EOL, update to the next version of Kubernetes only if a security patch is released. Otherwise retain the current version of Kubernetes until the Fedora release goes EOL.

Upstream Kubernetes changes the go language version for a given Kubernetes release. The following guidelines will apply in this scenario.

1. The version of go is unchanged in Fedora but not current enough for Kubernetes. Work with the go maintainers in Fedora and create COPR repositories for these new versions of Kubernetes.
1. The major:minor version of go is updated in a Fedora release and current enough for Kubernetes. Synchronize updated packages with the release of the new version of go.

## Workflow

1. Use the repository issue tracker to post questions, bugs, and issues that need resolution.
1. COPR is used as the build engine until the revised spec file is formally moved to Fedora Package Sources (https://src.fedoraproject.org/rpms/kubernetes) and incorporated into Fedora.

## Steps

1. modify spec file to meet goals of [Kubernetes Package Restructure change request](https://discussion.fedoraproject.org/t/f40-change-proposal-restructure-kubernetes-packages/87806) for F40. Goal with this request is to alter structure and organization of subpackages. 

## Useful Links

Upstream: https://kubernetes.io

The repository for the Fedora Kubernetes package is https://src.fedoraproject.org/rpms/kubernetes.

