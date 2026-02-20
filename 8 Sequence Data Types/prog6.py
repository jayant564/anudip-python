# Reverse a list without using reverse().
lst = list(map(int, input("Enter numbers: ").split()))
rev = []

for i in range(len(lst) - 1, -1, -1):
    rev.append(lst[i])

print("Reversed list =", rev)