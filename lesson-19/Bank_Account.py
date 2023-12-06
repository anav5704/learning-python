class BankAccount:
    def __init__(self, name, amount):
        self.balance = amount
        self.name = name
        print(f"\n Accout: {self.name} \n Balance: ${self.balance:.2f}")

    def getBalance(self):
        print(f"\n Accout: {self.name} \n Balance: ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print("\n Deposit Compelete!")
        self.getBalance()

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            print("\n Withdraw Complete!")
            self.getBalance()
        else:
            print("\n Not enought money to withdraw")

    def transfer(self, amount, recipient):
        if self.balance > amount:
            self.balance -= amount
            recipient.deposit(amount)
            print(f"\n Succesfully transfered ${amount:.2f} to {recipient.name}'s account")
        else:
            print("\n Not enought money to withdraw")


class InterestsRewardsAcc(BankAccount):
    def deposit(self, amount):
        self.balance += amount + (amount * 0.05)
        print("\n Deposit Compelete!")
        self.getBalance()


class SavingsAccount(InterestsRewardsAcc):
    def __init__(self, name, amount):
        super().__init__(name, amount)
        self.fee = 5

    def withdraw(self, amount):
        if self.balance > amount + self.fee:
            self.balance -= (amount + self.fee)
            print("\n Withdraw Complete!")
            self.getBalance()
        else:
            print("\n Not enought money to withdraw")