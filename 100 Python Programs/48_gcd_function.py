# Problem 48
# Problem Statement: Find GCD using function.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("GCD is:", gcd(a, b))
