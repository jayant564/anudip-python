# Find the sum of first n natural numbers using a loop.
n = int(input("Enter n: "))
sum = 0

for i in range(1, n + 1):
    sum += i

print("Sum =", sum)
