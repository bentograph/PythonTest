#Python Test Environment, simulates an employee onboarding program with managerial functions.
#Introduction to the program
print ("Launching Employee Onboarding Portal")
#TODO: Import processes beforehand. 
## Basic definitions for setup processes ##
def setupName() -> str and str: ## gets user information ## 
    find_username = True
    while find_username:
        userName = str(input ("Enter your name: "))
        print ("Your name is: ", userName, "Is that correct? (Y/N)")
        usernameApproval = str(input ("Enter: ")).upper().strip()
        if usernameApproval == "Y" or "yes" or "y":
            password = setupPassword(userName)
            return userName, password
        else:
            print ("Our apologies. Let's try that again.")

## sets password and transfers username and password to list ##
def setupPassword(userName : str) -> str: 
    while True:
        userPassword = str(input ("Please set a password: "))
        userpasswordConfirm = str(input ("Please confirm your password: "))
        if userPassword == userpasswordConfirm:
            print ("Your account has been created,", userName)
            listEmployee.append(userName) ## updates username list ##
            listPassword.append(userPassword) ##updates password list ## 
            initiateUser(userName, userPassword)
            print("User Added.")
            return userPassword
        else:
            print ("Sorry, the passwords you entered do not match. Please try again.")

## onboarding menu ##
            ## links to manager function menu ##
            ## shows and appends employees to list ##
def initiateUser(userName : str, userPassword : str) -> str and str:  
    print(*listEmployee, sep='\n')
    print ("[Onboarding Functions]\n\
            Select an option from the list below:\n\
            (0) Managerial Functions [RESTRICTED ACCESS] \n\
            (1) Close and Launch Workspace\n\
            (2) Add more employees\n\
            (3) List existing employees\n\
            (4) Exit this program")
    while True:
        optionSelect = int(input("Please enter your selection: "))
        if optionSelect == 1:
            print ("Launching Employee Workspace...")
            #Insert Function Here 
        elif optionSelect == 2:
            print ("Starting user management...")
            setupName()
        elif optionSelect == 3:
            print ("Listing current employees...")
            initiateUser(userName, userPassword)
        elif optionSelect == 4:
            print ("Shutting down...")
            exit()
        elif optionSelect == 0: 
            managerOverride(userName, userPassword)
        else:    ## default ##
            print ("Invalid number. Try again...")

## manager override function ##
            ## asks for manager authentication, max 3 attempts allowed ##
            ## shows all existing lists for basic diagnostic console functionality##
            ## shows and appends managers to list ##
            ## returns back to onboarding menu ##
            ## [note: default setting is an immediate logout after a change has been made for security]
def managerOverride(userName : str, userPassword : str) -> str and str: ##Manager Functions##
    managerApproval = True
    attemptCount = 3
    while managerApproval and attemptCount > 0:
        managerQuery = str(input ("Enter your manager name: "))
        managerPassword = str(input ("Enter your manager password: "))
        if any(managerQuery in s for s in listManager) and managerPassword == masterPassword:
            print ("[Manager Functions]\n\
            Select an option from the list below:\n\
            (1) Show diagnostic console\n\
            (2) Add a manager\n\
            (3) List existing managers\n\
            (4) Exit this program")
            while True:
                optionSelect = int(input("Please enter your selection: \n [For help press H]"))
                if optionSelect == 1:
                    print ("Showing diagnostic logs...")
                    print ("Master Database List- FOR DIAGNOSTIC USE ONLY")
                    print(*listEmployee, sep='\n')
                    print(*listPassword, sep='\n')
                    print(*listManager, sep='\n')
                    print("The master password is set as", masterPassword)
                elif optionSelect == 2:
                    print ("Adding new manager...")
                    newManager = str(input ("Enter manager name: "))
                    newmanagerConfirm = str(input ("Confirm manager name: "))
                    if newManager == newmanagerConfirm:
                        print ("Your account has been created,", userName)
                        listManager.append(newManager)
                        print("Manager Added.")
                        print("Logging out. Please reauthenticate...]")
                    managerOverride(userName, userPassword)
                elif optionSelect == 3:
                    print ("Listing current managers..")
                    print(*listManager, sep='\n')
                    print("Logging out. Please reauthenticate...]")
                    managerOverride(userName, userPassword)
                elif optionSelect == 4:
                    print ("Returning to Onboarding Menu..")
                    initiateUser(userName, userPassword)
                else:    ## default ##
                    print ("Invalid number. Try again...")
        else:
            print ("Manager name not in list. You have:", attemptCount, "attempts remaining.")
            attemptCount = (attemptCount - 1)
    print("You have exceeded the allowed number of attempts. Returning to onboarding menu...")
    initiateUser(userName, userPassword)

'''
from pyDes import *
import time

def encode(data,password):
    k = des(password, CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
    d = k.encrypt(data)
    return d

start=time.time()
for idx, val in enumerate(row):
    row[idx]=encode(str(val).encode(), 'password')

end=time.time()    
print(end-start)
'''

#Runtime actions to be executed
print ("Loading database lists...")
listEmployee = ['[Employees:]']
listPassword = ['[Password:]']
listManager = ['[Managers]','Administrator']
masterPassword = str("alpine")
print("Welcome, user. Let's get you started.")
userName, userPassword = setupName()
print ("Diagnostic Log: ")
print (userName)
print (userPassword)


