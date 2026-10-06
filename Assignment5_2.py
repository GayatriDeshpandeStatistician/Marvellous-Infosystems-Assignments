class Circle:
    PI = 3.14

    def __init__(self):
        print("Inside init method")
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        print("Enter the value of radius")
        self.Radius = float(input())

    def CalculateArea(self):
        self.Area = Circle.PI * (self.Radius**2)

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print("Radius is",self.Radius)
        print("Area is",self.Area)
        print("Circumference is",self.Circumference)

def main():
    object1 = Circle()
    object2 = Circle()
    Object3 = Circle()
    Object4 = Circle()

    object1.Accept()
    object2.Accept()
    Object3.Accept()
    Object4.Accept()

    object1.CalculateArea()
    object2.CalculateArea()
    Object3.CalculateArea()
    Object4.CalculateArea()

    object1.CalculateCircumference()
    object2.CalculateCircumference()
    Object3.CalculateCircumference()
    Object4.CalculateCircumference()

    object1.Display()
    object2.Display()
    Object3.Display()
    Object4.Display()

if __name__ == "__main__":
    main()

