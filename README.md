# mizer
command line program to automate python project setup
takes two arguments 1. project type, 2. project name

#example use
mizer -s weather
  -s = create executable script
  weather = script's name defaults to project name
  
mizer -p dust
  -p = create project directory
  dust = name of the project directory. directory contains a virtual environment and a main.py file
  you will need to activate the virtual environment in the terminal
