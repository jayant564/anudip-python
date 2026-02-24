# Problem 63
# Problem Statement: Find average of list elements.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

lst = list(map(int, input("Enter list elements separated by space: ").split()))
if lst:
    avg = sum(lst) / len(lst)
else:
    avg = 0
print("Average of list elements is:", avg)
