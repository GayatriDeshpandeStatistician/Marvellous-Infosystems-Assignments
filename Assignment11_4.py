import time
from  sys import *
import os
import hashlib


def DeleteFiles(dict1):
    results=list(filter(lambda x:len(x) >1,dict1.values()))

    icnt=0;
    if len(results)>0:
        for result in results:
            for subresult in result:
                icnt=icnt+1
                if icnt >=2:
                    os.remove(subresult)
            icnt=0
    else:
        print("No duplicate files found.")

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
            print("Current folder is: " + dirname)
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

def PrintResult(dict1):
    results=list(filter(lambda  x: len(x) >1 ,dict1.values()))

    if(len(results)>0):
        print("Duplicate files found")
        print("The following files are duplicate")
        for result in results:
            for subresult in result:
                print('\t\t%s' % subresult)
            file=open("Demo1.txt","w")
            file.write(subresult + "\n")

    else:
        print("No duplicate files found")


def main():
    print("Application name is " + "Remove all  duplicate files from a particular directory")

    if(len(argv)!=2):
        print("Error:Invalid number of argument")
        exit()

    if(argv[1]=="-h") or (argv[1]=="-H"):
        print("Help:This script is used to traverse specific directory and display duplicate files")
        exit()

    if(argv[1]=="-u") or (argv[1]=="-U"):
        print("Usage:ApplicationName AbsolutePath_)of_Directory_Extension")
        exit()

    try:
        arr={}
        StartTime=time.time()
        arr=FindDuplicate(argv[1])
        PrintResult(arr)
        DeleteFiles(arr)
        endtime=time.time()

        print('Took % s seconds to evaluate .' % (endtime-StartTime))
    except ValueError:
        print("Error:Invalid datatytpe of input")
    except Exception as E:
        print("Error: Invalid input",E)

if __name__=="__main__":
    main()
