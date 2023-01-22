COPR-K8S-REFRESH
================

Revise kuberntes spec file for Fedora

## Motivation

The current kubernetes spec file used to generate the kubernetes rpms in Fedora contains a number of artifacts that may no longer be useful or needed. The current maintainers also recognize that several improvements to the kubernetes rpms in Fedora are needed and decided to start from a fresh foundation using the go2rpm utility, inspiration from other golang projects, the existing kubernetes spec file, and the upstream spec files.

## Goals

We aim to provide first class support for Kubernetes packages in Fedora. Packages that allow Fedora machines, whether physical or virtual, to be used as host OS in Kubernetes clusters. This explicitly includes Fedora CoreOS. 

We also aim to provide parallel installs of all supported versions of Kubernetes available for a current release of Fedora. The go language is the used to developKubernetes with each Kubernetes release based on a specific version of go (magor:minor version). Each release of Fedora has a specific version of go. Fedora 36, for example, provides go 1.18.x and Fedora 37 provides go 1.19.x. The goal for Kubernetes then would be to provide a default version of Kubernetes that aligns with the go version, and parallel installable versions of earlier kubernetes releases that are still supported.

Example Availability Matrix. Each Fedora release annotated with the go version available. D - default; A- available parallel version; O - obsolete; -- - absent.

| Kubernetes Version | K8s Go Version | F38 (1.20) | F37 (1.19) | F36 (1.18) |
| :--- | --- | --- | --- | ---: |
| 1.26 | 1.20 (1.19) | D | -- | -- | 
| 1.25 | 1.19 | A | D | -- |
| 1.24 | 1.18 | A | A | D |
| 1.23 | 1.17 | O | A | A |


## Initialization


## Requirements


## Workflow

1. Use the repository issue tracker to post questions, bugs, and issues that need resolution.

1. COPR is used as the build engine until the revised spec file is formally moved to Fedora Package Sources (https://src.fedoraproject.org/rpms/kubernetes) and incorporated into Fedora.

## COPR

See https://frostyx.cz/posts/copr-docker-compose-without-supervisord for reasonably current instructions on setting up a local COPR instance on a Fedora-based workstation. Podman and podman-compose work well as replacements for docker and docker-compose used in the post.

A local, container-based instance of COPR cannot connect to a local github repository when using the git ```user@host:/path/to/repo``` clone URL pattern. One solution is to modify the COPR docker-compose.yaml file and share the host machine's SSH agent. Add to the builder container in docker-compose.yaml the following lines (see also https://medium.com/@vanuan/ssh-and-docker-compose-7bce10b67765):

```
...
environment:
  SSH_AUTH_SOCK: $SSH_AUTH_SOCK
  ...
volumes:
  - $SSH_AUTH_SOCK:$SSH_AUTH_SOCK
...
```

The result should look something like:

```
...
  builder:
    build:
      context: docker/builder
    hostname: builder
    stdin_open: true
    tty: true
    privileged: true
    environment:
      SSH_AUTH_SOCK: $SSH_AUTH_SOCK
    volumes:
      - .:/opt/copr:z
      - $SSH_AUTH_SOCK:$SSH_AUTH_SOCK:z
...
```

The Fedora COPR project is https://copr.fedorainfracloud.org/coprs/buckaroogeek/Kubernetes-Refresh/.

## Useful Links

Upstream: https://kubernetes.io

The repository for the Fedora Kubernetes package is https://src.fedoraproject.org/rpms/kubernetes.

