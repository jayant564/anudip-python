# Problem 23
# Problem Statement: Reverse a number using while loop.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

n = int(input("Enter a number: "))
rev = 0
temp = n
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10
print("Reversed number is:", rev)
