import threading

def thread1():
    for i in range(1,51):
        print(i,end='  ')

def thread2():
    n=50
    while(n>=1):
        print(n,end='  ')
        n=n-1

def main():
    print("Demonstartion of Serial programming using multiple threads")

    thread1()
    thread2()

    t1 = threading.Thread(target=thread1, args=())
    t2 = threading.Thread(target=thread2, args=())

    t1.start()
    t2.start()

    print("Exit from main")

if __name__ == "__main__":
    main()
