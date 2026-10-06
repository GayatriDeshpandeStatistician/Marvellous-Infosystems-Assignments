# A program to print pattern 1 2 3 4 5 when No=5

def Display(No):
    if(No>0):
         No = No - 1
         Display(No)
         print(No+1, end="  ")

Display(5)
