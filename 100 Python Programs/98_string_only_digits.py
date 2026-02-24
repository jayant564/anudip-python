# Problem 98
# Problem Statement: Check whether string contains only digits.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

s = input("Enter a string: ").strip()
if s.isdigit():
    print("The string contains only digits")
else:
    print("The string does not contain only digits")
