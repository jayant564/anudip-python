# Problem 65
# Problem Statement: Check whether list is palindrome.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

lst = list(map(int, input("Enter list elements separated by space: ").split()))
if lst == lst[::-1]:
    print("The list is Palindrome")
else:
    print("The list is Not Palindrome")
