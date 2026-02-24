# Problem 57
# Problem Statement: Reverse a list without reverse method.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

lst = list(map(int, input("Enter list elements separated by space: ").split()))
i, j = 0, len(lst) - 1
while i < j:
    lst[i], lst[j] = lst[j], lst[i]
    i += 1
    j -= 1
print("Reversed list is:", lst)
