'''
    this module consists of file reading & handling
'''
import csv
import sys
from bank_clients.clients import *

def fileReadingStart(file):
    '''
        fileReadingStart calls helper functions involved in reading the files
        @file is the csv file to be read
        Return value: a dictionary of all the clients at the bank
    '''
    # file should come in 
    fileContent = csvReader(file) 
    clientsDict = processCsvList(fileContent)
    clientsDict = createDictsClientInfo(clientsDict)

    return clientsDict


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
    global clientUsernames, clientIDs, clientInfo
    i = 1
    while(i < len(csvList)) :
            wordHolder = ";".join(csvList[i])
            wordHolder = wordHolder.split(";")
            # get the username
            clientUsernames.append(wordHolder.pop(0)) 
            # get the userID
            clientIDs.append(wordHolder.pop(0)) 
            # create a dictionary of the client info
            myDictValue = processClientInfo(wordHolder) 
            clientInfo.append(myDictValue)
            i += 1

    return clientInfo

