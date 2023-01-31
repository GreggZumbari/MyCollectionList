    #   Greggory Hickman, January 2023
    #   Image.py
    
from curses.ascii import isdigit
import os
import random
import time

def PRNG(input):
    end_program = False

    # Loop the program until end_program is set to True
    while (end_program == False):
        # Read data
        file = open("input.txt", "r")
        file_contents = file.readline()

        # If input.txt contains an integer
        if (file_contents.isdigit()):
            # Pull the number from input.txt
            rng = int(file_contents)

            for images in os.walk("./images"):
                image_count = len(images[2])
                rng = (rng % image_count)

            # Close and reopen the file in write mode so that we overwrite the contents of the file instead of appending
            file.close()
            file = open("input.txt", "w")
            file.write("./images/" + images[2][rng]) # Write the path to the rng'th image to input.txt
            # end_program = True # The while loop will end after this iteration
        
        time.sleep(1) # Sleep for 1 second
            
PRNG("input.txt")