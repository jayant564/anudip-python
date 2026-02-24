# Problem 99
# Problem Statement: Generate all substrings of a string.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

s = input("Enter a string: ")
n = len(s)
print("All substrings are:")
for i in range(n):
    for j in range(i + 1, n + 1):
        print(s[i:j])
