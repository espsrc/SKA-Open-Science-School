# Working with containerisation for software reproducibility

<img width="1087" alt="imagen" src="https://user-images.githubusercontent.com/7033451/237016601-02afac1c-53ec-4368-8a55-0304664922a4.png">

The aim of containerisation of scientific software is to provide a way to package and distribute scientific software in a way that ensures reproducibility of computational experiments across different computing environments. 

Containerisation creates a self-contained environment that includes all the software dependencies and libraries required to run the scientific software, regardless of the underlying operating system or hardware. 

This means that researchers can create a single container that contains all the software tools needed for their analysis, and share this container with others to ensure that their results can be replicated. 

This is particularly important in our context, the scientific research where the ability to reproduce results is critical for validating scientific claims and ensuring the integrity of research findings.


## Docker

Docker is a platform for containerizing applications, enabling software to be packaged into a self-contained unit that can run consistently across different environments. With Docker, users can create, distribute, and run containers that encapsulate applications and their dependencies, ensuring that they run the same way on any system. Docker is widely used in scientific computing because it provides a convenient way to create reproducible environments that can be shared with others, making it easier to collaborate and reproduce results. Docker also offers a large and growing library of pre-built images for a wide range of scientific software, allowing users to quickly get started with complex applications.

### Installation

There are many ways to install docker. The easiest way is to use the developer's own instructions for the particular operating system. You can follow the steps [here](https://docs.docker.com/engine/install/).

### Use and creation of container images

Docker provides a huge public repository-like catalogue of ready-to-use container images. In its repository, anyone can upload an image centrally and then be used/downloaded by anyone else. 

See Docker repository of images: https://dockerhub.com

In addition, docker allows you to build your own images and use them from a public or private repository (on your own machine).

### First example with docker: executing a containerised version of `CASA`

