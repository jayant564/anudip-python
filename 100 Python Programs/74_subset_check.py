# Problem 74
# Problem Statement: Check whether one set is subset of another.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

a = set(map(int, input("Enter first set elements separated by space: ").split()))
b = set(map(int, input("Enter second set elements separated by space: ").split()))
print("Is first set a subset of second set?:", a.issubset(b))
