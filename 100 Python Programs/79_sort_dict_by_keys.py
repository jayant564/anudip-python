# Problem 79
# Problem Statement: Sort dictionary by keys.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

d = eval(input("Enter dictionary: "))
sorted_dict = dict(sorted(d.items()))
print("Dictionary sorted by keys is:", sorted_dict)
