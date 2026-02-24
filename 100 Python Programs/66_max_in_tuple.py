# Problem 66
# Problem Statement: Find maximum value in a tuple.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

t = tuple(map(int, input("Enter tuple elements separated by space: ").split()))
print("Maximum value in tuple is:", max(t))
