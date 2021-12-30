import os

choice = input("Please choose one of the options:\n1- Shutdown the PC.\n2- Restart the PC.\n3- Sign out.\n4- Quit\n")
countdown = "Please input the countdown time in seconds: "

shutdown = "shutdown /s /t "
restart = "shutdown /r /t "
logout = "shutdown /l /t "

try:
    if choice == "4":
        exit()
    elif choice == "1" and int(input(countdown)) is True:
        os.system(shutdown + countdown)
    elif choice == "2" and int(input(countdown)) is True:
        os.system(restart + countdown)
    elif choice == "3" and int(input(countdown)) is True:
        os.system(logout + countdown)
    else:
        print("Only numbers from 1-4")
except ValueError:
    print("Invalid input, only numbers are allowed.")
