# Problem 97
# Problem Statement: Count uppercase and lowercase letters.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

s = input("Enter a string: ")
upper = sum(1 for c in s if c.isupper())
lower = sum(1 for c in s if c.islower())
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
