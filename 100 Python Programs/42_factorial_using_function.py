# Problem 42
# Problem Statement: Find factorial using function.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = int(input("Enter a number: "))
print("Factorial is:", factorial(n))
