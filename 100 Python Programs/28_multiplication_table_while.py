# Problem 28
# Problem Statement: Print multiplication table using while loop.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{n} x {i} = {n * i}")
    i += 1
