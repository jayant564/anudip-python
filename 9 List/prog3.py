# Find the largest and smallest number in a list.
lst = list(map(int, input("Enter numbers: ").split()))

largest = lst[0]
smallest = lst[0]

for x in lst:
    if x > largest:
        largest = x
    if x < smallest:
        smallest = x

print("Largest =", largest)
print("Smallest =", smallest)