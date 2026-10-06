from  sys import *
import os
import hashlib

def hashfile(path,buffersize=1024):
    fd=open(path,'rb')
    hasher=hashlib.md5()
    buf=fd.read(buffersize)

    while len(buf)>0:
        hasher.update(buf)
        buf=fd.read(buffersize)

    fd.close()
    return hasher.hexdigest()

def FindDuplicate(path):
    flag=os.path.isabs(path)
    print("Path is absolute path:",flag)

    if flag==False:
        path=os.path.abspath(path)
    print("Absolute path is:",path)

    exists=os.path.isdir(path)

    dups={}
    if exists:
        for dirname,subdir,filelist in os.walk(path):
            for fname in filelist:
                path=os.path.join(dirname,fname)
                file_hash=hashfile(path)

                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash]=[path]
        return dups

    else:
        print('Invalid Path')



def main():
    print("Application name is " + "display all names of duplicate files from a particular directory")

    if(len(argv)!=2):
        print("Error:Invalid number of argument")
        exit()

    if(argv[1]=="-h") or (argv[1]=="-H"):
        print("Help:This script is used to traverse specific directory and display sizes of files")
        exit()

    if(argv[1]=="-u") or (argv[1]=="-U"):
        print("Usage:ApplicationName AbsolutePath_)of_Directory_Extension")
        exit()

    try:
        arr={}
        arr=FindDuplicate(argv[1])
        print("Duplicate:",arr)
    except ValueError:
        print("Error:Invalid datatytpe of input")

if __name__=="__main__":
    main()
