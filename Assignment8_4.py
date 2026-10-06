#A program to display addtion of digits e.g.if input=879 output=24

def Sum_of_Digits(No):

    if(No<=0):
        return 0
    else:
        return((No%10)+Sum_of_Digits(No//10))

Ret=Sum_of_Digits(879)

print("Sum of Digits of A Number is",Ret)