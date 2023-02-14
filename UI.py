"""
    Greggory Hickman, January-February 2023
    Class Assignment for CS 361
"""

def tutorial():
    print("Tutorial function")

def help():
    print("\n- List of Commands -")
    print("+----------------+----------------------------------------+")
    print("| Command        | Description                            |")
    print("+----------------+----------------------------------------+")
    print("| help           | Alternatives: \"commands\" or \"?\".       |")
    print("|                | Displays the list of commands.         |")
    print("+----------------+----------------------------------------+")
    print("| login          | Alternatives: \"li\". Logs the user in   |")
    print("|                | using their username and password.     |")
    print("|                | If a different user is already logged  |")
    print("|                | in, then they are automatically logged |")
    print("|                | out.                                   |")
    print("+----------------+----------------------------------------+")
    print("| logout         | Alternatives: \"lo\". Logs the current   |")
    print("|                | user out, allowing a different user to |")
    print("|                | log in.                                |")
    print("+----------------+----------------------------------------+")
    print("| register       | Alternatives: \"r\". Creates a new       |")
    print("|                | account that can then be logged in to. |")
    print("|                | Asks for a username and password.      |")
    print("+----------------+----------------------------------------+")
    print("| quit           | Alternatives: \"exit\". Exits the        |")
    print("|                | program.                               |")
    print("+----------------+----------------------------------------+")

def commands():
    # Open the program
    print("Opening MyCollectionList...")
    # ASCII art, courtsey of https://onlineasciitools.com/convert-text-to-ascii-art
    print("  __  __        ____      _ _           _   _             _     _     _   ")
    print(" |  \/  |_   _ / ___|___ | | | ___  ___| |_(_) ___  _ __ | |   (_)___| |_ ")
    print(" | |\/| | | | | |   / _ \| | |/ _ \/ __| __| |/ _ \| '_ \| |   | / __| __|")
    print(" | |  | | |_| | |__| (_) | | |  __/ (__| |_| | (_) | | | | |___| \__ \ |_ ")
    print(" |_|  |_|\__, |\____\___/|_|_|\___|\___|\__|_|\___/|_| |_|_____|_|___/\__|")
    print("         |___/                                                            ")
    # Copyright
    print("© 2023 Greggory Hickman and Timothy Englehart")
    # Just a little space between the above text and the program that will appear below it
    print("\n")
    # Intro text
    print("Welcome to MyCollectionList! Please type \"help\" or \"?\" to recieve instructions on how to use this program!")
    print("To exit the program, type either \"exit\" or \"quit\".\n")

    # Start of the actual program
    running = True
    while (running == True):
        # Read the current_user file to find out which user is logged in. If file is empty, then no user is logged in.
        file = open("current_user.txt", "r")
        current_user = file.readline().split(", ")[0]
        file.close()
        command = input(current_user + "> ")
        match command:
            case "help":
                help()
            case "commands":
                help()
            case "?":
                help()
            case "login":
                file = open("login_input.txt", "w")
                file.write("login")
                file.close()
            case "li":
                file = open("login_input.txt", "w")
                file.write("login")
                file.close()
            case "logout":
                file = open("current_user.txt", "w")
                file.write("logout")
                file.close()
            case "lo":
                file = open("login_input.txt", "w")
                file.write("logout")
                file.close()
            case "register":
                file = open("login_input.txt", "w")
                file.write("register")
                file.close()
            case "r":
                file = open("login_input.txt", "w")
                file.write("register")
                file.close()
            case "exit":
                file = open("login_input.txt", "w")
                file.write("exit")
                file.close()
                running = False
                print("Exiting program...")
            case "quit":
                file = open("login_input.txt", "w")
                file.write("exit")
                file.close()
                running = False
                print("Exiting program...")
                
commands()