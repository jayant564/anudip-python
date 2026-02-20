# Remove duplicate elements from a list.
lst = list(map(int, input("Enter numbers: ").split()))
new_list = []

for x in lst:
    if x not in new_list:
        new_list.append(x)

print("List without duplicates =", new_list)