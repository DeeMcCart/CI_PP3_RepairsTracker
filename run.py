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
    If username is located and corresponding password matches the password parameter then return success (True)
    else
    return false
    """
    print("Accessing sys_users sheet....\n")
    all_users = SHEET.worksheet("sys_users").get_all_values()
    print(all_users)
    return True

def menu_manager():
    print("Input option string")
    print("OPTIONS at this level:")
    print("(E)nter new estimate/repair") 
    """ # this should include tracking (hmm what did I mean by this???) 
    """
    print("(F)ind existing estimate/repair")
    """
    Allows search by repair or phone number or customer name - from here can 
    (U)pdate status ie estimate->order (in which case need to track deposit taken & assign completion date 7 days from today)
    (U)pdate status to in-progress->) 
    """
    print("(N)otify customers of repair completion")
    """ 
    this will:
    accept multiple repair numbers separated by commas
    allow status update from in-progress to complete
    update the spreadsheet row completed status and notified date
    activate a trigger to send a customer notification (email or text)
    """
    print("(M)aintain system")
    """ 
    this will:
    print customer list with last repair date
    """
    print("e(X)it")
    """ 
    if selected this will return a value of False
    """
    input_string = input("option:\n")
    if (input_string.upper()=="X"):
        return False
    return True

def main():
    """
    Run all program functions
    """
    print("Welcome to RepairTracker")
    print("For demo purposes user-user will provide basic user level access")
    print("and super-super will provide super-user access\n\n")
    user_name = input("Please enter username:\n")
    password = input("password:\n")
#    valid_user = authenticate_user(user_name, password)
#    while valid_user:
#        valid_user=menu_manager
#    print("Exiting... Thank you for using RepairTracker...\n")

