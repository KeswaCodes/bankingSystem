clientInfo, clientIDs, clientUsernames, clientsMapping, userLoggedIn = [], [], [], {}, False


def processClientInfo(clientListValues):
    '''
        processClientInfo converts the list to a dictionary client info with respective values
        @clientListValues is a single clients information
        Return value: returns a dictionary of client demographics & bank accounts(not yet linked to their IDs)
    '''
    dictKeys = ["first name", "last name", "age", "transactional account", "savings account", "password"]
    myDict = {}
    
    for key in dictKeys:
        myDict[key] = clientListValues.pop(0)
    
    return myDict

    

def createDictsClientInfo(clientList):
    '''
        createDictsClientInfo creates a dictionary of client info against id and another for client id against username
        @clientList is a list of dictionaries of the client information
        Return value: dictionary of client information with their ids as key
    '''
    global clientIDs, clientUsernames, clientsMapping
    clientDataBase = {}
    idListCopy = clientIDs[:]

    for id in clientIDs:
        clientDataBase[id] = clientList.pop(0)

    for username in clientUsernames:
        clientsMapping[username] = idListCopy.pop(0)

    return clientDataBase



def resetGlobals():
    ''' resetGlobals() resets the global variables used in this module'''
    global csvList,  clientInfo, clientIDs, clientUsernames, clientsMapping, userLoggedIn
    csvList,  clientInfo, clientIDs, clientUsernames, clientsMapping = [], [], [], [], {}, False