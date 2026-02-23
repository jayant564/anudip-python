prices = [1200, 2500, 1200, 1800, 700]

#remove duplicates
unique_prices = list(set(prices))

total = sum(unique_prices)

#apply 10% discount if total>5000
if total>5000:
    total*=0.9

#add 18% GST
total*=0.18

print("Final payable amount: ", total)
