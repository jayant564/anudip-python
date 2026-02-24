# Problem 14
# Problem Statement: Check whether a character is digit or alphabet.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

ch = input("Enter a character: ").strip()
if ch.isdigit():
    print("It is a Digit")
elif ch.isalpha():
    print("It is an Alphabet")
else:
    print("It is neither Digit nor Alphabet")
