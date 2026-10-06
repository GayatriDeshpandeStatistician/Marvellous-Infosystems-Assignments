#write a program to insert N numbers in list & count the frequency of a number .

l=[]
print("Number of elements you want to insert:")
No = int(input())

for i in range(No):
    print("Enter a no:")
    x=int(input())
    l.append(x)

print("enter a no. to check frequency :")
check_frequency_of=int(input())
length=len(l)
count=0

for i in range(0,length):
    if check_frequency_of == l[i]:
        count = count+1

if count==0:
    print(check_frequency_of , "not found")
else:
    print(check_frequency_of,count)


