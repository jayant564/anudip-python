# Problem 95
# Problem Statement: Remove duplicate characters from string.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

s = input("Enter a string: ")
result = ""
for c in s:
    if c not in result:
        result += c
print("String after removing duplicates is:", result)
