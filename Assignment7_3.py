import threading

def Evenlist(No):
    s=0
    l=[]
    for i in range(1,No,1):
        if(i % 2 == 0):
            l.append(i)
            print("list of even factors",l)
            s=s+i
    print("sum of even factors is",s)

def Oddlist(No):
    s=0
    l=[]
    for i in range(1,No,1):
        if(i % 2 != 0):
            l.append(i)
            print("list of Odd factors", l)
            s=s+i
    print("sum of odd factors is",s)

def main():
    print("Demonstartion of Parallel programming using multiple threads")

    print("Enter number : ")
    No = int(input())

    Evenlist(No)
    Oddlist(No)

    p1 = threading.Thread(target = Evenlist, args = (No,))
    p2 = threading.Thread(target = Oddlist, args = (No,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
