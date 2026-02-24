# Problem 43
# Problem Statement: Check palindrome string using function.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

def is_palindrome(s):
    return s == s[::-1]

s = input("Enter a string: ")
if is_palindrome(s):
    print("The string is Palindrome")
else:
    print("The string is Not Palindrome")
