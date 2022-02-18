#!/usr/bin/env python3

import sys
import os
import subprocess
import argparse

"""create an executable script in the current directory"""
def create_executable_script(script_name):
    
    file_name = str(script_name + ".py")

    if os.path.isfile(file_name):
        print("file with that name already exists in the current directory")
    else:
        f = open(file_name, "w+")
        f.write("#!/usr/bin/env python3")
        f.write("\n\n")
        f.write("print(\"hello world\")\n")
        f.close()

        #grant full permissions
        os.chmod(file_name, 0o777)

        return file_name

"""create a project folder in the current directory"""
def create_python_project(project_name):
    path = os.getcwd()
    project_dir = path + "/" + str(project_name)
    
    try:
         os.mkdir(project_dir)
         os.chdir(project_dir)
         script_file = create_executable_script("main")
         virtual_environment = str(project_name+"-env")
         subprocess.run(["virtualenv",virtual_environment],stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT) #suppress virtualenv output
         
    except  FileExistsError:
        print("project folder already exists")
        print("choose a different project name or navigate to that project folder")

#take care of arguments
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--script_option", help="the option to create script", action='store_true')
parser.add_argument("-p", "--project_option", help="the option to setup a project", action='store_true')
parser.add_argument("name", help="set the name of the script/project", type=str)
args = parser.parse_args()

if not args.script_option and not args.project_option:
    print("provide an option for the program.\n")
    print("1. to create script only: -s.")
    print("2. to create project folder: -p.")
elif args.script_option and args.project_option:
    print("only one arguments needs to be set not both")
elif args.script_option and not args.project_option:
    create_executable_script(args.name)
elif args.project_option and not args.script_option:
    create_python_project(args.name)