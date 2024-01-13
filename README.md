# Secure CQL Shell
[![Docker Image Version (latest semver)](https://img.shields.io/docker/v/dols3m/secure-cql-shell?sort=semver&style=for-the-badge&logo=docker)][docker-url]
[![Docker Pulls](https://img.shields.io/docker/pulls/dols3m/secure-cql-shell?style=for-the-badge&logo=docker)][docker-url]
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)][license-url]

Docker image for accessing CQL shell over SSL with client auth enabled. Especially useful when running in Kubernetes or a private VPS.

## Usage

Run like this:
```bash
docker run -it -e cert=$(cat cert.pem) -e key=$(cat key.pem) dols3m/secure-cql-shell host port
```

Use image tags with the `-scylla` suffix for the Scylla flavor of cqlsh:
```bash
docker run -it -e cert=$(cat cert.pem) -e key=$(cat key.pem) dols3m/secure-cql-shell:latest-scylla host port
```

Or with kubectl:
```bash
kubectl run secure-cql-shell --rm -it --env cert=$(cat cert.pem) --env key=$(cat key.pem) --image dols3m/secure-cql-shell -- host port
```

[docker-url]: https://hub.docker.com/r/dols3m/secure-cql-shell
[license-url]: https://opensource.org/licenses/MIT