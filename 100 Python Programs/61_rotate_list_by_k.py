# Problem 61
# Problem Statement: Rotate a list by K positions.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

lst = list(map(int, input("Enter list elements separated by space: ").split()))
k = int(input("Enter K: "))
if lst:
    k = k % len(lst)
    rotated = lst[k:] + lst[:k]
else:
    rotated = lst
print("Rotated list is:", rotated)
