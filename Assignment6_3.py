class Numbers:


    def __init__(self):
          self.value = 0
          self.Arr = list()

    def Chkprime(self):
        i= 0
        Flag = True

        for i in range(2, int(No / 2) + 1):
            if (No % i == 0):
                Flag = False
                break

        return Flag


    def ChkPerfect(self):


    def SumFactors(self):

    def Factors(self):
        for i in range(0, self.value):
            if (self.__ChkPrime(self.Arr[i]) == True):
                print("{} is a prime number".format(self.Arr[i]))

class Arithmetic(Numbers):
    pass









