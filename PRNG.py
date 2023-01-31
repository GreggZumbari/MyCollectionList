    #   Greggory Hickman, January 2023
    #   PRNG.py
    
import os
import random
import time

def PRNG(input):
    end_program = False

    # Program starts here
    while (end_program == False):
        # Read data
        file = open("input.txt", "r")

        # If input.txt contains "run"
        if (file.readline() == "run"):
            # Generate a pseudo-random number between 0 and 20000 (hopefully there are less than 20000 images in the images folder)
            rng = random.randint(0, 20000)

            # Close and reopen the file in write mode so that we overwrite the contents of the file instead of appending
            file.close()
            file = open("input.txt", "w")
            
            print("RNG: " + str(rng))
            file.write(str(rng)) # Write the rng to input.txt
            file.close()
            # end_program = True # The while loop will end after this iteration
        
        time.sleep(1) # Sleep for 1 second so that this program doesn't obliterate the CPU
            
PRNG("input.txt")
