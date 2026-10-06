#write a program to insert N numbers in list & return the minimum Number.

l=[]
print("Number of elements you want to insert:")
No = int(input())

for i in range(No):
    print("Enter a no:")
    x=int(input())
    l.append(x)

min=l[0]
for i in range(No):
    if(l[i]<min):
        min=l[i]
print("Minimum Number is:",min)
