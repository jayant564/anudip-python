# Problem 60
# Problem Statement: Find common elements between two lists.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

a = list(map(int, input("Enter first list elements separated by space: ").split()))
b = list(map(int, input("Enter second list elements separated by space: ").split()))
common = list(set(a) & set(b))
print("Common elements are:", common)
