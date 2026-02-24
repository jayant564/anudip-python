# Problem 13
# Problem Statement: Check whether a character is vowel or consonant.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

ch = input("Enter a character: ").strip().lower()
if ch and ch.isalpha() and ch in "aeiou":
    print("The character is a Vowel")
elif ch and ch.isalpha():
    print("The character is a Consonant")
else:
    print("Invalid input")
