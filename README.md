# Wimpy Build [![Build Status](https://travis-ci.org/wimpy/wimpy.build.svg?branch=master)](https://travis-ci.org/wimpy/wimpy.build)
Ansible role to build your application using Docker Compose, so you can define which build tool to use.
It will then create a Docker image with your application, and finally push that image to a Docker Registry.

## Parameters
The parameters are

  - `wimpy_application_name`: The name to identify your project.
  - `wimpy_release_version`: Used for tagging your docker image.
  - `wimpy_docker_image_name`: (Optional: Defaults to `wimpy_application_name`). If using a Docker Registry other than DockerHub, this parameter must contain the registry host in the name.
  - `wimpy_docker_skip_login:`: (Optional: Defaults to `False`). If using a Docker Registry that doesnt't require you to login.

### Login to Docker Registry
When publishing to a Docker Registry that needs you to login (like DockerHub), pass the following parameters

  - `wimpy_docker_registry`: **It must have trailing slash**. Empty by default, which means DockerHub.
  - `wimpy_docker_registry_username`: Credentials for the Docker Registry.
  - `wimpy_docker_registry_email`: Credentials for the Docker Registry.
  - `wimpy_docker_registry_password`: Credentials for the Docker Registry.

### AWS ECR
If you are using AWS ECR to store your Docker images, we recommend you to use [wimpy.ecr](https://github.com/wimpy/wimpy.ecr) before `wimpy.build` in your playbooks.

## Usage

```yaml
- hosts: localhost
  connection: local
  vars:
    wimpy_application_name: "my-project"
    wimpy_release_version: "9da8s9fud8"
  roles:
    - wimpy.build

```

