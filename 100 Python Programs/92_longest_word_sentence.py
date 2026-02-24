# Problem 92
# Problem Statement: Find longest word in a sentence.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

words = input("Enter a sentence: ").split()
longest = max(words, key=len) if words else ""
print("Longest word is:", longest)
