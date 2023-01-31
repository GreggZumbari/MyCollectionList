"""
    Greggory Hickman, January 2023
    Assignment 2 for CS 361
    -
    This program is made up of this UI/controller program, and 2 microservice programs, Image.py and PRNG.py.

    UI.py: When the run button is clicked, input.txt is overwritten to contain only the word "run". Then, it waits until
    input.txt contains a path to an image, at which point that image is displayed.

    PRNG.py: Searches the first line of input.txt until it sees the word "run". When it does, it generates a 
    pseudo-random number and overwrites input.txt to contain only that random number.
     
    Image.py: Searches the first line of input.txt until it sees an integer number "i". Then, it chooses the i'th
    image from the "images" folder and overwrites input.txt to contain only the path to that image.
"""

from tkinter import *
from PIL import ImageTk,Image
import os
import time

def run_micros():
    # Put the word "run" in input.txt, prompting the microservices to do their work
    file = open("input.txt", "w")
    file.write("run")
    file.close()

def display_image():
    file = open("input.txt", "r")
    image_path = file.read()
    image = ImageTk.PhotoImage(Image.open(image_path))
    canvas.create_image(0, 0, anchor=NW, image=image)
    canvas.image = image

#Create the window
window = Tk()

window.title("Microservices Warmup")
window.geometry("600x450+10+20")

# UI elements
canvas = Canvas(window, width = 300, height = 300) 
canvas.pack(side = "top")
run_button = Button(window, text="Run", fg="red", command=run_micros)
run_button.pack(side = "bottom")
image_button = Button(window, text="Display Image", fg="blue", command=display_image)
image_button.pack(side = "bottom")

# Render image
#image = ImageTk.PhotoImage(Image.open("./images/Basketball.png"))
#canvas.create_image(30,30, anchor=NW, image=image)

# Mainloop
window.mainloop()