'''
    this module consists of file handling functions
'''
import csv
clientInfo, id_list, userNames = [], [], []


def fileReadingStart():
    '''fileReadingStart calls helper functions involved in reading the files'''
    fileContent = csvReader("transactionals.csv") # file should come in 
    clientsDict = processCsvList(fileContent)

    return clientsDict


def processWordHolder(clientListValues):
    '''
        processWordHolder converts list to dictionary with keys as values in the list below
        @clientListValues is a list of values read from csv file
        Return value: returns a dictionary 
    '''
    values = ["first name", "last name", "age", "transactional account", "savings account", "password"]
    myDict = {}
    
    for value in values:
        myDict[value] = clientListValues.pop(0)
    
    return myDict


def csvReader(file):
    '''
        csvReader reads a csv file
        @file is the csv file to be read
        Return value: a list of the contents of the csv file passed
    '''
    csvList = []

    with open(file, "r") as f:
        csvValues = csv.reader(f)
        for word in csvValues:
            csvList.append(word)
            
    return csvList


def processCsvList(csvList):
    '''
        processCsvList converts CSV list into a dictionary
        @csvList
        Return value: dictionary of client info
    '''
    global userNames, id_list, clientInfo
    i = 1
    while(i < len(csvList)) :
            wordHolder = ";".join(csvList[i])
            print(wordHolder)
            wordHolder = wordHolder.split(";")
            print(wordHolder)
            userNames.append(wordHolder.pop(0)) # get the username
            id_list.append(wordHolder.pop(0)) # get the userID
            myDictValue = processWordHolder(wordHolder) # create a dictionary of the client info
            clientInfo.append(myDictValue)
            i += 1

    return clientInfo


def resetGlobals():
    ''' resetGlobals() resets the global variables used in this module'''

    csvList, clientInfo, id_list, userNames = [], [], [], []

fileReadingStart()

