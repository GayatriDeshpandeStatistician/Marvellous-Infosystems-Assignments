print("Program To Print the Numbers from 10 to 1 on Screen")

list=[1,2,3,4,5,6,7,8,9,10]
list.sort(reverse = True)
print(list)

for i in range (0,len(list)):
    print(list[i],end="  ")
