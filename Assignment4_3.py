#filter = numbers between 70 to 90
#map = value increased by 10
#reduce = multiplication of elements in the list

from functools import reduce

select = lambda no: no if 70 <= no <= 90 else None

increment = lambda no: no + 10

multiplication = lambda no1, no2: no1 * no2


def main():
    print("Enter number of elements you want to enter:")
    isize = int(input())

    data_input = []
    print("please enter the data:")
    for iCnt in range(isize):
        value = int(input())
        data_input.append(value)

    print("data is:", data_input)

    data_filter = list(filter(select, data_input))
    print("data after filter is:", data_filter)

    data_map = list(map(increment, data_filter))
    print("data after map is:", data_map)

    output = reduce(multiplication, data_map)
    print("result after reduce is:", output)

if __name__ == "__main__":
    main()
