# Problem 27
# Problem Statement: Generate Fibonacci series using while loop.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

n = int(input("Enter number of terms: "))
a, b = 0, 1
i = 0
print("Fibonacci series:")
while i < n:
    print(a, end=" ")
    a, b = b, a + b
    i += 1
