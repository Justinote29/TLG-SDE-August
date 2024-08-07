#!/usr/bin/env python3

import shutil
import os


def main():

#chdir stands for change current working directory, so python
#thinks it's being executed in mycode directory
    os.chdir("/home/student/mycode/")

#let's you copy files from one place to another
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

#let's you copy whole directories from one place to another
#it will create a directory if it doesn't already exist
        #this will delete the folder before we remake it
    os.system("rm -rf /home/student/mycode/5g_research_backup/")
    shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ == "--main__":
    main()
