from prettytable import PrettyTable
from login.log import *
from authentication.files import *
from authentication.authenticate import *

isUserLoggedIn = False

def myBankStart():
    flag, loggedInUser = bankLogin()
    displayAccounts(loggedInUser)


def bankLogin():
    '''bankLogin logs the user into the banking system'''
    global isUserLoggedIn
    clients = fileReadingStart("bank_clients\\clients.csv")
    userName, userPassword = getLogins()
    clientID = userExists("zinksw023")
    if clientID == 'False':
        signUp = input("Would you like to sign up?")
        return '', ''
        # signUpFunction
    
    passwordCheck, loggedInUser = correctUserPassword("zee", clientID, clients)
    if passwordCheck == "False":
        return False, ''

    isUserLoggedIn = True
    return True, loggedInUser



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