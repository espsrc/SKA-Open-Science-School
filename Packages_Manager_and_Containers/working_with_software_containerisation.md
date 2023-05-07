# Working with containerisation for software reproducibility

The aim of containerisation of scientific software is to provide a way to package and distribute scientific software in a way that ensures reproducibility of computational experiments across different computing environments. 

Containerisation creates a self-contained environment that includes all the software dependencies and libraries required to run the scientific software, regardless of the underlying operating system or hardware. 

This means that researchers can create a single container that contains all the software tools needed for their analysis, and share this container with others to ensure that their results can be replicated. 

This is particularly important in our context, the scientific research where the ability to reproduce results is critical for validating scientific claims and ensuring the integrity of research findings.


## Docker

Docker is a platform for containerizing applications, enabling software to be packaged into a self-contained unit that can run consistently across different environments. With Docker, users can create, distribute, and run containers that encapsulate applications and their dependencies, ensuring that they run the same way on any system. Docker is widely used in scientific computing because it provides a convenient way to create reproducible environments that can be shared with others, making it easier to collaborate and reproduce results. Docker also offers a large and growing library of pre-built images for a wide range of scientific software, allowing users to quickly get started with complex applications.

### Installation

There are many ways to install docker. The easiest way is to use the developer's own instructions for the particular operating system. You can follow the steps here.

### Use and creation of container images

Docker provides a huge public repository-like catalogue of ready-to-use container images. In its repository, anyone can upload an image centrally and then be used/downloaded by anyone else. 

See Docker repository of images: https://dockerhub.com

In addition, docker allows you to build your own images and use them from a public or private repository (on your own machine).

### First example with docker: executing a containerised version of `CASA`

Pull of the image from a public repository of images in DockerHub:

```
docker pull amigahub/casa:6.5
```

Run the container based on the this image:

```
docker run -it casa:6.5 
```

Show containers running and the list of images pulled:

```
# See all the containers running
docker ps
# See all the containers running and the historical list
docker ps -a
# See all the images pulled and ready to instantiate as a container
docker images
```

### Building our own container with our specific software.

**Remember, we are using the same example of the section [Package Managers](using_package_managers.md)**

The idea is to build an ad-hoc image in order to be able to run the software transparently and reproducibly. 

For this purpose, containerisation tools provide utilities and image definition languages that enable this task.  Both docker and singularity have a definition language, which although different in structure are perfectly understandable. 

In Docker this file is called `Dockerfile` and in Singularity it is called `Definition File` or `.def`.

```
FROM ubuntu:20.04

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3.6 \
    python3-pip \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip3 install numpy astropy matplotlib

RUN wget https://casa.nrao.edu/download/distro/casa-release-5.7.2-2.el7/binaries/casa-release-5.7.2-2.el7.tar.gz && \
    tar xzf casa-release-5.7.2-2.el7.tar.gz && \
    rm -f casa-release-5.7.2-2.el7.tar.gz && \
    cd /casa-release-5.7.2-2.el7 && \
    ./bin/extractpkg.sh

ENV PATH="/casa-release-5.7.2-2.el7/bin:${PATH}"

# Copy the Python script to the container
COPY pipeline.py .

# Run the Python script
CMD ["python3", "pipeline.py"]
```

Another option is to create a `Dockerfile` by using a conda environment:


```
FROM continuumio/miniconda3:latest

# Install system dependencies
RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create a Conda environment for CASA
RUN conda create -n casa6 python=3.8 && \
    conda install -n casa6 -c conda-forge casa=6.2.0 && \
    conda clean -ya

# Activate CASA environment and install additional Python packages
SHELL ["conda", "run", "-n", "casa6", "/bin/bash", "-c"]
RUN pip install numpy astropy matplotlib

# Copy the Python script to the container
COPY pipeline.py .

# Run the Python script
CMD ["python", "pipeline.py"]
```

Make sure to put your `pipeline.py` file in the same directory as the `Dockerfile` before building the image. 

Then build the image with:

```
docker build -t pipeline:v1 .
```

And then run the image:

```
docker run -it pipeline:v1
```

### Publishing our image to a public docker registry

First, you need to have an account on a container registry platform like Docker Hub or Google Container Registry (GCR).

Next, you need to login to the registry platform from your local machine within the CLI. You can use the following command to login to Docker Hub:

```
docker login
```

Once you are logged in, you can tag your local image with the registry URL using the following command:


```
docker tag pipeline:v1 manuparra/pipeline:v1
```

Here, pipeline:v1 is the name of your local image, manuparra is your username on the registry platform, repository is the name of the repository where you want to push the image, and tag is the tag you want to assign to the image.

After tagging the image, you can push it to the registry platform using the following command:

```
docker push manuparra/pipeline:v1
```

This command will push the tagged image to the registry platform under the specified repository and tag.




