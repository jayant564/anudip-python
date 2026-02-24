# Problem 54
# Problem Statement: Sort a list without using sort method.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

lst = list(map(int, input("Enter list elements separated by space: ").split()))
n = len(lst)
for i in range(n):
    for j in range(i + 1, n):
        if lst[j] < lst[i]:
            lst[i], lst[j] = lst[j], lst[i]
print("Sorted list is:", lst)
