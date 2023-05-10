# How to include Binder in your workflow to share your results

![imagen](https://user-images.githubusercontent.com/7033451/236636063-dc712663-490e-41f4-9ce2-5f2b9f2cd3a3.png)


## What is Binder?

Binder is a tool that enables the creation of *interactive, sharable, and reproducible* computational environments based on Jupyter notebooks. It allows users to create a snapshot of their *code* and *environment*, and then share that snapshot with others in a way that allows them to interact with the code and reproduce the results.

### How does "Binder" achieve reproducibility of a study or analysis?

Binder achieves this by creating a custom computing environment based on the user's code and dependencies (and data), and then hosting that environment in the cloud. Users can access the environment through their web browser by using a direct link connected with a repository of your code, and can interact with the code and data using a Jupyter notebook interface.

### What is the key to how Binder works?

The key benefit of Binder is that it enables the creation of *self-contained, reproducible computational environments* that can be easily shared and used by others. An important part of Binder is that it allows you to containerise and create a complete environment for the execution of your scientific pipelines. At this point it is important to have knowledge of both:

- package managers and 
- containers. 

The idea with Binder is to fix/freeze the software core of your project and be able to launch it whenever you want.

### What is and What is not Binder?

**What Binder is:**

- A tool for creating and sharing reproducible computational environments based on Jupyter notebooks.
- A way to ensure that code and data are easily shareable and reproducible.
- A cloud-based service that allows users to access their environment through a web browser.
- A platform that supports a wide range of programming languages and scientific libraries.
- A way to create and share computational workflows in a transparent and reproducible way.

**What Binder is not**

- A replacement for traditional version control systems, such as Git.
- A tool for data storage or backup.
- A way to run computationally intensive workloads or large-scale data analysis.
- A platform for deploying production-ready applications.

### Binder use-cases

See the next link: https://mybinder.readthedocs.io/en/latest/using/using.html

### How does Binder work?

The key idea behind Binder is to take a *GitHub repository* that contains *code* and *environment files* and build a custom *Docker image* that includes all the necessary dependencies needed to run the code.

When you launch a Binder, the following steps take place:

- Binder scans/download the GitHub repository for a Binder configuration file (either binder.yml or Dockerfile).
- Binder builds a Docker image based on the instructions in the Binder configuration file. This image contains all the dependencies needed to run the code in the repository.
- Binder launches a Jupyter server that is pre-configured with the Docker image.
- The user is then directed to the Jupyter server, where they can interact with the code and data in the repository using a web interface.

A workflow that a scientist using Binder could adopt:

![imagen](https://user-images.githubusercontent.com/7033451/236659996-ec2e0a3e-aade-4e8c-9f15-a2c20db15e7a.png)
*Image credit: Juliette Taka, The Turing Way.*

## Creating a Binder repository and a Binder Project

Let's think that in our research work we create a code that performs different operations with data, generate plots and produces results.

- GitHub is a powerful platform for sharing code, but sharing code is not the same as executing it. 
- Running code requires multiple interdependent parts, including a copy of the code, the appropriate software to execute it, any extra packages it depends on, and input data required for the analysis.
- Additionally, you need hardware to run the code on. 
- Installing and configuring these parts correctly can be challenging, particularly when there are multiple dependencies involved.

Standardizing the execution of software is crucial to making research more reproducible and accessible. When researchers share their code, they must also share the necessary dependencies and configuration files to run it. Without standardization, reproducing the results can become a daunting task, especially for researchers who are not familiar with the particular software stack being used.

*So how about standardising or "binderising" the way we package software, code and data so that it can be easily run on public and private cloud servers? 

To do it we have to take into account the next points:

- *Hardware*: A server to execute code, typically hosted in the cloud but can also be on-premise hardware.
- *Computational environment*: An isolated environment that contains:
  - The appropriate software
  - Any extra package dependencies
  - Required input data
  - A copy of the code (Notebooks or scripts)
- *URL*: A web address where the computational environment is running, allowing you or your collaborators to interact with the code.

### Where I run a "Binderised" application?

Binder can be deployed on your own infrastructure (then we will show your the overall steps), giving you complete control over the hardware and software environment. In addition, you can customize the environment to your needs and specifications, including the ability to install custom software packages, set up authentication and authorization, and even limit the resources available to individual users.

The most common and straightforward option is to use mybinder.org website that provides a free and public version of the interface, making it accessible to anyone who wants to share their computational work with others without worrying about the technical details of setting up the infrastructure. 

MyBinder.org has some limitations that users should be aware of:

- Resource constraints: myBinder runs on servers with limited resources, so if your notebook requires a lot of CPU or memory, it may not be able to run on myBinder.
- Time limits: myBinder sessions have a maximum runtime of 12 hours. If your session exceeds this limit, it will be terminated, and any changes you made during the session will be lost.
- Disk space limits: myBinder provides a limited amount of disk space for each session, which may not be sufficient for some large datasets or files.
- Network limitations: myBinder sessions are hosted on servers with limited network bandwidth, so if your notebook requires a lot of data transfer, it may be slow or even fail to load.
- Concurrent usage: myBinder has a limit on the number of concurrent users that can access a single repository at a time. If the limit is reached, other users may have to wait or be unable to access the repository.
- Security: myBinder provides a secure computing environment, but it is important to note that the environment is shared with other users. Thus, users should be cautious about sharing sensitive data or code through myBinder.

### First steps to create Binder project in a GitHub repository

A Binder (also called a Binder-ready repository) is a code repository that contains at least two things:

- Code or content that you’d like people to run. This might be a Jupyter Notebook that explains an idea, or an R script that makes a visualization or a Python Script that run a data analysis.
- Configuration files for your environment. These files are used by Binder to build the environment needed to run your code. For a list of all configuration files available.

Configuration files for a Binder repo may be placed in the root of your repository or in a `binder/` folder in the repository’s root (i.e. `myproject/binder/`).

We can create the environments for Python Julia and R, as follows:

#### Python

To create a Binder with Python support, you need to include a requirements.txt or environment.yml file in your repository.

#### Julia

To build an environment with Julia, include a configuration file called Project.toml.

#### R 

To build an environment with R you need to create a `runtime.txt` file with the following format:

``r-<version>-<YYYY>-<MM>-<DD>``

This will provide you R of given version (such as 4.1, 3.6, etc), and a CRAN snapshot to install libraries from on the given date. To install more R packages from CRAN you need to add an `install.R` file to your repo. 

### Our first Binder project: in Python

Binder supports a wide range of computational environments for running Jupyter notebooks and other scientific computing workflows as commented before. These environments include popular programming languages such as Python, R, Julia, and MATLAB, as well as specialized tools for data analysis and machine learning.

Python is a particularly popular choice for scientific computing, and Binder supports Python environments via the Conda package manager or the pip package manager, so from here on we will only focus on *Python-based development*. For the rest of the environments you can consult the corresponding documentation.

#### Create a public repository

We will create a repository on GitHub (or other repository provider) with the name radio-data-analysis where we will progressively incorporate the necessary elements to create a Binderised version of our analysis ready to be executed.

- Remember to add a licence according to this project.
- Make the repository public and accessible.

#### Create your code and pipeline

We are going to use the next code as an example:

```
import numpy as np
import matplotlib.pyplot as plt
import astropy.io.fits as fits
from astropy.utils.data import download_file
from skimage import filters

# Load FITS image
image_file = download_file('http://data.astropy.org/tutorials/FITS-images/HorseHead.fits', cache=True )
hdulist = fits.open(image_file)
image = hdulist[0].data

# Save FITS image as PNG
plt.imsave('/output/original.png', image, cmap='gray')

# Apply filters
gaussian_image = filters.gaussian(image, sigma=2)
sobel_image = filters.sobel(image)

# Save filtered images as PNGs
plt.imsave('/output/gaussian.png', gaussian_image, cmap='gray')
plt.imsave('/output/sobel.png', sobel_image, cmap='gray')

# Display original and filtered images
fig, axs = plt.subplots(2, 2, figsize=(8, 8))
axs[0, 0].imshow(image, cmap='gray')
axs[0, 0].set_title('Original')
axs[0, 1].imshow(gaussian_image, cmap='gray')
axs[0, 1].set_title('Gaussian')
axs[1, 0].imshow(sobel_image, cmap='gray')
axs[1, 0].set_title('Sobel')
axs[1, 1].axis('off')

# Save figure as PNG
fig.savefig('/output/filtered.png')
```

To have this code in your project, clone this repository or download directly this Jupyter notebook with the name: `index.ipynb`

#### Add the `requirements.txt` file

As our study focuses on python code, here we can use several options to deploy the software environment and packages that our pipeline will need, such as using the requirements file: ``requirements.txt`` or the working environment file with conda `environment.yml`.

Create a new file in your repository with the name ``requirements.txt`` and add the next lines:

```
numpy==1.24.0
matplotlib==3.7.0
astropy>=5.2
scikit-image==0.20.0
```

*Remember to indicate the specific versions if necessary for your analysis.*


#### Adding the runtime version of Python

You need to include a file named `runtime.txt` with the python runtime name.

(Create a file named: runtime.txt and add `python3.8` to the file)

#### Running this first example on BinderHub


[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/manuparra/binder-pipeline-v1/HEAD)

[![Binder](https://srcdev.skatelescope.org/binderhub/badge_logo.svg)](https://srcdev.skatelescope.org/binderhub/v2/gh/manuparra/binder-pipeline-v1/HEAD)

See all the bootstrap examples: https://github.com/binder-examples/

### Creating a Binder by using our container definition

For a Dockerfile to work on Binder, it must meet the following requirements:

It must install a recent version of Jupyter Notebook and JupyterLab. This should be installed via pip with the notebook and jupyterlab packages. So in your dockerfile, you should have a command like:


```
RUN python3 -m pip install --no-cache-dir notebook jupyterlab
```

It must explicitly specify a tag in the image you source. When sourcing a pre-existing Docker image with FROM, a tag is required. The tag cannot be latest. Note that tag naming conventions differ between images, so we recommend using the SHA tag of the image.

Here’s an example of a Dockerfile FROM statement that would work.

```
FROM jupyter/scipy-notebook:cf6258237ff9
```

It must set up a user whose uid is 1000. It is bad practice to run processes in containers as root, and on binder we do not allow root container processes.


```
ARG NB_USER=jovyan
ARG NB_UID=1000
ENV USER ${NB_USER}
ENV NB_UID ${NB_UID}
ENV HOME /home/${NB_USER}

RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${NB_UID} \
    ${NB_USER}
```

We can use an example of Dockerfile:

https://github.com/binder-examples/minimal-dockerfile

and then modify to run our pipeline. 

### Ensure reproducibility for your Binder repository

Here are some tips to ensure reproducibility of your Binder links even if you must re-build your repository image:

#### Pin dependencies

Don’t just specify numpy, specify numpy==1.12.0.

`pip freeze` is a handy tool to export the exact version of every Python package in your environment in a format that can be used in `requirements.txt`.

`conda env export -n <env-name>` is the equivalent for anaconda’s `environment.yml` file.

#### Using Dockerfiles

- You need a popular Docker Image.

```
# Note that there must be a tag
FROM jupyter/scipy-notebook:cf6258237ff9
```

- You are building complex software.
- You are using a language that is not directly supported



#### Deploying Binder in your own infrastructure

![imagen](https://github.com/spsrc/SKA-Open-Science-School/assets/7033451/1c8a5f5a-6df3-473d-9dca-d87dca18aefd)


## Conclusions



