# Write a function to calculate the sum of elements in a list.
def sum_list(lst):
    s = 0
    for x in lst:
        s += x
    return s

lst = list(map(int, input("Enter list elements: ").split()))
print("Sum =", sum_list(lst))