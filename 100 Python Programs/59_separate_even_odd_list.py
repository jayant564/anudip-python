# Problem 59
# Problem Statement: Separate even and odd numbers from list.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

lst = list(map(int, input("Enter list elements separated by space: ").split()))
even = [x for x in lst if x % 2 == 0]
odd = [x for x in lst if x % 2 != 0]
print("Even numbers:", even)
print("Odd numbers:", odd)
