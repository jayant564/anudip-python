# Problem 37
# Problem Statement: Generate Fibonacci series using for loop.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

n = int(input("Enter number of terms: "))
a, b = 0, 1
print("Fibonacci series:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
