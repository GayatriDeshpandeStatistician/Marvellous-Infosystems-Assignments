

import MarvellousNum


def ListPrime(Data):
    Prime_List = []
    for num in Data:
        if num == 0 or num == 1:
            continue

        for i in range(2, num // 2 + 1):
            if num % i == 0:
                break
        else:
            Prime_List.append(num)
    print("Prime numbers are:", Prime_List)
    sum = MarvellousNum.ChkPrime(Prime_List)


def main():
    print("How many numbers you want to enter:")
    size = int(input())
    List = []
    for i in range(0, size, 1):
        Value = int(input())
        List.append(Value)
    print(List)

    ListPrime(List)


if __name__ == "__main__":
    main()
