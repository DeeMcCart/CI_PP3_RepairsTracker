# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import matplotlib
matplotlib.use('Agg')
import gspread 
from google.oauth2.service_account import Credentials
import time
from termcolor import colored
from tabulate import tabulate
# from wallpaper import set_wallpaper, get_wallpaper
import tk
import tkinter
#export DISPLAY=:0

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
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

def all_upper(my_set):
    """ 
    print(f"Function all_upper, value entered is {my_set}")
    returns uppercase set based on what is submitted
    """
    upper_set = []
    for ind in my_set:
        ind = [x.upper() for x in ind]
        upper_set.append(ind)
    my_set = upper_set
    return my_set

    
def find_cust(search_string):
    """ 
    This is a utility function which searches for matching customer record(s) 
    when passed a phone number or name 
    It returns the customer index within the spreadsheet, or 0 if not found
    """
    all_custs = SHEET.worksheet("sys_cust").get_all_values()
    # remove the title row
    all_custs.pop(0)
    # change all fields to uppercase
    upper_custs=[]
    upper_custs = all_upper(all_custs)
    print(f"upper_custs after uppercase conversion {upper_custs}")
    all_custs = all_upper(all_custs)
    print(f"all_custs after uppercase conversion {all_custs}")
    print(f"search string is {search_string}")

    for ind_cust in all_custs:
        cust_found = (set([search_string]) <= set(ind_cust))
        if(cust_found):
            print(f"customer found, details are {ind_cust} index is \n")
            return ind_cust
    print("Existing customer not found.....")
    return False

def update_worksheet(data, worksheet):
    """
    This function taken from love sandwiches
    Update any worksheet, add new row with the list data provided
    """
    print(f"Updating {worksheet} worksheet...\n")
    print(f"data to update: {data}")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully.\n")

def enter_repair(options):
    """ # this should include tracking (hmm what did I mean by this???)
    (Note - need to deal with situation where options is blank or null) 
    This function is designed to make input as quick as possible for the user
    Parameter 'options' is a string containing null or more characters, and it can be used for typeahead. 
    """
    print("\n\n\n\n------------------------------")
    print("---   ENTER REPAIR   ---------")
    print("------------------------------")
    # greeting = tkinter.Label(text="Hello, Tkinter")
    # window = tk.Tk()

    if options !="":
        print(f"\nEnter repair with options {options}\n" )
    search_string = input("Customer phone #: \n").upper()
    cust_index = find_cust(search_string)
    print(f"Returned value from find_cust: {cust_index}")
    if (cust_index):
        print("Valid customer returned")
        print(f"Customer name: {cust_index[1]}")
        repair_record = [15006, "R", cust_index[0], cust_index[1], "Add spangly diamonds", 1, "W", 25, 10, '01/07/23', '08/07/23', '01/01/1900', '20']
    else:
        print("No valid customer returned from find_cust")
        cust_name = input("Customer name: \n")
        repair_record = [15006, "R", search_string, cust_name, "Fix broken strap", 1, "W", 25, 10, '01/07/23', '08/07/23', '01/01/1900', '20']
    print(f"repair record is: {repair_record}")
    #update_worksheet([15004, "R", cust_index[0], cust_index[1], "Fix broken strap", 1, "W", 25, 10, '03/07/23', '10/07/23', '01/01/1900', 10], 'repairs')
    update_worksheet(repair_record, 'repairs')
    time.sleep(5)
    
def find_repair(options):
    """
    Allows search by repair or phone number or customer name - from here can 
    (U)pdate status ie estimate->order (in which case need to track deposit taken & assign completion date 7 days from today)
    (U)pdate status to in-progress->) 
    (Note - need to deal with situation where options is blank or null)
    """
    print("\n\n\n\n------------------------------")
    print("---    FIND REPAIR   ---------")
    print("------------------------------")
    print(f"\nFind repair with options {options}\n" )
    time.sleep(5)

