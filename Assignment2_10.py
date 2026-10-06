#To print sum of digits
print("Enter a number:")
no = int(input())

sum=0
while no>0:
    sum = sum+no%10
    no=no//10
print("sum of digits is",sum)
