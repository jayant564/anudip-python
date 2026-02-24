# Problem 16
# Problem Statement: Validate username and password.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

username = input("Enter username: ").strip()
password = input("Enter password: ").strip()

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Username or Password")
