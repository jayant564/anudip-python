# Problem 76
# Problem Statement: Create student marks dictionary and find topper.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

n = int(input("Enter number of students: "))
marks = {}
for _ in range(n):
    name = input("Enter student name: ").strip()
    score = int(input("Enter marks: "))
    marks[name] = score

topper = max(marks, key=marks.get)
print("Topper is:", topper)
