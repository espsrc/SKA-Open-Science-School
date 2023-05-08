# Using package managers to manage scientific software deployment and reproducibility

<img width="1041" alt="imagen" src="https://user-images.githubusercontent.com/7033451/236792845-a4efe4a6-f057-4013-9234-4cfce7441b23.png">

In this project, we will be working on creating a reproducible environment for a scientific pipeline. 

To achieve reproducibility and portability, we will be utilizing several package managers like pip, virtual environments, and conda. Incrementally, you will learn the advantages of each of the package managers and which is the best option for your software distribution.

These tools will help us to manage dependencies and ensure that our pipeline can be executed in the same manner on different systems. With these package managers, we can create isolated environments with specific versions of packages and their dependencies. This approach will help us avoid issues with conflicting dependencies and make it easier to share our work with others. 

By the end of this session, you will have a fully scientific reproducible software environment that can be easily recreated and shared with others.

## Our pipeline for this session

For this session we will prepare an example to perform the next steps in a pipeline.

- We will use the next FITS file: http://cdsarc.u-strasbg.fr/viz-bin/getCatFile_Redirect/?-plus=-%2b&J/A%2bA/632/A78/./fits/HCG16_CD_rob2_MS.pbcor.fits
- We will load this FITS file.
- We will create a few plots with different filters.
- We will compose a grid of these plots as output.

Libraries that we will need:

- `numpy`
- `matplotlib`
- `astropy`
- `skimage (scikit-image)`

The code is located here:

https://github.com/spsrc/SKA-Open-Science-School/blob/main/Packages_Manager_and_Containers/pipeline/run.py

The Notebook is here:

https://github.com/spsrc/SKA-Open-Science-School/blob/main/Packages_Manager_and_Containers/pipeline/run.ipynb


## Python Package Managers

<img width="907" alt="imagen" src="https://user-images.githubusercontent.com/7033451/236794732-815861e3-5b12-41d8-a657-22adf76edad1.png">

