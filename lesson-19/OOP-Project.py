from Bank_Account import *

Indee = BankAccount("Indee", 500)

Rohan = InterestsRewardsAcc("Rohan", 500)
Rohan.deposit(500)

Veer = SavingsAccount("Veer", 500)
Veer.withdraw(250)

Anav = BankAccount("Anav", 100000)
Anav.getBalance()   
Anav.deposit(258.50)
Anav.withdraw(400)
Anav.transfer(500, Indee)   
Anav.transfer(500, Rohan)

Indee.getBalance()
Rohan.getBalance()
