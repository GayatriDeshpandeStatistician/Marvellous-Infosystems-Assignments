# filter = prime or not
# map =  multiply by 2
# reduce = maximum in the list
from functools import reduce

def CheckPrime(no):
    count = 0
    for i in range(1,no+1):
        if no%i == 0:
            count = count + 1
    if (count==2):
        return 1
    else:
        return 0

def Multiply(no):
    return no**2

def Max(no1,no2):
    if no1>no2:
        print(no1)
    else:
        print(no2)


def main():
    print("Enter number of elements you want to enter:")
    isize = int(input())

    data_input = []
    print("please enter the data:")
    for iCnt in range(isize):
        value = int(input())
        data_input.append(value)

    print("data is:", data_input)

    data_filter = list(filter(CheckPrime, data_input))
    print("data after filter is:", data_filter)

    data_map =list(map(Multiply, data_filter))
    print("data after map is:", data_map)

    output = reduce(Max, data_map)
    print("result after reduce is:",output)

if __name__ == "__main__":
    main()
