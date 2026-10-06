#Enter a no.'n' which will display matrix of order n of *

def pattern(n):
    i = 0
    print("Star Pattern")

    while (i < n):
        j = 0
        while (j < n):
            j = j + 1
            print("*", end=" ")
        i = i + 1
        print("")

def main():
    print("Enter a no  :")
    n = int(input())

    star=pattern(n)

if __name__ == "__main__":
    main()


