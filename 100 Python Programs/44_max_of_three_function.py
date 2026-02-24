# Problem 44
# Problem Statement: Find maximum of three numbers using function.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

def max_of_three(a, b, c):
    return max(a, b, c)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("Maximum number is:", max_of_three(a, b, c))
