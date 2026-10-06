class Arithematic:
    def __init__(self):
        print("Inside init method")
        self.value1 = 0
        self.value2 = 0

    def Accept(self):
        self.value1 = int(input())
        self.value2 = int(input())
        print("no1 is",self.value1)
        print("no2 is",self.value2)

    def Addition(self):
        Ans = self.value1 + self.value2
        print(Ans)


    def Substraction(self):
        Ans = self.value1 - self.value2
        print(Ans)

    def Multiplication(self):
        Ans = self.value1 * self.value2
        print(Ans)


    def Division(self):
        Ans = self.value1 / self.value2
        print(Ans)

def main():
    print("Inside main method")

    obj1 = Arithematic()
    obj2 = Arithematic()
    obj3 = Arithematic()
    obj4 = Arithematic()
    obj5 = Arithematic()

    obj2.Accept()
    obj2.Addition()
    obj2.Substraction()
    obj2.Multiplication()
    obj2.Division()

    obj3.Accept()
    obj3.Addition()
    obj3.Substraction()
    obj3.Multiplication()
    obj3.Division()

    obj4.Accept()
    obj4.Addition()
    obj4.Substraction()
    obj4.Multiplication()
    obj4.Division()

    obj5.Accept()
    obj5.Addition()
    obj5.Substraction()
    obj5.Multiplication()
    obj5.Division()

if __name__ == "__main__":
    print("Inside starter")
    main()

