# Problem 8
# Problem Statement: Check whether a number is even or odd without modulus operator.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

n = int(input("Enter a number: "))
if (n & 1) == 0:
    print("The number is Even")
else:
    print("The number is Odd")
