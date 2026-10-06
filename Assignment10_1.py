#Accept directory Name & extention from user, display all the files ending with that extention.
from sys import *
import os

def DirectoryWatcher(path,extension):
    flag = os.path.isabs(path)
    print("flag:", flag)
    if flag == False:
        path = os.path.abspath(path)
        print("path:", path)

    exists = os.path.isdir(path)
    print("Exists:", exists)

    if exists:
        for foldername, subfolder,filname in os.walk(path):
            print("Current folder is : " + foldername)
            l = []
            for subf in subfolder:
                print("Sub folder of " + foldername + "is :" + subf)
            for filen in filname:
                path = os.path.join(foldername,filen)
                print("path of file is :",path)
                if filen.endswith(argv[2]):
                    l.append(filen)
                    for file in l:
                        print(file)
            print(' ')

    else:
        print("Invalid Path")

def main():
    print("---- Marvellous Infosystems by Piyush Khairnar-----")

    print("Application name : " + "DirectoryFileSearch")
    print(len(argv))

    if (len(argv) != 3):
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

#Command:python Assignment10_1.py .txt