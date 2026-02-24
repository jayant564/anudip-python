# Problem 80
# Problem Statement: Sort dictionary by values.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

d = eval(input("Enter dictionary: "))
sorted_dict = dict(sorted(d.items(), key=lambda x: x[1]))
print("Dictionary sorted by values is:", sorted_dict)
