# Problem 70
# Problem Statement: Check whether tuple elements are unique.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

t = tuple(map(int, input("Enter tuple elements separated by space: ").split()))
if len(set(t)) == len(t):
    print("All elements in tuple are unique")
else:
    print("Tuple contains duplicate elements")
