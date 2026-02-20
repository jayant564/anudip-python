# Sort a list in ascending order (without using sort()).
lst = list(map(int, input("Enter numbers: ").split()))

n = len(lst)
for i in range(n):
    for j in range(i + 1, n):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

print("Sorted list =", lst)