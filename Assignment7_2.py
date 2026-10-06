import threading

def EvenFactor(No):
    s=0
    for i in range(1,No,1):
        if(i % 2 == 0):
            print("Even factor:", i)
            s=s+i
    print("sum of even factors is",s)

def OddFactor(No):
    s=0
    for i in range(1,No,1):
        if(i % 2 != 0):
            print("Odd factor:", i)
            s=s+i
    print("sum of odd factors is",s)

def main():
    print("Demonstartion of Parallel programming using multiple threads")

    print("Enter number : ")
    No = int(input())

    EvenFactor(No)
    OddFactor(No)

    p1 = threading.Thread(target = EvenFactor, args = (No,))
    p2 = threading.Thread(target = OddFactor, args = (No,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
