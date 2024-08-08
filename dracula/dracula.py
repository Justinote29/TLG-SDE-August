#!/usr/bin/env python3

def main():
    #count variable
    count = 0
    #open dracula.txt file in read mode
    with open ("dracula.txt", "r") as draculatext:
        #open a new file to write to
        with open("vampiretext.txt", "w") as fang:
            for line in draculatext:
                if "vampire" in line.lower():
                    #increment counter when a line contains vampire regardless of case
                    count += 1
                    print(line.strip())
                    #write line to vampire.txt file
                    fang.write(line)
    print()
    #print total lines with vampire count
    print(f"There are {count} lines that contain the word vampire.")








if __name__ == "__main__":
    main()
