# Create a new list containing only the even numbers from a given list.
lst = list(map(int, input("Enter numbers: ").split()))
even_list = []

for x in lst:
    if x % 2 == 0:
        even_list.append(x)

print("Even numbers list =", even_list)