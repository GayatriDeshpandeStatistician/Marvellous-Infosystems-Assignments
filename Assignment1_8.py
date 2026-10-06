#if n=5 then output will be * * * * *


def pattern(value):
    i = 0
    while i < value:
        print("*", end="  ")
        i = i + 1
    return i

def main():
    print("Enter a no:")
    No = int(input())

    star=pattern(No)
    # we are not printing print(star) as it will retuen value of i which is No

if __name__ == "__main__":
    main()
