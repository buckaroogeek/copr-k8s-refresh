COPR-K8S-REFRESH
================

Revise kuberntes spec file for Fedora

## Motivation

The current kubernetes spec file used to generate the kubernetes rpms in Fedora contains a number of artifacts that may no longer be useful or needed. The current maintainers also recognize that several improvements to the kubernetes rpms in Fedora are needed and decided to start from a fresh foundation using the go2rpm utility, inspiration from other golang projects, the existing kubernetes spec file, and the upstream spec files.

## Goal

We aim to provide first class support for Kubernetes packages in Fedora. Packages that allow Fedora machines, whether physical or virtual, to be used as host OS in Kubernetes clusters. This explicitly includes Fedora CoreOS. We also aim to provide modular Kubernetes rpms that align with the modular version of the CRI-O container runtime enhancing the role Fedora can play as a hosting OS for clusters.

## Initialization

The Fedora go-sig provides the go2rpm utility that scans a go language based project and produces an initial rpm spec file. The initial spec file in this repository was created with

```
go2rpm -f github.com/kubernetes/kubernetes k8s.io/kubernetes
```

## Requirements


## Workflow

1. Use the repository issue tracker to post questions, bugs, and issues that need resolution.

1. COPR is used as the build engine until the revised spec file is formally moved to Fedora Package Sources (https://src.fedoraproject.org/rpms/kubernetes) and incorporated into Fedora.

## COPR

See https://frostyx.cz/posts/copr-docker-compose-without-supervisord for reasonably current instructions on setting up a local COPR instance on a Fedora-based workstation. Podman and podman-compose work well as replacements for docker and docker-compose used in the post.

The Fedora COPR project is https://copr.fedorainfracloud.org/coprs/buckaroogeek/Kubernetes-Refresh/.

## Podman Notes

As noted above podman-compose and podman can be used to run COPR locally if you are interested. I chose to run COPR locally so I could experiment with configurations and build process before consuming resources on Fedora COPR. If you also have the git repository containing the spec file hosted locally and need to use ssh transport for git, then there are a couple of additional steps needed. Since COPR is running in a container, root is the user id not yours even though podman is running in rootless mode.

To enable COPR access to your local git repo, start COPR (podman-compose up -d) and then open a shell on copr_build34_1:

```
podman exec -it copr_builder_1 bash
```

In the shell, follow the usual steps to create an ssh key, add the new public key to your workstation using ssh-copy-id, and, while still in the container shell, add the key and passphrase to the local keyring.

```
ssh-keygen -t ed25519 -C "user@host"
ssh-copy-id -f user@host
ssh-add ~/.ssh/id_ed25519
```

COPR will be able to use git clone URLs such as:

```
user@host:/path/to/repo
```

## Useful Links

Upstream: https://kubernetes.io

The repository for the Fedora Kubernetes package is https://src.fedoraproject.org/rpms/kubernetes.

The repository for the Fedora Kubernetes module is https://src.fedoraproject.org/modules/kubernetes.
