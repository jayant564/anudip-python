# Insert an element at a specific position in a list.
lst = list(map(int, input("Enter numbers: ").split()))
pos = int(input("Enter position (index): "))
val = int(input("Enter value to insert: "))

lst.insert(pos, val)

print("Updated list =", lst)