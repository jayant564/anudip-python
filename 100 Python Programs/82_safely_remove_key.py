# Problem 82
# Problem Statement: Safely remove a key from dictionary.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

d = eval(input("Enter dictionary: "))
k = input("Enter key to remove: ").strip()
d.pop(k, None)
print("Updated dictionary is:", d)
