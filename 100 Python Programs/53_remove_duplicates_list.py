# Problem 53
# Problem Statement: Remove duplicate elements from list.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

lst = list(map(int, input("Enter list elements separated by space: ").split()))
result = []
for x in lst:
    if x not in result:
        result.append(x)
print("List after removing duplicates:", result)
