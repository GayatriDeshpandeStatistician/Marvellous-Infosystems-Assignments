#Accept 2 directory names from user & one extension

import os
from sys import *
import shutil
import pathlib

source = argv[1]
if os.path.exists(argv[2]):
    pass
else:
    target = os.mkdir(argv[2])

def DirectoryWatcher(source,target):
    flag = os.path.isabs(source)
    print("flag:", flag)
    if flag == False:
        source = os.path.abspath(source)
        print("path:",source)

    exists = os.path.isdir(source)
    print("Exists:", exists)

    if exists:
        for foldername, subfolder, filname in os.walk(source):
            print("Current folder is : " + foldername)
            for filen in filname:
                if filen.endswith(argv[3]):
                    print(filen)
                    file = os.path.join(source,foldername, filen)
                    if os.path.exists(file):
                        print("filename:",file)
                        shutil.copy(file,target)
                print(len(os.listdir(target)))

    else:
        print("Invalid Path")

def main():
    print("---- Marvellous Infosystems by Piyush Khairnar-----")

    print("Application name : " + "DirectoryFileSearch")
    print(len(argv))

    if (len(argv) != 4):
        print("Error : Invalid number of arguments")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to traverse specific directory")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory")
        exit()

    try:
        DirectoryWatcher(argv[1],argv[2])

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invalid input")

if __name__ == "__main__":
    main()

#command:python Assignment10_4.py Demo temp .exe