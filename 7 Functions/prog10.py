# Write a function to find the average of numbers in a list.
def average(lst):
    if len(lst) == 0:
        return 0
    return sum(lst) / len(lst)

lst = list(map(int, input("Enter list elements: ").split()))
print("Average =", average(lst))