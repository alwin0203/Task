class BankAccount:
    def __init__(self,AccountNumber,Name,Balance):
        self.AccountNumber=AccountNumber
        self.Name=Name
        self.Balance=Balance
        
obj=BankAccount(120937820930,"Alwin",50000)
 
print("Account Number : ",obj.AccountNumber)
print("Name : ",obj.Name)
print("Balance : ",obj.Balance)
