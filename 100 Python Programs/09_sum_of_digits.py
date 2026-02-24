# Problem 9
# Problem Statement: Find the sum of digits of a number.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

s = input("Enter a number: ").strip()
total = sum(int(d) for d in s if d.isdigit())
print("Sum of digits is:", total)
