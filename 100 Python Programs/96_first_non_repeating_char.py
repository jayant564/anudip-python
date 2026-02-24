# Problem 96
# Problem Statement: Find first non-repeating character in string.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

s = input("Enter a string: ")
freq = {}
for c in s:
    freq[c] = freq.get(c, 0) + 1

found = False
for c in s:
    if freq[c] == 1:
        print("First non-repeating character is:", c)
        found = True
        break

if not found:
    print("No non-repeating character found")
