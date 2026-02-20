# Write a function to check whether a number is even or odd.
def is_even(n):
    return n % 2 == 0

n = int(input("Enter a number: "))
if is_even(n):
    print("Even")
else:
    print("Odd")