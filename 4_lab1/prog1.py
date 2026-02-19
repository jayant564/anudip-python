# Banking – Suspicious Transaction Detection 
# A bank wants to flag suspicious transactions. 
# • If the transaction amount is greater than ₹2,00,000 
# • And the account is less than 6 months old 
# • And the transaction is international 
# Write a program to detect whether the transaction should be flagged for manual verification. 
amount = float(input("Enter transaction amount: "))
account_age = int(input("Enter account age in months: "))
is_international = input("Is transaction international? (yes/no): ").lower()

if amount > 200000 and account_age < 6 and is_international == "yes":
    print("Transaction flagged for manual verification")
else:
    print("Transaction is normal")
