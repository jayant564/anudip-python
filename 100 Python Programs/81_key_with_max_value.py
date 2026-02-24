# Problem 81
# Problem Statement: Find key with maximum value.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

d = eval(input("Enter dictionary: "))
key = max(d, key=d.get)
print("Key with maximum value is:", key)
