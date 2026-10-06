from sys import *
import os
import hashlib

def hashfile(path,buffersize=1024):
    afile=open(path,"rb")
    hasher=hashlib.md5()
    buf=afile.read(buffersize)
    while len(buf)>0:
        hasher.update(buf)
        buf=afile.read(buffersize)
    afile.close()
    return hasher.hexdigest()

def DisplayCheckSum(path):
    flag=os.path.isabs(path)
    print("This is absolute path:",flag)
    if flag==False:
        path=os.path.abspath(path)
        print("Absolute path is:",path)

    exists = os.path.isdir(path)
    print("specified path is an  directory path: ", exists)

    if exists:
        for foldername,subfolder,filelist in os.walk(path):
            print("Current directory is: " + foldername)

            for fname in filelist:
                print("File inside folder " + foldername + " is " + fname)
                path=os.path.join(foldername,fname)
                file_hash=hashfile(path)

                print(path)
                print(file_hash)
                print(' ')

    else:
        print("Invalid path")

def main():
    print("________________________________________________________________________________________")
    print("Application is Display checksum of all the files which are enclosed in a particular directory")
    print("________________________________________________________________________________________")
    print("length of command line argumrnt is:",len(argv))

    if(len(argv)!=2):
        print("Error: Insufficient arguments or invalid number of arguments")
        exit()

    if(argv[1]=="-h") or (argv[1]=="-H"):
        print("Help:This script is used to traverse specific directory and display checksum of files")
        exit()

    if(argv[1]=="-u") or (argv[1]=="-U"):
        print("Usage:ApplicationName AbsolutePath_of_Directory_Extension")
        exit()

    try:
        DisplayCheckSum(argv[1])
    except Exception:
        print("Invalid Input")

if __name__=="__main__":
    main()
