#write a program to insert N numbers in list & return their Addition.

l=[]
print("Number of elements you want to insert:")
No = int(input())

for i in range(No):
    print("Enter a no:")
    x=int(input())
    l.append(x)

sum = 0
for i in range(No):
    sum=sum+l[i]
print("sum of elements = ",sum)
