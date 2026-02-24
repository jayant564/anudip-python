# Problem 5
# Problem Statement: Calculate compound interest.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time (in years): "))
ci = p * ((1 + r / 100) ** t) - p
print("Compound Interest is:", ci)
