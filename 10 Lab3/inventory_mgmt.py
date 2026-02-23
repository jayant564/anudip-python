stock = [0, 5, 20, 8, 0, 15, 3]

# Remove 0 stock
stock = [s for s in stock if s != 0]

# Restock items below 10
for i in range(len(stock)):
    if stock[i] < 10:
        stock[i] += 50

total_inventory = sum(stock)

print("Updated stock:", stock)
print("Total inventory:", total_inventory)