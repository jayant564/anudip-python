# Problem 45
# Problem Statement: Find sum of digits using function.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

def sum_of_digits(n):
    return sum(int(d) for d in str(n))

n = int(input("Enter a number: "))
print("Sum of digits is:", sum_of_digits(n))
