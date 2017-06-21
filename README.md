# Wimpy Build [![Build Status](https://travis-ci.org/wimpy/wimpy.build.svg?branch=master)](https://travis-ci.org/wimpy/wimpy.build)
Ansible role to help you build and push Docker images to a Docker Registry. 

## Parameters
The parameters are

  - `wimpy_application_name`: The name to identify your project.
  - `wimpy_release_version`: Used for tagging your docker image.
  - `wimpy_docker_image_name`: (Optional: Defaults to `wimpy_application_name`). If using a Docker Registry other than DockerHub, this parameter must contain the registry host in the name.
  - `wimpy_docker_skip_login:`: (Optional: Defaults to `False`). If using a Docker Registry that doesnt't require you to login.
  - `wimpy_docker_image_force`: (Optional: Defaults to `no`). Creates a new docker image even if one with the same name and tag already exists in the repository. Useful to override SNAPSHOT builds.
  - `wimpy_docker_image_skip_latest_tag`: (Optional: Defaults to `False`). If set to True it will not tag the built image as latest. Useful if releasing a patch for non mainstream branch like older versions or building non stable code.

### Login to Docker Registry
When publishing to a Docker Registry that needs you to login (like DockerHub), pass the following parameters

  - `wimpy_docker_registry`: **It must have trailing slash**. If you pass an empty string, it will use DockerHub. Otherwise, it will create an AWS ECR.
  - `wimpy_docker_registry_username`: Credentials for the Docker Registry.
  - `wimpy_docker_registry_email`: Credentials for the Docker Registry.
  - `wimpy_docker_registry_password`: Credentials for the Docker Registry.

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

