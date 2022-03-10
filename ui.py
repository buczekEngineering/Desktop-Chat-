import tkinter
from tkinter import *

class Login:
    def __init__(self):
        self.screen = Tk()
        self.screen1 = None
        self.username_input = None
        self.password_input = None

    def login(self):
        print("Login session started")

    def process_register_data_with_db(self, username, password):
        username_data = username.get()
        password_data = password.get()
        print(username)
        print(username_data)

        users_db = open("users.txt", "w")
        users_db.write(f"{username_data}:{password_data}\n")
        users_db.close()

        self.username_input.delete(0, END)
        self.password_input.delete(0, END)
        Label(self.screen1, text="Hurray you are registerd", fg="magenta", font=("calibri", 11)).pack()

    def confirm(self):
        screen_confirm = Toplevel(self.screen)
        screen_confirm.title("Huray! You logged in!")
        Label(screen_confirm, text="You can enter the chat").pack()
        Label(screen_confirm, text="").pack()
        Button(screen_confirm, text="Chat", width=10, height=1).pack()

    def register(self):
        # global screen1
        screen1 = Toplevel(self.screen)
        screen1.title("Register")
        screen1.geometry("300x250")

        username = StringVar()
        password = StringVar()

        Label(screen1, text="Please enter your username and password below").pack()
        Label(screen1, text="").pack()
        Label(screen1, text="Username *").pack()
        # global username_input
        self.username_input = Entry(screen1, textvariable=username)
        self.username_input.pack()
        Label(screen1, text="Password *").pack()
        # global password_input
        self.password_input = Entry(screen1, textvariable=password)
        self.password_input.pack()
        Label(screen1, text="").pack()
        Button(screen1, text="Register", width=10, height=1, command=self.confirm).pack()
        self.process_register_data_with_db(username, password)

    def main_screen(self):
        self.screen.geometry("300x250")
        self.screen.title("Notes v1.0")
        Label(text="Notes 1.0", bg="magenta", fg="white", width="300", height="2", font=("Calibri", 13)).pack()
        Label(text="").pack()
        Button(text="Login", height="2", width="30", command=self.login).pack()
        Label(text="").pack()
        Button(text="Register", height="2", width="30", command=self.register).pack()
        self.screen.mainloop()


ui = Login()
ui.main_screen()
