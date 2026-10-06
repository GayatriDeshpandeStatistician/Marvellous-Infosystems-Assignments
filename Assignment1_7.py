def fun(value):
    if value%5 == 0:
        print("True")
    else:
        print("False")

def main():
    print("enter a number")
    Number=int(input())

    Output=fun(Number)

if __name__ == "__main__":
    main()