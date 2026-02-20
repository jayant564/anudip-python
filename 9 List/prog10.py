# Delete an element from a list and display the updated list.
lst = list(map(int, input("Enter numbers: ").split()))
val = int(input("Enter value to delete: "))

if val in lst:
    lst.remove(val)
    print("Updated list =", lst)
else:
    print("Element not found in list")