Pull of the image from a public repository of images in DockerHub (https://hub.docker.com/r/amigahub/casa):

```
docker pull amigahub/casa:6.5.0
```

Run the container based on the this image:

```
docker run -it amigahub/casa:6.5.0 ./casa-6.5.0-15-py3.6/bin/casa 
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

The first part is to create the minimal environment within an image:

```
FROM ubuntu:20.04

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3.6 \
    python3-pip \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip3 install astropy numpy matplotlib scikit-image

```

Another option is to create a `Dockerfile` by using a conda environment:

```
FROM continuumio/miniconda3:latest

# Install system dependencies
RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create a Conda environment 
RUN conda create -n casa6 python=3.8 && \
    conda install -n casa6 -c conda-forge casa=6.2.0 && \
    conda clean -ya

RUN pip install numpy astropy matplotlib scikit-image

```

Then build the image with:

```
docker build -t pipeline:v1 .
```

Once created we can see the images created/downloaded:

```
docker images
```

To test this recent image in a container, you have to type the next:

```
docker run -it pipeline:v1 python3
```

You can check that all the libraries were installed:

```
import astropy
...
```

Finally exit from the container.

Now we are going to complete the code to store the results and to include the code to execute our pipeline:

```
FROM ubuntu:20.04

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3.6 \
    python3-pip \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip3 install astropy numpy matplotlib scikit-image

RUN mkdir /code/
RUN mkdir /output/

COPY run.py /code/
CMD ["python3", "/code/run.py"]
```

We need to build this new image:


```
docker build -t pipeline:v2
```

Then we have to run the pipeline:

```
docker run -it pipeline:v2
```

And check the results: Wait, where are the outputs of this pipeline?

We have to connect our user storage with the container storage:

```
docker run -it -v ./output:/output pipeline:v2
```

Now we can see the outputs.

**In this point you have created two ways to share your pipeline:**
*- 1) A static version *
*- 2) A flexible version *



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

```
docker tag pipeline:v2 manuparra/pipeline:v2
```


Here, pipeline:v1 /  pipeline:v2  is the name of your local image, manuparra is your username on the registry platform, repository is the name of the repository where you want to push the image, and tag is the tag you want to assign to the image.

After tagging the image, you can push it to the registry platform using the following command:

```
docker push manuparra/pipeline:v1
```

```
docker push manuparra/pipeline:v2
```

This command will push the tagged image to the registry platform under the specified repository and tag.


## Singularity

Singularity is a containerization platform that allows users to create and run portable and reproducible environments. Unlike Docker, Singularity containers do not require root access to run, making them a popular choice in scientific computing, where users often do not have administrative privileges on the computing infrastructure. Singularity can run Docker containers, as well as its own container format, and has a user-friendly command-line interface. It is commonly used in high-performance computing environments to provide reproducible software stacks for scientific workflows.

### Installation

See installation instructions for:

- [Linux](https://ska-telescope.gitlab.io/src/ska-src-training-containers/#h.cpchh14b5v93)
- [MacOSX](https://ska-telescope.gitlab.io/src/ska-src-training-containers/#h.nuqiqiwd9xpa)
- [Windows](https://ska-telescope.gitlab.io/src/ska-src-training-containers/#h.vfuryuhkc9ca)


### Basic commands

To work with the Singularity there are really only a few commands that provide us with all the operations:

- build : Build a container on your user endpoint or build environment
- exec : Execute a command to your container
- inspect : See labels, run and test scripts, and environment variables
- pull : pull an image from Docker or Singularity Hub
- run : Run your image as an executable
- shell : Shell into your image

### Hub of images

Singularity has its own image platform in `.sif` format, but with singularity it is possible to directly use any container that is available on DockerHub. This makes both systems compatible, allowing the use of singularity's own images or other consolidated images from dockerhub.

### Running an example of image

Go to the environment where you have Singularity installed to do some tests. 

```
singularity pull docker://godlovedc/lolcow
```

This command will simply download an image that already exists in Docker (`docker://godlovedc/lolcow` from DockerHub: lol docker), and store it as a local file with `SIF format`.

Then, we execute the image as an executable, simply typing:

```
singularity run lolcow_latest.sif
```

### Building our image with Singularity

We have to create a Definition file `.def` like this (check https://docs.sylabs.io/guides/3.7/user-guide/definition_files.html):

*Create a file with name pipeline.def*

```
Bootstrap: library
From: ubuntu:20.04

%labels
    maintainer="Manuel Parra<mparra@iaa.es>"
    description="Singularity image "

%post
    # Install required packages
    apt-get update && \
    apt-get install -y python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

    # Install required Python packages
    pip3 install numpy astropy numpy matplotlib scikit-image

```

This is a first approach that will allow us to run a python environment with all the containerised dependencies and then run the pipeline from our own filesystem, using one of the most interesting features of Singularity.

Time to build this definition file:

```
sudo singularity build pipeline.sif pipeline.def
```

**Note: sudo here ?**

You can see a newly created `pipeline.sif` file that stores the image. This image is fully shareable and distributable.

To execute it:

```
singularity run pipeline.sif
```

And after this step we can run your pipeline:

```
Singularity> python3.8 run.py
```

*Error: It it looking for `/output/`but it is not in your system.*

Change your path within the `run.py` or, better, to mount this folder for the container :

*Remember: Create an `output` folder*

```
singularity run -B output/:/output pipeline.sif
```

Finally the last option to containerise this pipeline is to include the code inside the image:

```
Bootstrap: library
From: ubuntu:20.04

%labels
    maintainer="Manuel Parra<mparra@iaa.es>"
    description="Singularity image "

%files
    run.py run.py
%post
    # Install required packages
    apt-get update && \
    apt-get install -y python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

    # Install required Python packages
    pip3 install numpy astropy numpy matplotlib scikit-image

%runscript
    python3.8 run.py

```

Build the image:

```
sudo singularity build pipeline-v2.sif pipeline-v2.def
```

And then run the container:

```
singularity run -B output/:/output pipeline-v2.sif

```

Check the output folder ! :)




