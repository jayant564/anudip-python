# Find the sum of all elements in a list.
lst = list(map(int, input("Enter numbers: ").split()))

s = 0
for x in lst:
    s += x

print("Sum =", s)