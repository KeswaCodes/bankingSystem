from file_handling.validate import *

def getLogins():
    '''getLogins returns username & password upon recieving input '''

    while True:
        username = input("Username: ").strip()
        psswd = input("Password: ").strip()
        if validInput([username, psswd]) is False:
            print("Password and/or username cannot be empty fields!")
            continue
        break

    return username, psswd

                