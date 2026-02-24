# Problem 25
# Problem Statement: Find sum of even numbers up to N.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

n = int(input("Enter N: "))
s = 0
i = 2
while i <= n:
    s += i
    i += 2
print("Sum of even numbers up to N is:", s)
