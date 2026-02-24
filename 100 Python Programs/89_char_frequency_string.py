# Problem 89
# Problem Statement: Find frequency of each character in string.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

s = input("Enter a string: ")
freq = {}
for c in s:
    freq[c] = freq.get(c, 0) + 1
print("Character frequencies are:", freq)
