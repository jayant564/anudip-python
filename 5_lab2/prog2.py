# Smart Login System 
# Create a login system with: 
# • Username validation 
# • Password validation 
# • Maximum 3 failed attempts 
# If 3 attempts fail, lock the account. 
correct_username = "admin"
correct_password = "1234"

attempts = 0

while attempts < 3:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login successful")
        break
    else:
        print("Invalid credentials")
        attempts += 1

if attempts == 3:
    print("Account locked due to 3 failed attempts")
