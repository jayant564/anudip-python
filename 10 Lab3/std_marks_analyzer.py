marks = [120, 85, 90, -5, 70, 85, 100, 30]

# Remove invalid
valid = [m for m in marks if 0 <= m <= 100]

avg = sum(valid) / len(valid) if valid else 0
topper = max(valid) if valid else None

# Grade based on average
if avg >= 90:
    grade = "A"
elif avg >= 75:
    grade = "B"
elif avg >= 60:
    grade = "C"
else:
    grade = "D"

print("Valid marks:", valid)
print("Average:", avg)
print("Topper:", topper)
print("Grade:", grade)