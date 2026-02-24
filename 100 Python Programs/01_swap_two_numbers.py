# Problem 1
# Problem Statement: Swap two numbers without using a third variable.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a, b = b, a
print("After swapping:")
print("First number:", a)
print("Second number:", b)
