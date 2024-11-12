Project2
This project demonstrates a machine learning model training pipeline, packaged in a Docker container and set up for easy deployment and tracking on GitHub Codespaces.

Table of Contents:
Installation
Usage
Main Project Structure
Running the Docker Image

Installation:
Clone the Repository:
git clone https://github.com/RohanPolam/Project_2.git
cd app

Usage:
Running the training script locally:
python3 main.py -lr 3e-5 -wd 0.003 -bs 16

Main Project Structure:
app/
main.py: main script to start a training run
mlops_hyperparameter_tuning.py: Project one code adapted for Project 2
Dockerfile: Builds the project container and installs any dependencies from requirements.txt.
requirements.txt: Lists the requrired Python packages

Running the Docker Image:
Build the Docker Image:
docker build -t rohan_polam .

Run the Docker Container in Docker:
docker run rohan_polam python3 main.py -lr 3e-5 -wd 0.003 -bs 16^C



