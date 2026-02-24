# Problem 68
# Problem Statement: Convert tuple to list.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

t = tuple(map(int, input("Enter tuple elements separated by space: ").split()))
lst = list(t)
print("Converted list is:", lst)
