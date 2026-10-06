#To count number of digits

print("Enter a number:")
no = int(input())

count=0
while no!=0:
    no//=10
    count +=1
print("Number of digits are",count)