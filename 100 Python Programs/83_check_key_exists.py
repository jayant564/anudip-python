# Problem 83
# Problem Statement: Check whether key exists in dictionary.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

d = eval(input("Enter dictionary: "))
k = input("Enter key to check: ").strip()
print("Key exists:" , k in d)
