class HDFC:  #Class Variable
    ROI = 9.5

    def __init__(self,Name,Amount):  #Constructor
        self.AccountHolder = Name   # Instant Variable
        self.Balance = Amount       # Instant Variable
        self.Balance = Amount       # Instant Variable
        print("Welcome ",self.AccountHolder)
        print("Account gets successfully created with initial balance : ",self.Balance)

    def DisplayBalance(self):     #Instant method
        print("Hello ",self.AccountHolder)
        print("Your account balance is : ",self.Balance)
        
    @classmethod
    def DisplayBankInfo(cls):      #Class method   
        print("Welcome to HDFC Bank Portal")
        print("Our Bank is PVT LTD Bank")
        print("We provide the ROI on saving account is : ",cls.ROI)

    @staticmethod
    def DisplayKYCInfo():
        print("According to the rules of RBI you should provide below documents for KYC")
        print("Your Aadhar Card")
        print("PAN Card")
        print("Passport size Photo")
        
    def Withdraw(self,Amount):     #Instance method
        if self.Balance < Amount:
            print("There is no sufficient balance")
        else:
            self.Balance = self.Balance - Amount 
            print("Amount withdrawal successfully...")

    def Deposit(self,Amount):      #Instance method  
        self.Balance = self.Balance + Amount
        print("Amount deposited successfully...")

def main():
    print("ROI of HDFC Bank is : ",HDFC.ROI)

    HDFC.DisplayBankInfo()
    HDFC.DisplayKYCInfo()

    print("Creating new Account....")
    Amit = HDFC("Amit",5000)   #__init__(100,"Amit",5000)

    print("Creating new Account...")
    Sagar = HDFC("Sagar",3000)   #__init__(200,"Sagar",3000) 

    print("Performing operations on Amit's")
    Amit.Deposit(2000)
    Amit.DisplayBalance()

    Amit.Withdraw(1000)
    Amit.DisplayBalance()

    print("Performing operations on Sagar's")
    Sagar.Deposit(4000)
    Sagar.DisplayBalance()

    Sagar.Withdraw(500)
    Sagar.DisplayBalance()

if __name__ == "__main__":
    main()