class BankAccount:
    ROI = 10.5

    def __init__(self):
        self.Name = ""
        self.Amount = 0

    def Display(self):
        print("Enter your name : ")
        self.Name = input()

        print("Enter your intial amount : ")
        self.Amount = int(input())

    def Deposite(self,value):
        self.Amount = self.Amount + value
        print("Total amount after deposite is {}".format(self.Amount))

    def Withdraw(self,value):
        self.Amount = self.Amount - value
        print("Total amount after withdrawal is {}".format(self.Amount))

    def CalculateInterest(self):
        self.Amount = (self.Amount) * ((BankAccount.ROI)/100)
        print("Total amount of Interest",self.Amount)

def main():
    user1 = BankAccount()
    user2 = BankAccount()

    user1.Display()
    user2.Display()

    user1.Deposite(500)
    user2.Deposite(500)

    user1.Withdraw(100)
    user2.Withdraw(100)

    user1.CalculateInterest()
    user2.CalculateInterest()

if __name__ == "__main__":
    main()



