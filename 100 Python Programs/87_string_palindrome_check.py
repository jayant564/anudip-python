# Problem 87
# Problem Statement: Check whether string is palindrome.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

s = input("Enter a string: ")
if s == s[::-1]:
    print("The string is Palindrome")
else:
    print("The string is Not Palindrome")
