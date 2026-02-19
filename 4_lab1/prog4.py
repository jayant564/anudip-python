# University Admission Eligibility 
# A student applies for admission. Eligibility rules: 
# • Minimum 75% in 12th grade 
# • Must have studied Mathematics 
# • Entrance exam score ≥ 80 
# If any condition fails, show the exact reason. 
percentage = float(input("Enter 12th percentage: "))
maths = input("Did you study Mathematics? (yes/no): ").lower()
entrance = int(input("Enter entrance exam score: "))

if percentage < 75:
    print("Not eligible: Less than 75% in 12th")
elif maths != "yes":
    print("Not eligible: Mathematics not studied")
elif entrance < 80:
    print("Not eligible: Entrance score less than 80")
else:
    print("Eligible for admission")
