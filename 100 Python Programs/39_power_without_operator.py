# Problem 39
# Problem Statement: Calculate power without using exponent operator.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

a = int(input("Enter base: "))
b = int(input("Enter exponent: "))
result = 1
for _ in range(b):
    result *= a
print("Result is:", result)
