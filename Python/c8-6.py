#6.Create a display() method to display account details.
class BankAccount:
    def __init__(self,AccountNumber,Name,Balance):
        self.AccountNumber=AccountNumber
        self.Name=Name
        self.Balance=Balance

        
obj=BankAccount(120937820930,"Alwin",50000)
amount=float(input("Enter The Amount To withdraw : "))
if obj.Balance>=amount:
    obj.Balance-=amount
    print("Amount Before bank Fee : ",obj.Balance)
a=obj.Balance-((obj.Balance*5)/100)
print("Amount After Applying bank fee : ",a)
    

