# Problem 18
# Problem Statement: Calculate BMI category.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height * height)

if bmi < 18.5:
    print("BMI Category: Underweight")
elif bmi < 25:
    print("BMI Category: Normal")
elif bmi < 30:
    print("BMI Category: Overweight")
else:
    print("BMI Category: Obese")
