# Problem 58
# Problem Statement: Merge two lists and remove duplicates.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

a = list(map(int, input("Enter first list elements separated by space: ").split()))
b = list(map(int, input("Enter second list elements separated by space: ").split()))
merged = list(set(a + b))
print("Merged list without duplicates:", merged)
