scores = [20, 35, 40, 55, 60, 30, 45, 25]

# Remove lowest 2
scores.sort()
scores = scores[2:]

# Add grace marks
for i in range(len(scores)):
    if 30 <= scores[i] <= 35:
        scores[i] += 5

# Count passed (>=40)
passed = sum(1 for s in scores if s >= 40)

print("Final scores:", scores)
print("Students passed:", passed)