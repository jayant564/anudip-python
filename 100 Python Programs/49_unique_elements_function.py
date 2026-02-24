# Problem 49
# Problem Statement: Return unique elements from a list using function.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

def unique_elements(lst):
    result = []
    for x in lst:
        if x not in result:
            result.append(x)
    return result

lst = list(map(int, input("Enter list elements separated by space: ").split()))
print("Unique elements are:", unique_elements(lst))
