#write a program to insert N numbers in list & return the maximum Number.

l=[]
print("Number of elements you want to insert:")
No = int(input())

for i in range(No):
    print("Enter a no:")
    x=int(input())
    l.append(x)

max=l[0]
for i in range(No):
    if(l[i]>max):
        max=l[i]
print("Maximum Number is:",max)
