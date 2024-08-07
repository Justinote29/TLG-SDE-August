
#the name of the import matches the file name minus the .py
#these two files MUST be in the same directory
import first_module

def main():
    #calling main() function from first_module
    first_module.main()
    print("Module #2 Name=", __name__)
    

if __name__ == "__main__":
        main()
