print("A Program to take input from user & return Addition of its factors")
print("Enter a no:")
No = int(input())

i=1
sum=0
while i<=No:
    if No%i == 0:
        sum=sum+i
    i +=1
print("sum of factors =",sum)