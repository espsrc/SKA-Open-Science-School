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

### How does Binder work?

The key idea behind Binder is to take a *GitHub repository* that contains *code* and *environment files* and build a custom *Docker image* that includes all the necessary dependencies needed to run the code.

When you launch a Binder, the following steps take place:

- Binder scans/download the GitHub repository for a Binder configuration file (either binder.yml or Dockerfile).
- Binder builds a Docker image based on the instructions in the Binder configuration file. This image contains all the dependencies needed to run the code in the repository.
- Binder launches a Jupyter server that is pre-configured with the Docker image.
- The user is then directed to the Jupyter server, where they can interact with the code and data in the repository using a web interface.

![imagen](https://user-images.githubusercontent.com/7033451/236659996-ec2e0a3e-aade-4e8c-9f15-a2c20db15e7a.png)
**(C) Juliette Taka, The Turing Way.**


