# Problem 22
# Problem Statement: Find factorial using while loop.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

n = int(input("Enter a number: "))
result = 1
i = 1
while i <= n:
    result *= i
    i += 1
print("Factorial is:", result)
