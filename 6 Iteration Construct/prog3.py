# Find the sum of first n natural numbers using a loop.
n = int(input("Enter n: "))
s = 0

for i in range(1, n + 1):
    s += i

print("Sum =", s)