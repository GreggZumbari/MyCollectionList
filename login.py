"""
    Greggory Hickman, January-February 2023
    login.py
"""

import time

# Logs in a user whose account info already exists in the accounts folder
def login():
    print("Please enter your username and password below.")
    # Check if the specified username and password match an existing account
    login_username = input("Username: ")
    login_password = input("Password: ")

    account_string = login_username + ", " + login_password

    # If there is an account with this username and password, login
    try:
        # Attempt to open a file with the imputted username to see if that file exists, and if that file contains the correct username and password
        file = open("./accounts/" + login_username + ".txt", "r")
        if (file.readline() == account_string):
            login_file = open("./current_user.txt", "w")
            login_file.write(login_username + ", " + login_password)
            
            print("You are now logged in! Welcome, " + login_username + "!")
        else:
            print("Wrong password. Please try again.")
        
        file.close()
    except:
        print("No account with that username exists. Please try again.")

# Logs out the user
def logout():
    file = open("current_user.txt", "r+")
    current_user = file.readline().split(", ")[0]
    file.truncate(0)
    print("User " + current_user + " has been logged out.")
    file.close()

# Returns true if there is already a user with the username "login_username"
def user_already_exists(login_username):
    try:
        # If we can open the file in read mode, then it must exist!
        file = open("./accounts/" + login_username + ".txt", "r")
        file.close()
        return True
    except:
        return False

# Have the user input their account info, then stick that info into a file for safekeeping
def register():
    print("Please enter the username and password below for your new account.")
    # Put the input into a file in ./accounts
    new_username = input("Username: ")
    new_password = input("Password: ")
    #confirm_password = input("Confirm Password: ")

    if (user_already_exists(new_username) == False):
        file = open("./accounts/" + new_username + ".txt", "w")
                
        file.write(new_username + ", " + new_password) # Write the rng to input.txt
        file.close()

        print("Account created successfully. You may now log in with this account.")
    else:
        print("An account with that username already exists. Please choose a different username.")

def mainloop():
    # Checks for data requests every second
    running = True
    while (running == True):
        time.sleep(1)
        # Check the contents of login_input.txt
        file = open("./login_input.txt", "r+")
        file_input = file.readline()
        if (file_input == "login"):
            login()
            file.truncate(0) # This line clears the contents of login_input.txt so that the program will only run login() once for each request
        elif (file_input == "logout"):
            logout()
            file.truncate(0)
        elif (file_input == "register"):
            register()
            file.truncate(0)
        elif (file_input == "exit"):
            running = False
            file.truncate(0)
        file.close()

mainloop()