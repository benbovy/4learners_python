# SWC/DC workshops at Potsdam, Germany

This repository contains materials for [Software Carpentry](https://software-carpentry.org/) and [Data Carpentry](http://www.datacarpentry.org/) workshops hosted at Potsdam, Germany.


The present branch of the repository relates to the **Python Novice workshop -- An Introduction to Scientific Computing and Reproducible Research** held at [Potsdam Institute for Climate Impact Research (PIK)](https://www.pik-potsdam.de/), in Potsdam, Germany, on **22-23rd of February 2018**. 

The homepage with a detailed schedule for this particular workshop is found [here](https://swc-bb.github.io/2018-02-22-Potsdam-Berlin/).

 If you want to get in touch with us, please email to _swc-workshop-org@gfz-potsdam.de_. 

 
 ***
 
The workshop focuses on three tools for scientific computing and reproducible research:   
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
* 04a - Exploratory Data Analysis I: Time Series and plotting   
* 04b - Exploratory Data Analysis II: Higher dimensional (spatial) data   

All data sets, all code snippets, all [Jupyter](http://jupyter.org/) notebooks and e `requirements.yml` file for reproducibility are available through this self contained repository. 

The structure of this repository is outlined below.

    4learners                   
    │.git
    └───data
    │   │...               # find all the raw data files 
    └───figures
    │   │...               # saved figure go here
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
            │...           # solutions for coding challenges
            



_Note that we are currently working on lessons to provide our curriculum in a more generic form, hence, come back once in a while and check the [master branch](https://github.com/swc-bb/4learners) for updates._


 
 
 ***