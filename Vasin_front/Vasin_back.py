# login.py 

import re

def validate_username(username):
    if not username:
        print("Username cannot be empty.")
        return False
    if len(username) < 4:
        print("Username must be at least 4 characters long.")
        return False
    if not re.search(r"^[a-zA-Z0-9_]+$", username):
        print("Username can only contain letters, numbers, and underscores.")
        return False
    return True

def validate_password(password):
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        return False
    if not re.search(r"[A-Z]", password):
        print("Password must contain at least one uppercase letter.")
        return False
    if not re.search(r"[a-z]", password):
        print("Password must contain at least one lowercase letter.")
        return False
    return True

def login():
    while True:
        username = input("Enter your username: ")
        if not validate_username(username):
            print("Invalid username. Please try again.")
            continue
        break

    while True:
        password = input("Enter your password: ")
        if not validate_password(password):
            print("Invalid password. Please try again.")
            continue
        break

    with open("login.txt", "a") as f:
        f.write(f"{username} {password}\n")

    print("Login successful!")

if __name__ == "__main__":
    login()
