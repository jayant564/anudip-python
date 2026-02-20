# Write a function to reverse a string.
def reverse_string(s):
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev

s = input("Enter a string: ")
print("Reversed string =", reverse_string(s))