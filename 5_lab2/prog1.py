# Electricity Bill Calculator 
# Calculate the electricity bill based on units consumed: 
# • 0–100 → ₹5/unit 
# • 101–300 → ₹7/unit 
# • Above 300 → ₹10/unit 
# If the user is a senior citizen, apply 10% discount. 
units = int(input("Enter units consumed: "))
age = int(input("Enter age: "))

bill = 0

if units <= 100:
    bill = units * 5
elif units <= 300:
    bill = (100 * 5) + (units - 100) * 7
else:
    bill = (100 * 5) + (200 * 7) + (units - 300) * 10

# Senior citizen discount
if age >= 60:
    bill = bill - (bill * 0.10)

print("Electricity Bill = ₹", bill)
