# Income Tax Calculator (India Based) 
# Create a program that calculates income tax based on the following slabs: 
# • Up to ₹2,50,000 → No tax 
# • ₹2,50,001 – ₹5,00,000 → 5% 
# • ₹5,00,001 – ₹10,00,000 → 20% 
# • Above ₹10,00,000 → 30% 
# Additionally, if the person is a senior citizen (age ≥ 60), increase the exemption limit to ₹3,00,000. 
income = float(input("Enter annual income: "))
age = int(input("Enter age: "))

exemption = 300000 if age >= 60 else 250000

if income <= exemption:
    tax = 0
elif income <= 500000:
    tax = (income - exemption) * 0.05
elif income <= 1000000:
    tax = (500000 - exemption) * 0.05 + (income - 500000) * 0.20
else:
    tax = (500000 - exemption) * 0.05 + (1000000 - 500000) * 0.20 + (income - 1000000) * 0.30

print("Income Tax =", tax)
