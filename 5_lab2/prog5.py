# ATM Withdrawal System 
# Conditions: 
# • Account balance must be sufficient 
# • Daily withdrawal limit ₹50,000 
# • ATM cash availability 
# Display appropriate messages for each condition failure.
balance = float(input("Enter account balance: "))
withdraw = float(input("Enter withdrawal amount: "))
atm_cash = float(input("Enter ATM cash available: "))

if withdraw > balance:
    print("Transaction failed: Insufficient account balance")
elif withdraw > 50000:
    print("Transaction failed: Exceeds daily withdrawal limit")
elif withdraw > atm_cash:
    print("Transaction failed: ATM does not have sufficient cash")
else:
    print("Withdrawal successful")
    balance = balance - withdraw
    print("Remaining balance =", balance)
