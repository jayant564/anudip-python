# Problem 26
# Problem Statement: Check whether a number is Armstrong.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

n = int(input("Enter a number: "))
temp = n
digits = len(str(n))
total = 0

while temp > 0:
    r = temp % 10
    total += r ** digits
    temp //= 10

if total == n:
    print("The number is an Armstrong number")
else:
    print("The number is not an Armstrong number")
