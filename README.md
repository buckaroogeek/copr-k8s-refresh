COPR-K8S-REFRESH
================

Revise kuberntes spec file for Fedora

## Motivation

The current kubernetes spec file used to generate the kubernetes rpms in Fedora contains a number of artifacts that may no longer be useful or needed. The current maintainers also recognize that several improvements to the kubernetes rpms in Fedora are needed and decided to start from a fresh foundation using the go2rpm utility, inspiration from other golang projects, the existing kubernetes spec file, and the upstream spec files.

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
See https://frostyx.cz/posts/copr-docker-compose-without-supervisord for reasonably current instructions on setting up a COPR instance on a local Fedora-based workstation. Podman and podman-compose work well as replacements for docker and docker-compose.

The Fedora COPR project is https://copr.fedorainfracloud.org/coprs/buckaroogeek/Kubernetes-Refresh/.
