import os
import time
choice = input("Please choose one of the options:\n1- Shutdown the PC.\n2- Restart the PC.\n3- Sign out.\n4- Quit\n")
countdown = input("Please input the countdown time in minutes: ")


shutdown = "shutdown /s /t "
restart = "shutdown /r /t "
logout = "shutdown /l"

try:
    timeout = int(countdown) * 60
    if choice == "4":
        exit()
    elif choice == "1" and int(countdown):
        os.system(shutdown + str(timeout))
    elif choice == "2" and int(countdown):
        os.system(restart + str(timeout))
    elif choice == "3" and int(countdown):
        time.sleep(timeout)
        os.system(logout)
    else:
        print("Only numbers from 1-4")
except ValueError:
    print("Invalid input, only numbers are allowed.")
