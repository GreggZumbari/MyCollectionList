"""
    Greggory Hickman, January-February 2023
    Class Assignment for CS 361
"""

from tkinter import *
from register import register
from login import login

# This gets called every second without interrupting the rest of the program
def update_window():
    file = open("./current_user.txt", "r")
    current_user = file.readline().split(", ")[0]
    file.close()
    current_user_label.config(text = "Current User: " + current_user)
    window.after(1000, update_window)

# Create the window
window = Tk()

window.title("MyCollectionList")
window.geometry("600x450+10+20")

file = open("./current_user.txt", "r")
current_user = file.readline().split(", ")[0]
file.close()

# UI elements
current_user_label = Label(window, text = "Current User: " + current_user)
login_button = Button(window, text="Log in", fg="blue", command=login)
register_button = Button(window, text="Register", fg="red", command=register)

register_button.pack(side = "bottom")
login_button.pack(side = "bottom")
current_user_label.pack()

window.after(1000, update_window)
# Mainloop
window.mainloop()
