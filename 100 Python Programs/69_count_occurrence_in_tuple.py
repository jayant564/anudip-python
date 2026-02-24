# Problem 69
# Problem Statement: Count occurrence of element in tuple.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

t = tuple(map(int, input("Enter tuple elements separated by space: ").split()))
x = int(input("Enter element to count: "))
print("Occurrence count is:", t.count(x))
