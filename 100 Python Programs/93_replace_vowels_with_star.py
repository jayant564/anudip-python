# Problem 93
# Problem Statement: Replace all vowels with *.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

s = input("Enter a string: ")
result = ""
for c in s:
    if c.lower() in "aeiou":
        result += "*"
    else:
        result += c
print("Updated string is:", result)
