import Arithmetic

def main():
    print("Enter A first no:")
    no1=float(input())
    print("Enter a second no:")
    no2=float(input())

    sum = Arithmetic.Add(no1,no2)
    print("Addition is :",sum)

    difference = Arithmetic.Sub(no1,no2)
    print("Subtraction is :",difference)

    product = Arithmetic.Mult(no1,no2)
    print("Product is :",product)

    division = Arithmetic.Div(no1,no2)
    print("division is :",division)

if __name__ == "__main__":
    main()