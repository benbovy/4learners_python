# SWC/DC workshops at Potsdam, Germany

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/swc-bb/4learners_python/master)

This repository contains materials for [Software Carpentry](https://software-carpentry.org/) and [Data Carpentry](http://www.datacarpentry.org/) workshops hosted at Potsdam, Germany.

The present branch of the repository relates to the **Python Novice workshop -- An Introduction to Scientific Computing and Reproducible Research** held at [Potsdam Institute for Climate Impact Research (PIK)](https://www.pik-potsdam.de/), in Potsdam, Germany, on **22-23rd of February 2018**.

The homepage with a detailed schedule for this particular workshop is found [here](https://swc-bb.github.io/2018-02-22-Potsdam-Berlin/).

In order to re-run the workshop materials we encourage you to use the [conda](https://conda.io/docs/) package manager. Once installed, create an environment and install all required dependencies on your machine by typing 

`conda env create -f environment.yml`

into your console. Alternatively, you may launch [binder](https://binderhub.readthedocs.io/en/latest/) to get a reproducible executable environment immediately in your browser. Simply click the _binder_ icon in the upper left corner.

If you want to get in touch with us, please email to swc-workshop-org@gfz-potsdam.de.

_If you are here because you are looking for a particular Python workshop you attended in the past, make sure you visit the appropriate branch of this repository (note that the branches are ordered by date)._


***

The workshop focuses on three foundational tools for scientific computing and reproducible research:
* the shell
* git for version control
* scientific computing with Python


## the shell

In this workshop we closely follow the Software Carpentry lesson [The Unix Shell](https://swcarpentry.github.io/shell-novice/).

## git for version control

In this workshop we closely follow the Software Carpentry lesson [Version Control with Git](https://swcarpentry.github.io/git-novice/).


## scientific computing with Python

In this workshop we teach four main aspects of scientific computing with Python.

* 01 - Introduction to Python
* 02 - Functions and Code Structures
* 03 - Defensive Programming
* 04a - Exploratory Data Analysis I: Introduction to pandas
* 04b - Exploratory Data Analysis II: Time Series and plotting
* 04c - (optional) Exploratory Data Analysis III: Higher dimensional (spatial) data

All data sets, all code snippets, all [Jupyter](http://jupyter.org/) notebooks and the `requirements.yml` file(s) for reproducibility are available through this self contained repository.

The structure of this repository is outlined below:

    4learners
    │.git                  # git internals
    │.gitignore            # specify files/folders to be ignored by git
    └───data
    │   │...               # find all the raw data files
    └───figures
    │   │...               # saved figures go here
    └───notebooks
    │   └───_img
    │   │   │...           # rendered images are placed here
    │   │...               # find all Jupyter notebooks here
    │
    │README.md
    │requirements.yml      # conda environment specifications for reproducibility
    └───src
        │...               # here go the code snippets and scripts
        └───_solutions
            │...           # solutions for coding challenges (don't cheat yourself ;-))


_Note that we are currently working on lessons to present our curriculum in a more generic form, hence, come back once in a while and check the [master branch](https://github.com/swc-bb/4learners_python) for updates._


 ***
