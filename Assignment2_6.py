#write a program to display given pattern

print("Enter a number:")
no = int(input())

for i in range(no):
    for j in range(no-i):
        print("*",end=" ")
    print()