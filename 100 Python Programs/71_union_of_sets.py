# Problem 71
# Problem Statement: Perform union of two sets.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

a = set(map(int, input("Enter first set elements separated by space: ").split()))
b = set(map(int, input("Enter second set elements separated by space: ").split()))
result = a | b
print("Union of the two sets is:", result)
