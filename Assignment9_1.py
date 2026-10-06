#Accept file name from user & check if it exists or not

import os

def CreateFile(FileName):
    if(os.path.exists(FileName)):
        print("File Exists")
        return
    else:
        print("File doesn't Exist")

def main():
    print("Enter the name of the file that you want to check")
    Name = input()

    CreateFile(Name)

if __name__ == "__main__":
    main()