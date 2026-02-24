# Problem 78
# Problem Statement: Merge two dictionaries manually.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

d1 = eval(input("Enter first dictionary: "))
d2 = eval(input("Enter second dictionary: "))

merged = {}
for k, v in d1.items():
    merged[k] = v
for k, v in d2.items():
    merged[k] = v

print("Merged dictionary is:", merged)
