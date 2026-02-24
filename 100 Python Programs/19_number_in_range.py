# Problem 19
# Problem Statement: Check whether a number lies within a given range.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

n = int(input("Enter the number: "))
low = int(input("Enter lower bound: "))
high = int(input("Enter upper bound: "))

if low <= n <= high:
    print("The number lies within the range")
else:
    print("The number does not lie within the range")
