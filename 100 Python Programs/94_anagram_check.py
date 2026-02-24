# Problem 94
# Problem Statement: Check whether two strings are anagrams.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

s1 = input("Enter first string: ").replace(" ", "").lower()
s2 = input("Enter second string: ").replace(" ", "").lower()

if sorted(s1) == sorted(s2):
    print("The strings are Anagrams")
else:
    print("The strings are Not Anagrams")
