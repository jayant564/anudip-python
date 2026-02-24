# Problem 84
# Problem Statement: Create dictionary from two lists.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

keys = input("Enter keys separated by space: ").split()
values = input("Enter values separated by space: ").split()
d = dict(zip(keys, values))
print("Created dictionary is:", d)
