# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread 
from google.oauth2.service_account import Credentials
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("RepairsTracker")

def authenticate_user(user_name, password):
    """
    The autenticate_user function takes a user_name and password and compares it to the entries in the sys_users table.
    If username is located and corresponding password matches the password parameter then 
    return the level of user access (1=user, 2=super-user)
    else
    return 0 (false)
    """
    all_users = SHEET.worksheet("sys_users").get_all_values()
    # remove the title row
    all_users.pop(0)
    for ind_user in all_users:
        user_found = (set([user_name, password]) <= set(ind_user))
        if(user_found):
            print(f"Username & password verified, security level {ind_user[2]}\n")
            return ind_user[2]
    print("Invalid userid, please try again.....")
    return False

def enter_repair(options):
    """ # this should include tracking (hmm what did I mean by this???) 
    """
    print("\n\n\n\n------------------------------")
    print("---   ENTER REPAIR   ---------")
    print("------------------------------")
    print(f"\nEnter repair with options {options}\n" )
    
def find_repair(options):
    """
    Allows search by repair or phone number or customer name - from here can 
    (U)pdate status ie estimate->order (in which case need to track deposit taken & assign completion date 7 days from today)
    (U)pdate status to in-progress->) 
    """
    print("\n\n\n\n------------------------------")
    print("---    FIND REPAIR   ---------")
    print("------------------------------")
    print(f"\nFind repair with options {options}\n" )

def find_repair(options):
    print("\n\n\n\n------------------------------")
    print("---    FIND REPAIR   ---------")
    print("------------------------------")
    print(f"\nFind repair with options {options}\n" )

def notify_customer(options):
    """ 
    this will:
    accept multiple repair numbers separated by commas
    allow status update from in-progress to complete
    update the spreadsheet row completed status and notified date
    activate a trigger to send a customer notification (email or text)
    """
    print("\n\n\n\n------------------------------")
    print("--     NOTIFY CUSTOMER(s)   --")
    print("------------------------------")
    print(f"\nNotify customer(s) with options {options}\n" )

def maintain_sys(options):
    """ 
    this will:
    print customer list with last repair date
    """
    print("\n\n\n\n------------------------------")
    print("-- MAINTAIN REPAIRS SYSTEM  --")
    print("------------------------------")
    print(f"\nMaintain repairs tracking system with options {options}\n" )

def show_help(options):
    """
    this (clears the screen and) prints a set of help text
    """
    print("\n\n\n\n------------------------------")
    print("-- MAINTAIN REPAIRS SYSTEM  --")
    print("------------------------------")
    print(f"\nMaintain repairs tracking system with options {options}\n" )

def menu_manager():
    print("\n\n\n\n------------------------------")
    print("OPTIONS (main menu):")
    print("    (E)nter new estimate/repair") 
    print("    (F)ind existing estimate/repair")
    print("    (N)otify customers of repair completion")
    print("    (M)aintain system")
    print("    (H)elp")
    print("    e(X)it")  # if selected this will return a value of False
    print("(You can combine with submenu options ")
    print("e.g. EE to enter estimate, ER to enter repair)")
    
    input_string = input("Option:\n").upper()
    user_option=input_string[0]
    if (user_option=="X"):
        return False
    
    if (input_string[1:] !=""):
        further_options = input_string[1:]
        print(f"Option selected is {user_option}, further input options {further_options}")
    if(user_option=="E"):
        enter_repair(further_options)
    elif (user_option=="F"):
        find_repair(further_options)
    elif (user_option=="N"):
        notify_customer(further_options) 
    elif (user_option=="M"):
        maintain_sys(further_options)
    elif (user_option=="H"):
        show_help()
    else:
        print("Invalid option, try again!")
    return True

def main():
    """
    Run all program functions
    """
    print("Welcome to RepairTracker")
    print("(For demo purposes u-u provides basic user level access")
    print("and s-s provides super-user access)")
    user_name = input("Please enter username:\n")
    password = input("password:\n")
    # note that valid_user returns a value of 0(False) 1(user-level security) 2(super-user level security)
    valid_user = authenticate_user(user_name, password)
    while valid_user:
        valid_user=menu_manager()
    print("Exiting... Thank you for using RepairTracker...\n")

main()