#TO accept one number from user & return its factorial.

print("Enter a number")
No = int(input())
fac=1
while(No>0):
    fac=fac*No
    No=No-1
print("factirial :",fac)

