# Wimpy Build
Ansible playbook to build your application using Docker Compose, so you can define which build tool to use.
It will then create a docker image with your application, and finally push that image to a Docker Registry.

## Required Parameters
The required parameters are

  - `wimpy_project_name`: The name to identify your project.
  - `wimpy_release_version`: Used for tagging your docker image.

## Optional Parameters
The optional parameters are

  - `wimpy_docker_registry`: Defaults to Docker Hub. It must have trailing slash.
  - `wimpy_docker_image_name`: Defaults to your project's name.

### Login to Docker Registry
This role handles the login with your Docker Registry.

When publishing to other Docker Registry that needs you to login (like DockerHub), pass the following parameters

  - `wimpy_docker_registry_username`
  - `wimpy_docker_registry_email`
  - `wimpy_docker_registry_password`

If you pass the `wimpy_docker_registry` parameter containing an AWS ECR address, it will login with ECR, given that the computer executing this role has the right permissions.


