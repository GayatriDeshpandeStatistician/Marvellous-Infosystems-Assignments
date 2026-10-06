class Demo:

    value = 0
    def __init__(self,x,y):
        print("Inside init method")
        self.No1 = x
        self.No2 = y

    def Fun(self):
        print("Inside instance1 method")
        print(self.No1)

    def Gun(self):
        print("Inside instance2 method")
        print(self.No2)

def main():
    print("Inside main method")

    object1 = Demo(11,21)
    object2 = Demo(51,101)

    object1.Fun()
    object1.Gun()
    object2.Fun()
    object2.Gun()

if __name__ == "__main__":
    main()




