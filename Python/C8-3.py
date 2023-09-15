#3.Create a Deposit() method which manages the deposit actions.

class BankAccount:
    def __init__(self,AccountNumber,Name,Balance):
        self.AccountNumber=AccountNumber
        self.Name=Name
        self.Balance=Balance

        
obj=BankAccount(120937820930,"Alwin",50000)

amount=float(input("Enter The Amout To Be Deposited : "))
obj.Balance+=amount
print("Deposited : ",amount)
print("Balance : ",obj.Balance)
