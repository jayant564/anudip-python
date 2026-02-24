# Problem 86
# Problem Statement: Reverse a string without slicing.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

s = input("Enter a string: ")
rev = ""
for c in s:
    rev = c + rev
print("Reversed string is:", rev)
