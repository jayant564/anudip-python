# Problem 64
# Problem Statement: Replace negative numbers with zero.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

lst = list(map(int, input("Enter list elements separated by space: ").split()))
result = [x if x >= 0 else 0 for x in lst]
print("Updated list is:", result)
