# Problem 55
# Problem Statement: Find second largest number in list.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

lst = list(map(int, input("Enter list elements separated by space: ").split()))
unique = sorted(set(lst))
if len(unique) >= 2:
    print("Second largest element is:", unique[-2])
else:
    print("List does not have a second largest element")
