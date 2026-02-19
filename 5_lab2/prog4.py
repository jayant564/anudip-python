# Salary Increment System 
# An employee’s increment depends on: 
# • Performance rating (1–5) 
# • Years of experience 
# • Attendance percentage 
# Design logic to calculate increment percentage based on these factors. 
rating = int(input("Enter performance rating (1-5): "))
experience = int(input("Enter years of experience: "))
attendance = float(input("Enter attendance percentage: "))

increment = 5  # base increment

if rating >= 4:
    increment += 5

if experience >= 5:
    increment += 3

if attendance >= 90:
    increment += 2

print("Total increment percentage =", increment, "%")
