#Check whether a number is prime or not

print("Enter a no:")
No = int(input())

if No == 1:
    print(" It is Neither prime nor composite.")

if No > 1:
    for n in range(2,No):
        if No%n == 0:
            print(No,"Not Prime")
            break

    else:
        print(No,"is Prime")
