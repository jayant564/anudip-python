# Problem 100
# Problem Statement: Compress a string using character counts.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

s = input("Enter a string: ")
result = ""
i = 0
while i < len(s):
    j = i
    while j < len(s) and s[j] == s[i]:
        j += 1
    result += s[i] + str(j - i)
    i = j
print("Compressed string is:", result)
