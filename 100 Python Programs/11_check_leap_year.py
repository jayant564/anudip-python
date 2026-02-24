# Problem 11
# Problem Statement: Check whether a given year is a leap year.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

year = int(input("Enter a year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("The year is a Leap Year")
else:
    print("The year is Not a Leap Year")
