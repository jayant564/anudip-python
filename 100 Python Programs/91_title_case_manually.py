# Problem 91
# Problem Statement: Convert string to title case manually.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

s = input("Enter a string: ").strip()
words = s.split()
result = []
for w in words:
    if w:
        result.append(w[0].upper() + w[1:].lower())
print("Title case string is:", " ".join(result))
