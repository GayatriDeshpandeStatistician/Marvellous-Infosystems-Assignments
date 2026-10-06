import multiprocessing
import os

def small(str):
    small_count=0
    for i in str:
        if i.islower():
            small_count=small_count+1
        else:
            pass
    print("Count of small is",small_count)
    print("Name of the thread is small")
    print("ID of the process is",os.getpid())

def capital(str):
    capital_count=0
    for i in str:
        if i.isupper():
            capital_count = capital_count + 1
        else:
            pass
    print("Count of capital is", capital_count)
    print("Name of the thread is capital")
    print("ID of the process is", os.getpid())

def digit(str):
    digit_count=0
    for i in str:
        if i.isdigit():
            digit_count = digit_count + 1
        else:
            pass
    print("Count of digit is", digit_count)
    print("Name of the thread is digit")
    print("ID of the process is", os.getpid())


def main():
    print("Demonstartion of Parallel programming using multiple threads")

    print("Enter a string")
    str = input()

    small(str)
    capital(str)
    digit(str)

    p1 = multiprocessing.Process(target = small, args = (str,))
    p2 = multiprocessing.Process(target = capital, args = (str,))
    p3 = multiprocessing.Process(target = digit, args = (str,))


    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
