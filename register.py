"""
    Greggory Hickman, January-February 2023
    register.py
"""

from tkinter import *

# Returns true if there is already a user with the username "login_username"
def user_already_exists(login_username):
    try:
        file = open("./accounts/" + login_username, "r")
        file.close()
        return True
    except:
        return False

# Have the user input their account info, then stick that info into a file for safekeeping
def register():
    
    # Put the input into a file in ./accounts
    def submit():
        new_username = username_text.get("1.0", END)[:-1]
        new_password = password_text.get("1.0", END)[:-1]

        if (user_already_exists(new_username) == False):
            file = open("./accounts/" + new_username, "w")
                
            file.write(new_username + ", " + new_password) # Write the rng to input.txt
            file.close()

            information_label.config(text = "Account created successfully! You may now close out of this window and log in.")
        else:
            information_label.config(text = "An account with that username already exists. Please choose a different username.")

    #Create the window
    register_window = Tk()

    register_window.title("Register")
    register_window.geometry("600x450+10+20")

    username_label = Label(register_window, text = "Username:")
    username_text = Text(register_window, height = 5, width = 60)
    password_label = Label(register_window, text = "Password:")
    password_text = Text(register_window, height = 5, width = 60)
    submit_button = Button(register_window, text="Register", fg="red", command=submit)
    information_label = Label(register_window, text = "Please enter the username and password below for your new account!")

    
    submit_button.pack(side = "bottom")
    password_text.pack(side = "bottom")
    password_label.pack(side = "bottom")
    username_text.pack(side = "bottom")
    username_label.pack(side = "bottom")
    information_label.pack(side = "bottom")
