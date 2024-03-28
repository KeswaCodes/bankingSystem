from prettytable import PrettyTable
from login.log import *
from authentication.files import *
from authentication.authenticate import *


def myBankStart():
    global userLoggedIn

    user = bankLogin()
    if userLoggedIn:
        displayAccounts(user)


def bankLogin():
    '''bankLogin logs the user into the banking system'''
    global userLoggedIn
    clients = fileReadingStart("bank_clients\\clients.csv")
    
    while True:
        userName, userPassword = getLogins()
        userID = userExists(userName)
        if userID == "Does not exist":
            # call sign up function
            return
        break
    
    user = passwordMatch(userPassword, userID, clients)
    userLoggedIn = True
    return user


def passwordMatch(userPassword, userID, clients):
    '''
    passwordMatch ensures user enters correct password to client account
    @userPassword is the password entered by user in terminal
    @userID is the client identification
    @clients is a dictionary of all the bank's clients 
    Return value: returns the logged in user
    '''
    while True:
        passwordCheck, user = correctUserPassword(userPassword, userID, clients)
        if passwordCheck == False:
            print("Invalid password entered")
            userPassword = input("Enter password: ") 
            continue
        break  

    return user 
    


def displayAccounts(client):
    '''
        displayAccounts displays the logged in user's bank accounts
        @client is the person whose bank account we are printing
    '''
    my_table = PrettyTable()
    my_table.field_names = ["Transactional account", "Savings account"]
    my_table.add_row([client.get('transactional account', None), client.get('savings account')])

    print(my_table)


if __name__ == "__main__":
    myBankStart()



# {'9012': {'first name': 'Rachel', 'last name': 'Booker', 'age': '28', 'transactional account': '5000.00', 'savings account': '2000.00', 'password': 'P@ssw0rd123'},
#  '2070': {'first name': 'Laura', 'last name': 'Grey', 'age': '35', 'transactional account': '7500.00', 'savings account': '3000.00', 'password': 'SecurePwd456'}
#  '4081': {'first name': 'Craig', 'last name': 'Johnson', 'age': '42', 'transactional account': '6000.00', 'savings account': '4000.00', 'password': 'Secret123!'}
#  '9346': {'first name': 'Mary', 'last name': 'Jenkins', 'age': '31', 'transactional account': '8200.00', 'savings account': '2500.00', 'password': 'Pa$$w0rd789'}, 
# '5079': {'first name': 'Jamie', 'last name': 'Smith', 'age': '29', 'transactional account': '4000.00', 'savings account': '3500.00', 'password': 'MyPwdIsStrong'}
#  '1006': {'first name': 'Zinhle', 'last name': 'Keswa', 'age': '20', 'transactional account': '400000.00', 'savings account': '3500000.00', 'password': 'zee'}}