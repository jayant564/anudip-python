# Problem 20
# Problem Statement: Find the greatest of four numbers.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

nums = []
for i in range(4):
    nums.append(int(input(f"Enter number {i+1}: ")))

print("The greatest number is:", max(nums))
