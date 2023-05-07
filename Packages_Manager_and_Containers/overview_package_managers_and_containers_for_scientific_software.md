# Overview of package managers and containers for scientific software

## Introduction 

Package managers and containers are essential tools for managing scientific software dependencies and creating reproducible environments for software development and analysis.

Package managers such as *pip*, *conda (mamba, miniconda, etc)*, and *apt-get* (as many others) are used to install, update, and manage software packages and their dependencies. They ensure that the necessary libraries and tools are installed and configured correctly, and can help avoid version conflicts or other compatibility issues.

Containers, on the other hand, are complete and portable environments that include not only the software packages and their dependencies but also the necessary libraries and operating system. Containers can be easily shared and run on different platforms, ensuring that the software works the same way regardless of the underlying infrastructure.

Using package managers and containers can provide several benefits, such as:

- Reproducibility: By capturing the software and its dependencies, it's easier to recreate the environment and reproduce the same results.
- Portability: Containers can be easily shared and run on different platforms, ensuring that the software works the same way regardless of the underlying infrastructure.
- Isolation: Containers and virtual environments can help isolate the software and its dependencies from other software on the system, reducing the risk of conflicts or compatibility issues.

### Advantages and Disadvantages of package managers

- Package managers can automate the installation and management of software dependencies, making it easier to reproduce computational environments, can ensure that software dependencies are compatible with each other and with the operating system, reducing the risk of conflicts or incompatibilities and can provide a centralized repository of software packages, making it easier to discover and install new software.

- Package managers may have limited support for specific operating systems or software packages and thet may require manual configuration or troubleshooting to resolve conflicts or incompatibilities.

### Advantages and Disadvantages of containers
 
- Containers can encapsulate an entire computational environment, including the operating system, software dependencies, and data, making it easier to reproduce computational environments, they can provide a standardized and portable way to share computational environments across different systems and platforms and it can provide a secure and isolated environment for running software, reducing the risk of conflicts or security vulnerabilities.

- Containers can have a larger overhead in terms of disk space and computational resources compared to other methods of software distribution and installation, they may require additional configuration or setup to interact with other systems or services outside of the container environment, and they have limited support for specific operating systems or architectures, depending on the containerization technology used.

## Python Packages Manager and software environments

<img width="661" alt="imagen" src="https://user-images.githubusercontent.com/7033451/236664427-087dd3b1-9324-47a1-b95d-897145fa349e.png">

*Image credit: xkcd - http://xkcd.com/1987*

Python package managers, such as pip and conda, help to solve the issue of reproducibility of scientific software by managing the dependencies of the software. Dependencies are other software packages that the scientific software relies on to function correctly. Managing these dependencies ensures that the scientific software can run consistently across different environments.

When a scientific software project is shared with others, the project's dependencies are listed in a requirements file or environment file. This file is used by the package manager to install the necessary dependencies for the project. By using a requirements or environment file, the dependencies can be pinned to specific versions, ensuring that the same versions of the dependencies are used across different environments.

In this context a Python package manager is a tool that:
- helps to manage dependencies and installation of Python packages, and
- automates the process of installing, upgrading, and uninstalling packages and their dependencies.

One example of a Python package manager, as commented before, is `pip`, which is the default package manager for Python. pip allows you to install packages from the Python Package Index (PyPI) as well as from other sources, and it automatically installs any required dependencies.

For example, to install the popular NumPy package using pip, you would simply run the following command in your terminal or command prompt:

`pip install numpy`

This would download and install the NumPy package and any necessary dependencies on your system, ready to use it.

### pip 

`pip` is the package installer for Python. It is a command-line tool that allows you to install, upgrade, and uninstall Python packages from the Python Package Index (PyPI), as well as other indexes. 

PyPI is a repository of software packages for the Python programming language. Pip helps to resolve dependencies and manages the installation of the required packages, ensuring that the correct version of each package is installed. It is a crucial tool for managing Python packages and creating reproducible environments for scientific software development and analysis.

### Poetry

Poetry is a new Python package manager that simplify dependency management and packaging of Python projects. It provides a simple and easy-to-use command-line interface for managing project dependencies, creating virtual environments, and packaging projects for distribution.

Poetry has gained popularity in the Python community due to its simplicity and focus on reproducibility of environments.

### Conda

Conda is an open-source package management system and environment management system that helps to install, run, and update software packages and their dependencies. It was primarily designed for data science and scientific computing but can be used for any software in any language. Conda supports packages written in multiple programming languages, including Python, R, Ruby, Lua, Scala, Java, and others.

Conda works by creating isolated environments, where each environment has its own set of packages and dependencies. This approach helps to avoid conflicts between packages and makes it easy to reproduce an environment on different machines. Conda also has a built-in mechanism for creating and sharing environments, making it easy to distribute and reproduce complex software projects.

#### Miniconda

Miniconda is a minimal installer for conda. It includes only conda, Python, and a few essential packages needed to get started with conda. Miniconda allows you to create isolated environments to manage packages and dependencies for different projects, and it also provides the flexibility to install and manage packages from both the conda-forge and PyPI repositories. 

It is a simple alternative to the full Anaconda distribution, which includes a comprehensive collection of packages for scientific computing and data analysis.

#### Mamba

Mamba is a high-performance package manager and an alternative to conda. It is designed to be much faster than conda and has some additional features, such as parallel downloading of packages and an improved solver for resolving package dependencies. Like conda, mamba also supports creating and managing virtual environments, installing packages from various sources, and creating reproducible environments for scientific software development and analysis.

### Virtual environments

Virtual environments are an important concept in the Python ecosystem, as they allow you to create isolated environments with their own set of packages and dependencies.

conda, pip, poetry, etc. support virtual environments. With pip, you can use virtualenv or venv to create a virtual environment, while with conda, you can create and manage environments using the conda command.

Virtual environments are an important tool for managing dependencies and creating reproducible environments, and they can be used in combination with these package managers to provide an even more robust solution.

## Containers in software reproducibility

Containers are an increasingly popular way to achieve reproducibility in scientific software development and analysis. Containers provide a complete and isolated environment for running code, including all the required dependencies and libraries, making it easier to ensure that the code runs the same way across different systems.

Using containers, scientists can package their entire computational environment, including the operating system, libraries, and dependencies, into a single file, which can be easily shared and deployed on different machines. Containers are designed to be platform-independent, so they can run on any operating system that supports the container runtime.

Containers can be created and managed using containerization technologies such as Docker or Singularity. These technologies allow for the creation of images that can be easily shared, reused, and version-controlled, enabling users to capture and replicate their computational environment exactly as it was at the time of analysis.

### Docker

Docker is a containerization platform that enables software developers to build, deploy, and run applications in containers. Containers are lightweight and portable environments (more than VMs) that can be easily moved between systems, making it easier to ensure that code runs consistently across different machines. 

Docker containers are similar to virtual machines but use the host system's kernel instead of creating a separate operating system. This means that Docker containers can start up much faster and require less overhead than virtual machines, making them a popular choice for many types of applications.

### Singularity

Singularity is a containerization platform designed specifically for high-performance computing (HPC) environments. Like Docker, Singularity allows users to create lightweight and portable containers that can be easily moved between systems (portability and reproducibility).

Singularity is optimized for running scientific and HPC applications and it also includes features such as support for parallel processing and integration with job scheduling systems commonly used in HPC environments.







