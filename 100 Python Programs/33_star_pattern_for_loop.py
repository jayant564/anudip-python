# Problem 33
# Problem Statement: Print star pattern using for loop.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    print("*" * i)
