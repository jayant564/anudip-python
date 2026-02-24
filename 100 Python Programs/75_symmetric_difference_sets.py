# Problem 75
# Problem Statement: Find symmetric difference of two sets.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

a = set(map(int, input("Enter first set elements separated by space: ").split()))
b = set(map(int, input("Enter second set elements separated by space: ").split()))
result = a ^ b
print("Symmetric difference of the two sets is:", result)
