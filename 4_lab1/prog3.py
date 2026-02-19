# E-commerce Discount Engine 
# An online shopping platform gives discounts based on: 
# • Cart value 
# • Customer membership (Silver/Gold/Platinum) 
# • Festival season 
# Apply the highest eligible discount and print the final payable amount. 
cart = float(input("Enter cart value: "))
membership = input("Enter membership (silver/gold/platinum/none): ").lower()
festival = input("Is it festival season? (yes/no): ").lower()

discount = 0

if cart > 5000:
    discount = max(discount, 10)

if membership == "silver":
    discount = max(discount, 5)
elif membership == "gold":
    discount = max(discount, 10)
elif membership == "platinum":
    discount = max(discount, 15)

if festival == "yes":
    discount = max(discount, 5)

final_amount = cart - (cart * discount / 100)

print("Discount applied:", discount, "%")
print("Final payable amount:", final_amount)
