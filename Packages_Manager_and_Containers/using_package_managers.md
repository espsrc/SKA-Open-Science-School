# Using package managers to manage scientific software deployment and reproducibility

In this project, we will be working on creating a reproducible environment for a scientific pipeline. 

To achieve reproducibility and portability, we will be utilizing several package managers like pip, virtual environments, and conda. Incrementally, you will learn the advantages of each of the package managers and which is the best option for your software distribution.

These tools will help us to manage dependencies and ensure that our pipeline can be executed in the same manner on different systems. With these package managers, we can create isolated environments with specific versions of packages and their dependencies. This approach will help us avoid issues with conflicting dependencies and make it easier to share our work with others. 

By the end of this session, you will have a fully scientific reproducible software environment that can be easily recreated and shared with others.

## Our example for this session

For this session we will prepare an example to perform the next steps in a pipeline.

- We will use the next FITS file
- We will load this FITS file
- We will print a few plots with different filters
- We will apply flagging to the data
- Finnally we will apply a cleannig to the data

Libraries that we will need:

- NumPy
- Astropy
- MathPlotLib
- CASA Modular


### Using pip

### Using a Python VirtualEnv

Install virtualenv. You can install virtualenv using pip. Open a command prompt or terminal and type the following command:

``pip3 install virtualenv`` or ``pip install virtualenv``

Check what the version we will install (and is installed in our system):

``which python3``

Create the virtual environment. You can select the name to identify the environment and what will be the version of Python.

``virtualenv skaschool -p $(which python3)``

This will create a new directory named env in your current directory with the name `skaschool`, which will contain the virtual environment.

Now is time to activate the virtual environment. To activate the virtual environment, type the following command:

``source skaschool/bin/activate``

Deactivate the virtual environment. To deactivate the virtual environment, simply type the following command:

``source skaschool/bin/deactivate``

This will deactivate the virtual environment and return you to your original Python environment, so everything installed will not be available.

Again, activate the recently created environment: 

``source skaschool/bin/activate``

and now we will create a file with the requirements, named `requirements.txt` to install in this environment.

Create a file `requirements.txt` with the next lines:


```
numpy
astropy
matplotlib
casatools
casatasks
```

And then we install all these packages for this study:

```
pip install -r requirements.txt

```

All this packages are ready to be used withing the skaschool environment.

(?) What about the versions of the packages we work with? Recommendation: Fix the versions of the packages to make sure that our code only works with those packages.

Change `requirements.txt` and include the versions of the packages:


```
numpy==XXX
astropy==XXX
matplotlib==XXX
casatools==XXX
casatasks==XXX
```


