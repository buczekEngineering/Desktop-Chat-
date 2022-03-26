from tkinter import *

class User:
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

        users_db = open("users.txt", "a")
        users_db.write(f"{username_data}:{password_data}\n")
        users_db.close()

        self.username_input.delete(0, END)
        self.password_input.delete(0, END)
        Label(self.screen1, text="Hurray you are registerd", fg="magenta", font=("calibri", 11)).pack()

    def confirm(self, username, password):
        if username and password:
            self.process_register_data_with_db(username, password)
            screen_confirm = Toplevel(self.screen1)
            screen_confirm.title("Huray! You logged in!")
            Label(screen_confirm, text="You can enter the chat").pack()
            Label(screen_confirm, text="").pack()
        else:
            screen_confirm = Toplevel(self.screen1)
            screen_confirm.title("Huray! You logged in!")
            Label(screen_confirm, text="You can enter the chat").pack()
            Label(screen_confirm, text="").pack()


        Button(screen_confirm, text="Chat", width=10, height=1).pack()

    def register(self):
        screen1 = Toplevel(self.screen)
        screen1.title("Register")
        screen1.geometry("300x250")

        username = StringVar()
        password = StringVar()

        Label(screen1, text="Please enter your username and password below").pack()
        Label(screen1, text="").pack()
        Label(screen1, text="Username *").pack()

        self.username_input = Entry(screen1, textvariable=username)
        self.username_input.pack()
        Label(screen1, text="Password *").pack()

        self.password_input = Entry(screen1, textvariable=password)
        self.password_input.pack()
        Label(screen1, text="").pack()
        Button(screen1, text="Register", width=10, height=1, command= lambda: self.confirm(self.username_input, self.password_input)).pack()

    def main_screen(self):
        self.screen.geometry("300x250")
        self.screen.title("Pink Chat - Hello You")
        Label(text="Hello You -> Login to chat", bg="magenta", fg="white", width="300", height="2", font=("Calibri", 13)).pack()
        Label(text="").pack()
        Button(text="Login", height="2", width="30", command=self.login).pack()
        Label(text="").pack()
        Button(text="Create new account", height="2", width="30", command=self.register).pack()
        self.screen.mainloop()

user = User()
user.main_screen()
