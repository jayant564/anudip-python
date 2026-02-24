# Problem 36
# Problem Statement: Print all divisors of a number.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

n = int(input("Enter a number: "))
print("Divisors of the number are:")
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