def notify_customer(options):
    """ 
    this will:
    accept multiple repair numbers separated by commas
    allow status update from in-progress to complete
    update the spreadsheet row completed status and notified date
    activate a trigger to send a customer notification (email or text)
    (Note - need to deal with situation where options is blank or null)
    """
    print("\n\n\n\n------------------------------")
    print("--     NOTIFY CUSTOMER(s)   --")
    print("------------------------------")
    print(f"\nNotify customer(s) with options {options}\n" )
    time.sleep(5)

def maintain_sys(options):
    """ 
    this will:
    maintain users
    maintain other sys tables
    maintain customer list with last repair date
    In each case maintain means find, list, edit based on index number
    (Note - need to deal with situation where options is blank or null)
    """
    print("\n\n\n\n------------------------------")
    print("-- MAINTAIN REPAIRS SYSTEM  --")
    print("------------------------------")
    print(f"\nMaintain repairs tracking system with options {options}\n" )
    print("Adding value to sys_status sheet")
    sys_record=[]
    sys_record.append(["60", "Repair - Archived"])
    print(f"sys record is: {sys_record}")
    update_worksheet(sys_record, "sys_status")
    print(f"Updating sys_status worksheet...\n")
    worksheet_to_update = SHEET.worksheet("sys_status")
    worksheet_to_update.append_row(["60", "Repair - Archived"])
    print(f"{worksheet} worksheet updated successfully.\n")

    time.sleep(5)

def show_help(options):
    """
    this (clears the screen and) prints a set of help text
    (Note - need to deal with situation where options is blank or null)
    """
    print(f"\nShow help screen with options {options}\n" )
    print("\n\n\n\n---------------------------------")
    print("- REPAIRS TRACKER - HELP SCREEN -\n")
    print("1. Security")
    print("-----------")
    print("To use the system, you must have a userid and password ")
    print("This assigns access at user or super-user level")
    print("(For demo purposes u-u provides basic user level access")
    print("and s-s provides super-user access)")
    print("It is recommended that these userids are removed when moving from demo to live usage")
    print("OPTIONS (main menu) are below:")
    print("    (E)nter new estimate/repair") 
    print("    (F)ind existing estimate/repair")
    print("    (N)otify customers of repair completion")
    print("    (M)aintain system")
    print("    (H)elp")
    print("    e(X)it")  # if selected this will return a value of False
    print("(You can combine with submenu options ")
    print("e.g. EE to enter estimate, ER to enter repair)")
    print("")
    input("Press any key to return to main menu....\n")

def menu_manager():
    print("\n\n\n\n---------------------------------")
    print("- REPAIRS TRACKER - OPTIONS (main menu):")
    print("    (E)nter new estimate/repair") 
    print("    (F)ind existing estimate/repair")
    print("    (N)otify customers of repair completion")
    print("    (M)aintain system")
    print("    (H)elp")
    print("    e(X)it")  # if selected this will return a value of False
    print("(You can combine with submenu options ")
    print("e.g. EE to enter estimate, ER to enter repair)")
    
    input_string = input("Option:\n").upper()
    if input_string!="":
        user_option=input_string[0]
        if (user_option=="X"):
            return False
        
        if (input_string[1:] !=""):
            further_options = input_string[1:]
            print(f"Option selected is {user_option}, further input options {further_options}")
        else:
            further_options=""

        if(user_option=="E"):
            enter_repair(further_options)
        elif (user_option=="F"):
            find_repair(further_options)
        elif (user_option=="N"):
            notify_customer(further_options) 
        elif (user_option=="M"):
            maintain_sys(further_options)
        elif (user_option=="H"):
            show_help(further_options)
        else:
            print("Invalid option, try again!")
    else:
       print("Blank option, try again!")
         
    return True

def main():
    """
    Run all program functions
    """
    # set_wallpaper("../assets/images/jewellery_bench.jpg")
    print("Welcome to RepairTracker")
    user_name = input("Please enter username:\n")
    password = input("password:\n")
    # note that valid_user returns a value of 0(False) 1(user-level security) 2(super-user level security)
    valid_user = authenticate_user(user_name, password)
    while valid_user:
        valid_user=menu_manager()
    print("Exiting... Thank you for using RepairTracker...\n")

main()