#!/usr/bin/env python3
import shutil
import os

def main();
#make python start in the home directory, so user can run the program from any location on the system and it will always start here
    os.chdir('/home/student/mycode/')


#we move the file to a new location
    shutil.move('raynor.obj', 'ceph_storage/')

#we prompt user for a new name for the file
    xname = input('What is the new name for kerrigan.obj? ')

#we rename the file
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)


if __name__ == "__main__":
    main()


