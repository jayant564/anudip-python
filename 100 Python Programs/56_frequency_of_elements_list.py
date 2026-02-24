# Problem 56
# Problem Statement: Count frequency of elements in list.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

lst = list(map(int, input("Enter list elements separated by space: ").split()))
freq = {}
for x in lst:
    freq[x] = freq.get(x, 0) + 1
print("Frequency of elements:", freq)
