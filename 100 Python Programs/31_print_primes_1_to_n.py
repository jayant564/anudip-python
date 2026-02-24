# Problem 31
# Problem Statement: Print all prime numbers between 1 and N.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

n = int(input("Enter N: "))
print("Prime numbers between 1 and N:")
for i in range(2, n + 1):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        print(i, end=" ")
