from bank_clients.clients import *
from file_handling.validate import *

def userExists(username):
    '''
        userExists checks if user exists in database, returns userID if true, string of false if otherwise
        @username is the username entered by the client to be validated/checked
        Return value: userID if user is found, false if otherwise
    '''
    global clientsMapping

    for clientUsername in clientsMapping:
        if clientUsername == username:
            return clientsMapping[clientUsername]

    print("User does not exist")
    return "Does not exist"


def correctUserPassword(userPassword, clientID, dictClients):
    '''
        correctUserPassword validates whether the password associated with ID is correct before logging user in
        @userPassword is the user's password to login
        @clientID is the client's ID to match
        @dictClients is a dictionary of all the clients at a bank
        Return value: boolean; True if the passwords match, False if otherwise
    '''


    client = dictClients.get(clientID)
    client_password = client.get("password")

    if client_password == userPassword:
        return True, client
    
    return False, ''
