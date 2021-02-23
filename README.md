# Honeycomb Technology website

The [Honeycomb technology website](https://www.honeycomb-technology.co.uk/) was created using the Python Library Flask and has been deployed to Heroku. 
This page will explain how to get the [Honeycomb technology website](https://www.honeycomb-technology.co.uk/) and how to deploy the changes onto Heroku 

## Step 1 - Install Anaconda 
The easiest way to install initial python packages is by downloading the [Anaconda's data science toolkit](https://www.anaconda.com/products/individual) 


## Step 2 - Pull the files from this repository locally
You will need to pull this repository on your computer/laptop. The easiest way to do that is by navigating to a directory of your choice the running the command 

```bash
git pull https://github.com/yonisM/honeycomb_technology.git
```

if you don't have git on your computer/laptop, the command above will not run. You can [download it very easily from the git website](https://git-scm.com/downloads)


## Step 3 - Download the appropriate Python Packages

Once you have pulled the repository locally, on your command line, navigate to the directory that contains the file **requirements.txt**. This file contains all the Python packages you need run the Flask application locally. 
To download all the Python packages from the **requirements.txt**, run the command below:

```bash
 pip install -r requirements.txt
```

*note - the installation from requirements.txt is different on MacOS. Google it*

## Step 4 - Run the application locally

Now you are ready to run the application locally. On your command line, Simply navigate to the directory that contains the file **server.py** then run the command 

```bash
 python server.py
```

If successfully, you will be given a URL in the command prompt you can copy and paste into the browser of choice. You can then make the changes as you please. 


## Step 4 - Deploying to Heroku. 

Once you are finished making your changes, simply push the changes back into GitHub and Heroku will automatically pick up the changes. Give it a minute or so and the website will automatically update. Easy. 
If you made CSS changes, you may need to clear your cache from your browser or simply go into a different browser or open your browser of choice in incognito mode. 











