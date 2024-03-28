import re

def validInput(input, flag=""):
    '''
        validInput checks for correct input given using match statement
        @input is the input to check
        @flag is a flag to display what kind of input is being validated ie name, age
        Return value: boolean; true if correct input given, otherwise false
    '''
        
    for inpt in input:
        if len(inpt) == 0:
            return False

        match(flag):
            case "name" | "surname": #| "age":
                if validNameFormat(inpt) is False:
                    return False
                break
            case "age":
                if inpt.isdigit() is False or len(inpt) <= 1:
                    return False
                break
            # case "password":
            #     pass
            case "username":
                if validUsernameFormat(inpt) is False:
                    return False
                break
            case _:
                pass

    return True


def validUsernameFormat(inpt):
    '''
        validUsernameFormat checks the parsed username for invalid format & returns a boolean
        @inpt is a string of the username parsed to the function
        Return value: boolean; True if username is in correct format, false if otherwise 
    '''

    if (len(inpt) == 9): 
        pattern = re.compile(r'(\w+)(\d)(\d)(\d)')
        matchObj = pattern.search(inpt)

        if matchObj is not None:
            return True

    return False


def validNameFormat(name):
    '''
        validNameFormat checks for correct format of names & surnames i.e correct length, no digits in input etc
        @name is the name to check i.e name or surname
        Return value: boolean; true of the names are invalid, false if otherwise
    '''
    if len(name) > 1 and name.isalpha():
        return True
    
    return False


def validPasswordFormat():
    pass