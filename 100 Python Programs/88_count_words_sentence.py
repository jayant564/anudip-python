# Problem 88
# Problem Statement: Count number of words in a sentence.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

s = input("Enter a sentence: ").strip()
count = len(s.split())
print("Number of words is:", count)
