def Add(v1,v2):
    Ans=v1+v2
    return Ans

def main():
    print("Enter First Number:")
    no1=int(input())
    print("Enter second Number:")
    no2=int(input())

    sum=Add(no1,no2)
    print("Addition is:",sum)

if __name__ == "__main__":
    main()

