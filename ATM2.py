import sys

#beginning account balance 
account_balance = float(500.25)
#printbalance function
def printbalance():
    print("your current balance: $%.2f" % account_balance)
#deposit function
def deposit(deposit_amount):
    global account_balance
    account_balance = account_balance+deposit_amount
    print("Deposit amount was %.2f, current balance is %.2f"%(deposit_amount,account_balance))
    return (deposit_amount,account_balance)
##withdraw function
def withdraw(withdrawal_amount):
    global account_balance
    if(withdrawal_amount>account_balance):
        print("%.2f is greater than your account balance of %.2f"%(withdrawal_amount,account_balance))
    else:
        account_balance = account_balance - withdrawal_amount
        print("withdraw amount was $%.2f, your current balance is $%.2f" %(withdrawal_amount,account_balance))
    return (withdrawal_amount,account_balance)
#UserChoice
userchoice = input("what would you like to do?\n")
if (userchoice == 'D' or userchoice == 'd'):
  deposit_amount = float(input("How much would you like to deposit?\n"))
  deposit(deposit_amount)
elif (userchoice == 'W' or userchoice == 'w'):
  withdrawal_amount = float(input("How much would you like to withdraw?\n"))
  withdraw(withdrawal_amount)
elif (userchoice == "B" or userchoice == "b"):
  balance()
else:
  print("Thank you for banking with us.")