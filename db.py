import sqlite3

connection = sqlite3.connect("users.db")

cursor = connection.cursor()

all_users = "SELECT * FROM users"

def user_exists(username):
    query = f"SELECT * FROM users WHERE username == {username}"
    pass

def check_password():
    pass

def add_new_user(username, password):
    if user_exists(username):
        return "user already exicts"
    else:
        pass


