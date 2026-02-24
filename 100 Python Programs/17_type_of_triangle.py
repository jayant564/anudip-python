# Problem 17
# Problem Statement: Determine the type of triangle.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))

if a == b == c:
    print("The triangle is Equilateral")
elif a == b or b == c or a == c:
    print("The triangle is Isosceles")
else:
    print("The triangle is Scalene")
