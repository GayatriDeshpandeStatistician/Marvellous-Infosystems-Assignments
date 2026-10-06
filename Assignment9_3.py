#Accept file name from user & create new file named as Demo.txt &then copy data from ABC.txt to Demo.txt
import os
import sys
from sys import *


def Read_File(FileName):
        fd = open(FileName, "r")
        Data = fd.read()
        print("Data from the file is")
        print(Data)

        fd.close()

        fd = open("Demo.txt","w")
        fd.write(Data)


def main():
    print("Enter the name of the file that you want to create")

    Name = sys.argv[1]
    Read_File(Name)


if __name__ == "__main__":
    main()

#Command:python Assignment9_3.py ABC.txt