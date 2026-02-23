attendance = [1,1,0,0,0,1,1,0,1,0]

percentage = (sum(attendance) / len(attendance)) * 100
print("Attendance %:", percentage)

if percentage < 75:
    print("Below 75% attendance")

# Replace consecutive absences with warning (-1)
i = 0
while i < len(attendance)-1:
    if attendance[i] == 0 and attendance[i+1] == 0:
        attendance[i] = attendance[i+1] = -1
    i += 1

print("Updated attendance:", attendance)