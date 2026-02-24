# Problem 35
# Problem Statement: Count vowels in a string.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

s = input("Enter a string: ")
count = sum(1 for c in s.lower() if c in "aeiou")
print("Number of vowels is:", count)
