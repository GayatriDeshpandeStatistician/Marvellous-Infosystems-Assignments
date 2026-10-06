import threading

def Even(No):
    for i in range(1,No,1):
        if(i % 2 == 0):
            print("Even number : ",i)

def Odd(No):
    for i in range(1,No,1):
        if(i % 2 != 0):
            print("Odd number : ",i)

def main():
    print("Demonstartion of Parallel programming using multiple threads")
    Number = 20

    p1 = threading.Thread(target = Even, args = (Number,))
    p2 = threading.Thread(target = Odd, args = (Number,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("End of main")

if __name__ == "__main__":
    main()
