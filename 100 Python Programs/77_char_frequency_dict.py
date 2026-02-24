# Problem 77
# Problem Statement: Count character frequency using dictionary.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

s = input("Enter a string: ")
freq = {}
for c in s:
    freq[c] = freq.get(c, 0) + 1
print("Character frequency is:", freq)
