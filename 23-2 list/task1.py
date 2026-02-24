# Create list of 20 numbers
lst = []
print("Enter 20 numbers:")
for i in range(20):
    lst.append(int(input()))

print("Original list:", lst)

# Ask number to delete
num = int(input("Enter number to delete (except first occurrence): "))

# Flag to check if first occurrence is found
found_first = False

i = 0
while i < len(lst):
    if lst[i] == num:
        if not found_first:
            # Keep the first occurrence
            found_first = True
            i += 1
        else:
            # Delete other occurrences
            lst.pop(i)
            # Do NOT increment i here because list shifts left
    else:
        i += 1

print("Updated list:", lst)