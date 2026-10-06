# A program to print pattern 5 4 3 2 1  when No=5

def Display(No):

    if(No>0):
        print(No,end="  ")
        No = No - 1
        Display(No)

Display(5)