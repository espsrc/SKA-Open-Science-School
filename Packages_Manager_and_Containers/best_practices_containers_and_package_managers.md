# Best practices for creating and sharing containers images and python environments for scientific software

<img width="1087" alt="imagen" src="https://user-images.githubusercontent.com/7033451/236948436-89b5fb17-5f28-49bb-b60e-a687483ffe91.png">


## Document everything

Document all installation and configuration steps, dependencies, and any other important details related to your software. This makes it easier for others to understand and replicate your work. It is essential to document all dependencies in your container image or Python environment. This includes all packages, libraries, and other software that your application relies on to run. This documentation should be clear and concise, and should be easily accessible to anyone who needs it.


## Use version control

Store all code, configuration files, data, and other resources in a version control system like Git. This makes it easy to keep track of changes, collaborate with others, and roll back to previous versions if necessary.

- https://git-scm.com/
- https://gitlab.com/rluna-gitlab/gitlab-ce
- 

## Use a containerization platform

Use a containerization platform like Docker, Moby, Podman or Singularity to create isolated, reproducible environments for your scientific software. This ensures that your software runs consistently across different systems and eliminates issues caused by dependencies and system configuration.

- https://port.us.org/
- https://goharbor.io/

## Use a package manager

Use a package manager like pip, conda/miniconda, or poetry to manage dependencies and create reproducible environments for your Python code.


## Test your environment

Test your environment to ensure that it works as expected. Use automated testing tools like pytest to catch issues early and make sure that your software works across different environments.

- GitHub CI/CD

## Share your code, data and environment

Share your code, data and environment through a public repository like GitHub or a container registry like Docker Hub. This makes it easy for others to access and use your software.

- https://binderhub.readthedocs.io/en/latest/
- https://solidproject.org/ -- Tim Berners-Lee's new WWW model

