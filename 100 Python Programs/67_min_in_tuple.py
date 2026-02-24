# Problem 67
# Problem Statement: Find minimum value in a tuple.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

t = tuple(map(int, input("Enter tuple elements separated by space: ").split()))
print("Minimum value in tuple is:", min(t))
