#1.Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.


class BankAccount:
    accountNumber = int(input("Enter Account Number : "))
    Name =(input("Enter Account Holder Name : "))
    Balance = int(input("Enter Account Balance : "))

obj=BankAccount()
print("Account Number : ",obj.accountNumber)
print("Name : ",obj.Name)
print("Balance : ",obj.Balance)
