# Problem 30
# Problem Statement: Accept numbers until 0 is entered and print sum.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

total = 0
print("Enter numbers (0 to stop):")
while True:
    n = int(input())
    if n == 0:
        break
    total += n

print("Sum of entered numbers is:", total)
