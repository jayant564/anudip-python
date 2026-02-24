# Problem 4
# Problem Statement: Calculate simple interest.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time (in years): "))
si = (p * r * t) / 100
print("Simple Interest is:", si)
