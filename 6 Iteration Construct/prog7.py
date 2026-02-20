# Count the number of digits in a given number using a loop.
n = int(input("Enter a number: "))
count = 0

if n == 0:
    count = 1
else:
    while n > 0:
        n = n // 10
        count += 1

print("Number of digits =", count)