transactions = [10000, -5000, 20000, -12000, 3000, -2000]

balance = sum(transactions)

withdrawals = [t for t in transactions if t < 0]
largest_withdrawal = min(withdrawals) if withdrawals else 0

big_deposits = sum(1 for t in transactions if t > 10000)

print("Total balance:", balance)
print("Largest withdrawal:", largest_withdrawal)
print("Deposits > 10000:", big_deposits)