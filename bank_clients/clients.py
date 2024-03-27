clientInfo, clientIDs, clientUsernames, clientsUsernameIDs = [], [], [], {}


def processClientInfo(clientListValues):
    '''
        processClientInfo converts the list to a dictionary client info with respective values
        @clientListValues is a list of values read from csv file
        Return value: returns a dictionary 
    '''
    values = ["first name", "last name", "age", "transactional account", "savings account", "password"]
    myDict = {}
    
    for value in values:
        myDict[value] = clientListValues.pop(0)
    
    return myDict

    

def createDictsClientInfo(clientDict):
    '''
        createDictsClientInfo creates a dictionary of client info against id and another for client id against username
        @clientDict is a list of dictionaries of the client information
        Return value: dictionary of client information with their ids as key
    '''
    global clientIDs, clientUsernames, clientsUsernameIDs
    finalClientDict = {}
    idListCopy = clientIDs[:]

    for id in clientIDs:
        finalClientDict[id] = clientDict.pop(0)

    for username in clientUsernames:
        clientsUsernameIDs[username] = idListCopy.pop(0)

    return finalClientDict



def resetGlobals():
    ''' resetGlobals() resets the global variables used in this module'''
    global csvList, clientInfo, clientIDs, clientUsernames, clientsUsernameIDs 
    csvList, clientInfo, clientIDs, clientUsernames, clientsUsernameIDs = [], [], [], [], {}