We will work on how to reproduce this proposed software environment documented in (Our example for this session)[#our_pipeline_for_this_session].

### Using pip

Using pip without a virtual environment can result in package conflicts and compatibility issues. When pip installs a package, it installs it system-wide and it could potentially conflict with other packages or system libraries that depend on different versions of the same package. This can lead to unexpected behavior and make it difficult to reproduce results or debug issues.

For these reasons, it is generally recommended to use virtual environments and then install packages with pip to create isolated environments for our scientific pipelines.

So the ideal for software reproducibility management is to use Python virtual environments, such as the following.

### Using a Python VirtualEnv

In order to use Python Virtual envs, yo have to install virtualenv. To do it open a shell and type the following command:

``sudo apt-get install python3-virtualenv``

Check what the version we will install (and is installed in our system):

``which python3``

Create the virtual environment. You can select the name to identify the environment and what will be the version of Python.

``virtualenv skaschool -p $(which python3)``

This will create a new directory named env in your current directory with the name `skaschool`, which will contain the virtual environment.

Now is time to activate the virtual environment. To activate the virtual environment, type the following command:

``source skaschool/bin/activate``

Deactivate the virtual environment. To deactivate the virtual environment, simply type the following command:

``deactivate``

This will deactivate the virtual environment and return you to your original Python environment, so everything installed will not be available.

Again, activate the recently created environment: 

``source skaschool/bin/activate``

and now we will create a file with the requirements, named `requirements.txt` to install in this environment.

Create a file `requirements.txt` with the next lines:


```
numpy
matplotlib
astropy
scikit-image
```

And then we install all these packages for this study:

```
pip install -r requirements.txt

```

All this packages are ready to be used withing the skaschool environment.

(?) What about the versions of the packages we work with? 
- Recommendation: Fix the versions of the packages to make sure that our code only works with those packages.

We can check our current version of installed packages:

```
pip list
```

It will show something like the next:

```
Package             Version  
------------------- ---------
astropy             5.2.2    
contourpy           1.0.7    
cycler              0.11.0   
fonttools           4.39.3   
imageio             2.28.1   
importlib-resources 5.12.0   
kiwisolver          1.4.4    
lazy-loader         0.2      
matplotlib          3.7.1    
networkx            3.1      
numpy               1.24.3   
packaging           23.1     
Pillow              9.5.0    
pip                 20.0.2   
pkg-resources       0.0.0    
pyerfa              2.0.0.3  
pyparsing           3.0.9    
python-dateutil     2.8.2    
PyWavelets          1.4.1    
PyYAML              6.0      
scikit-image        0.20.0   
scipy               1.9.1    
setuptools          44.0.0   
six                 1.16.0   
tifffile            2023.4.12
wheel               0.34.2   
zipp                3.15.0   

```


Now we can fix our dependencies to a concrete version. Change `requirements.txt` and include the versions of the packages:


```
numpy==1.24.0
matplotlib==3.7.0
astropy>=5.2
scikit-image==0.20.0
```

Once we've tested this environment, we can close and deactivate it:

``deactivate``

### Conda/Miniconda

We recommend using conda to manage the dependencies. Miniconda is a light-weight version of Anaconda. 
First we show how to install Miniconda if you don't have it already. More details https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html#regular-installation

Miniconda works in Linux, Windows and MacOSX.

#### Installation 

Miniconda for Linux:

```
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash ./Miniconda3-latest-Linux-x86_64.sh
rm ./Miniconda3-latest-Linux-x86_64.sh
```

Miniconda for macOS:

```
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
bash Miniconda3-latest-MacOSX-x86_64.sh
rm Miniconda3-latest-MacOSX-x86_64.sh
```

Miniconda for Windows: You can follow the instructions (download the exe file) from here: https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html


### Adding Mamba 

Mamba!

Mamba is a very efficient dependency solver. If you don't have it, you can substitute all mamba commands with conda, and it will do the same but slower. You can install it in the base environment with:

```
conda install mamba -n base -c conda-forge
```

#### Working with Conda environments

```
mamba create --name skaschool_py3.8 python=3.8
```

But we might also want to have another environment with a different python runtime

```
mamba create --name skaschool_py3.9 python=3.X
```

To activate this environment, use:

```
mamba activate skaschool_py3.8
```

To deactivate an active environment, use the next:

```
mamba deactivate
```

We activate the environment again:

```
mamba activate skaschool_py3.8
```

Check the version of python here:


```
python --version
```

Now we can check what is installed in this -empty- environment:

```
conda list
```

Will show something like:

```
# packages in environment at /home/mparra/miniconda3/envs/skaschool_py3.8:
#
# Name                    Version                   Build  Channel
_libgcc_mutex             0.1                        main  
_openmp_mutex             4.5                       1_gnu  
ca-certificates           2022.3.29            h06a4308_0  
certifi                   2020.6.20          pyhd3eb1b0_3  
ld_impl_linux-64          2.35.1               h7274673_9  
libffi                    3.3                  he6710b0_2  
libgcc-ng                 9.3.0               h5101ec6_17  
libgomp                   9.3.0               h5101ec6_17  
libstdcxx-ng              9.3.0               hd4cf53a_17  
ncurses                   6.3                  h7f8727e_2  
openssl                   1.1.1n               h7f8727e_0  
pip                       21.2.2           py36h06a4308_0  
python                    3.6.13               h12debd9_1  
readline                  8.1.2                h7f8727e_1  
setuptools                58.0.4           py36h06a4308_0  
sqlite                    3.38.2               hc218d9a_0  
tk                        8.6.11               h1ccaba5_0  
wheel                     0.37.1             pyhd3eb1b0_0  
xz                        5.2.5                h7b6447c_0  
zlib                      1.2.12               h7f8727e_1  
```

#### Adding packages to a conda environment


### Manually and on demand 

We can install any software available in `anaconda.org` with a simple command. For example:

```mamba install matplotlib```
or 

```mamba install numpy```

(?) We can include version as well as with `pip` and requirements.

We can even install the pip package manager:

```
mamba install pip
```

To export the list of packages installed in a conda environment to an environment.yml file, you can use the following command:

```
conda env export --name <environment_name> > environment.yml
```

Replace `<environment_name>` with the name of the environment you want to export or without it to use the current environment. This will create an `environment.yml` file in the current directory containing the list of packages and their versions installed in the specified environment. With `--from-history` you can get all of the installed packages.

```
conda env export --from-history
```


#### From an `environment.yml` file

One way to create and manage conda environments is by using an environment.yml file. This file contains the specifications of the packages needed for the project, including the name and version of the packages, and any required dependencies. 
Here's our example for this environment.yml file:


```
name: skaschool_py3.8_automated
  
channels:
- conda-forge
- defaults

dependencies:
- 
- numpy
- astropy
- matplotlib
- casatools
- casatasks
```

To test it, first we need deactivate our environment:

```
mamba deactivate
```

And now we can create a new environment based in our environment.yml created by using:

```
mamba env create -f environment.yml
```

Once the environment is created, you can activate it using the following command:

```
conda activate skaschool_py3.8_automated
```

or check what is the list of conda environments with

```
conda env list
```

#### Removing environments

We can easily remove any environment created (you may need to deactivate it first).

```
conda env remove -n skaschool_py3.8
```

### Conclusion

Our replicable project with conda should contain the following:

- environment.yml file
- Our data file
- Code or Notebook with the pipeline
- Instructions to 
  - activate the environment with conda and
  - run the pipeline.
  
  


