#BANK TRANSACTION
INITIAL_BALANCE = 2000
MIN_BAL = 500
available_balance = INITIAL_BALANCE
while(available_balance>0):
    amount = int(input("Enter the amount to withdraw : "))
    if available_balance-amount>=0:
        available_balance -= amount
        print(" Rs."+str(amount)+" withdrawn from account.")
        if available_balance>MIN_BAL:
            print("---------------------------------------")
            print("Available balance is Rs.",available_balance)
            print("---------------------------------------")
        else:
            print("---------------------------------------")
            print("Available balance is Rs."+str(available_balance)+"\nPlease  keep your account balance above Rs.500 to avoid unwanted charges.")
            print("---------------------------------------")   
    else:
        print("Sorry, Insufficient Balance!")
print("Your Current Balance is zero, you can't transact anymore!")
