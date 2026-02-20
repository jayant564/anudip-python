# Count how many times a given element appears in a list.
lst = list(map(int, input("Enter numbers: ").split()))
num = int(input("Enter element to count: "))

count = 0
for x in lst:
    if x == num:
        count += 1

print("Count =", count)