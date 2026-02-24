# Problem 46
# Problem Statement: Generate Fibonacci series using function.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

n = int(input("Enter number of terms: "))
print("Fibonacci series:")
print(*fibonacci(n))
