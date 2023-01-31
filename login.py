"""
    Greggory Hickman, January-February 2023
    login.py
"""

from tkinter import *

def login():
    # Check if the specified username and password match an existing account
    def submit():
        login_username = username_text.get("1.0", END)[:-1]
        login_password = password_text.get("1.0", END)[:-1]

        account_string = login_username + ", " + login_password

        # If there is an account with this username and password, login
        try:
            file = open("./accounts/" + login_username, "r")
            if (file.readline() == account_string):
                login_file = open("./current_user.txt", "w")
                login_file.write(login_username + ", " + login_password)
                information_label.config(text = "You are now logged in! You may now close out of this window.")
            else:
                information_label.config(text = "Wrong password. Please try again.")
            
            file.close()
        except:
            information_label.config(text = "No account with that username exists. Please try again.")

    #Create the window
    login_window = Tk()

    login_window.title("Login")
    login_window.geometry("600x450+10+20")

    username_label = Label(login_window, text = "Username:")
    username_text = Text(login_window, height = 5, width = 60)
    password_label = Label(login_window, text = "Password:")
    password_text = Text(login_window, height = 5, width = 60)
    submit_button = Button(login_window, text="Login", fg="red", command=submit)
    information_label = Label(login_window, text = "Please enter your username and password below.")
    
    submit_button.pack(side = "bottom")
    password_text.pack(side = "bottom")
    password_label.pack(side = "bottom")
    username_text.pack(side = "bottom")
    username_label.pack(side = "bottom")
    information_label.pack(side = "bottom")