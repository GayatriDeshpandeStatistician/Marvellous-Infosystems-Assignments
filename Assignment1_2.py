def ChkNum(value):
    if value % 2 == 0:
        print("This is an Even Number")
    else:
        print("This is an Odd Number")


def main():
    print("Enter a Number:")
    Number = int(input())

    Check_Number=ChkNum(Number)


if __name__ == "__main__":
    main()
