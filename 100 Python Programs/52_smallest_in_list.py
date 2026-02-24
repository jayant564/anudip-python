# Problem 52
# Problem Statement: Find smallest element in a list.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

lst = list(map(int, input("Enter list elements separated by space: ").split()))
print("Smallest element is:", min(lst))
