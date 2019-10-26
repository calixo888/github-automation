import os
import sys
import shutil
import subprocess
from os.path import expanduser

home = expanduser("~")

link = sys.argv[1]

repo_name = link.split("/")[-1][:-4]

os.chdir(home)

directories = [i for i in os.listdir(os.getcwd())]

for folder_name in directories:
    if folder_name[:6] == "cloner":
        shutil.rmtree(os.path.join(os.getcwd(), folder_name))

os.mkdir("cloner-" + repo_name)
os.chdir("cloner-" + repo_name)
subprocess.run("git clone {}".format(link).split())
