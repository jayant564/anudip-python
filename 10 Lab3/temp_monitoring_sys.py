temps = [32, 45, 47, 38, 41, 50, 29, 44]

hottest = max(temps)
coldest = min(temps)

extreme_days = 0
for i in range(len(temps)):
    if temps[i] > 45:
        temps[i] = "Heat Alert"
    if isinstance(temps[i], int) and temps[i] > 40:
        extreme_days += 1

print("Hottest:", hottest)
print("Coldest:", coldest)
print("Updated temps:", temps)
print("Extreme days (>40):", extreme_days)