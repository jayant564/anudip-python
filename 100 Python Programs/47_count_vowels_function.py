# Problem 47
# Problem Statement: Count vowels using function.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

def count_vowels(s):
    return sum(1 for c in s.lower() if c in "aeiou")

s = input("Enter a string: ")
print("Number of vowels is:", count_vowels(s))
