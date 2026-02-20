# Find the sum and average of elements in a list.
lst = list(map(int, input("Enter numbers: ").split()))

s = 0
for x in lst:
    s += x

avg = s / len(lst)

print("Sum =", s)
print("Average =", avg)