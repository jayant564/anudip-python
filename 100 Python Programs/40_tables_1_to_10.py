# Problem 40
# Problem Statement: Print multiplication tables from 1 to 10.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

print("Multiplication tables from 1 to 10:")
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=" ")
    print()
