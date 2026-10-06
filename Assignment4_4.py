# filter = even numbers
# map = square
# reduce = sum of all numbers in list

from functools import reduce

CheckEven = lambda no: (no % 2 ==0 )

Square = lambda no: no**2  #or no*no

Addition = lambda no1, no2: no1 + no2


def main():
    print("Enter number of elements you want to enter:")
    isize = int(input())

    data_input = []
    print("please enter the data:")
    for iCnt in range(isize):
        value = int(input())
        data_input.append(value)

    print("data is:", data_input)

    data_filter = list(filter(CheckEven, data_input))
    print("data after filter is:", data_filter)

    data_map = list(map(Square, data_filter))
    print("data after map is:", data_map)

    output = reduce(Addition, data_map)
    print("result after reduce is:",output)

if __name__ == "__main__":
    main()
