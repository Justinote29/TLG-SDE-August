#!/usr/bin/env python3
hostname = input("What value should we set for hostname?")
## Notice how the next line has changed
## here we use the str.lower() method to return a lowercase string
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    #print a second line if howname is mtg
    print("hostname matches expected config")
 # always pring out to user no matter value of hostname
print("Exiting the script")
