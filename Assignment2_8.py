#write a program to display given pattern

print("Enter a number:")
no = int(input())

for i in range(no):
    for j in range(i+1):
        print(j+1,end=" ")
    print()