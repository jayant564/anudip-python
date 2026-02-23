salaries = [15000, 60000, 45000, 80000, 12000, 55000]

# Remove below minimum wage (assume 15000)
salaries = [s for s in salaries if s >= 15000]

# Add 5% bonus if > 50000
for i in range(len(salaries)):
    if salaries[i] > 50000:
        salaries[i] *= 1.05

# Sort descending
salaries.sort(reverse=True)

print("Processed salaries:", salaries)
print("Top 3 salaries:", salaries[:3])