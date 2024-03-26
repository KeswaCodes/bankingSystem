import csv
clientInfo, id_list, userNames = [], [], []
'''
    this module consists of file handling functions

    readFile reads a text file and returns the contents of the file
'''

def filesStart():
    fileContent = csvReader("username.csv")
    clientsDict = processCsvList(fileContent)
    print(clientsDict)




def processWordHolder(clientListValues):
    '''
        function convert list to dictionary with keys as values in the list below
        Return value: returns a dictionary 
    '''
    values = ["first name", "last name"]
    myDict = {}
    
    for value in values:
        myDict[value] = clientListValues.pop(0)
    
    return myDict



def csvReader(file):
    '''
        csvReader() is a function that reads a csv file
        Return value: a dictionary of the clients
    '''
    csvList = []

    with open(file, "r") as f:
        csvValues = csv.reader(f)
        for word in csvValues:
            print(word)
            csvList.append(word)
    print("CSV Values" , csvList , "\n\n\n")
    return csvList



def processCsvList(csvList):
    '''
        processCsvList() converts CSV list into a dictionary
        Return value: dictionary of client info
    '''
    global userNames, id_list, clientInfo
    i = 1
    while(i < len(csvList)) :
            wordHolder = "".join(csvList[i])
            wordHolder = wordHolder.split(";")
            userNames.append(wordHolder.pop(0)) # get the username
            id_list.append(wordHolder.pop(0)) # get the userID
            myDictValue = processWordHolder(wordHolder) # create a dictionary of the client info
            clientInfo.append(myDictValue)
            i += 1

    return clientInfo


def resetGlobals():
    ''' resetGlobals() resets the global variables used in this module'''

    csvList, clientInfo, id_list, userNames = [], [], [], []



filesStart()

