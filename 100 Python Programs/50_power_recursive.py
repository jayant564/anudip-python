# Problem 50
# Problem Statement: Calculate power using recursive function.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)

a = int(input("Enter base: "))
b = int(input("Enter exponent: "))
print("Result is:", power(a, b))
