#Accept directory name & two extentions from user & rename .txt as .doc

from sys import *
import os

def DirectoryWatcher(path,extension1,extension2):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)
    exists = os.path.isdir(path)

    if exists:
        for foldername, subfolder,filname in os.walk(path):
            print("Current folder is : " + foldername)
            l=[]
            for subf in subfolder:
                print("Sub folder of " + foldername + "is :" + subf)
            for filen in filname:
                path=os.path.join(foldername,subf,filen)
                if filen.endswith(argv[2]):
                    l.append(filen)
                    for file in l:
                        print(file)
                        old_file_name = os.path.join(foldername, filen)
                        print("old file:",old_file_name)
                        new_file_name = old_file_name.replace(argv[2], argv[3])
                        print("new file:",new_file_name)
                        new=os.rename(old_file_name, new_file_name)

            print(' ')

    else:
        print("Invalid Path")


def main():
    print("----- Marvellous Infosystems by Piyush Khairnar-----")

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
        DirectoryWatcher(argv[1],argv[2],argv[3])

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invalid input")

if __name__ == "__main__":
    main()

#Command:python Assignment10_2.py .txt .doc