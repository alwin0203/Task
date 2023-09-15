class BankAccount:
    def __init__(self,AccountNumber,Name,Balance):
        self.AccountNumber=AccountNumber
        self.Name=Name
        self.Balance=Balance

        
obj=BankAccount(120937820930,"Alwin",50000)


def Withdrawal():
    amount=float(input("Enter The Amount To withdraw : "))
    if obj.Balance>=amount:
       obj.Balance-=amount
       print("Withdrawed : ",amount)
       print("Balance : ",obj.Balance)
    else:
        print("Insufficient Balance")
Withdrawal()

        
