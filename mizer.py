#!/usr/bin/env python3

import sys
import os
import subprocess


def create_executable_script(script_name):
    file_name = str(script_name + ".py")
    f = open(file_name, "w+")
    f.write("#!/usr/bin/env python3")
    f.write("\n\n\n")
    f.write("print(\"hello world\")\n")
    f.close()

    #grant full permissions
    os.chmod(file_name, 0o777)


def create_python_project(project_name):
    path = os.getcwd()
    project_dir = path + "/" + str(project_name)
    try:
         os.mkdir(project_dir)
         os.chdir(project_dir)
         create_executable_script("main")
         subprocess.run(["virtualenv", "env"])

    except:
        print("project folder already exists")
        print("choose a different project name or navigate to that project folder")


if len(sys.argv) == 3:
    if(sys.argv[1] == "-s"):
        create_executable_script(sys.argv[2])
    elif(sys.argv[1] == "-p"):
        create_python_project(sys.argv[2])
else:
    print("args missing")
