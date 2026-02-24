# Problem 32
# Problem Statement: Find factorial using for loop.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

n = int(input("Enter a number: "))
result = 1
for i in range(1, n + 1):
    result *= i
print("Factorial is:", result)
