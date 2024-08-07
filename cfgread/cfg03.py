#!/usr/bin/env python3

import os

newName = input("What do you want to name your file: ").strip()
os.rename("vlanconfig.cfg", newName)
## create file object in "r"ead mode
lines = 0;
with open(newName, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()

    for line in configlist:
        lines += 1
## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)
print(f"There are {lines} lines")

