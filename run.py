import matplotlib
# matplotlib.use('Agg')
import gspread
import time
import os
import sys
import tk
from termcolor import colored
from tabulate import tabulate
from colorama import Fore, Back, Style
from google.oauth2.service_account import Credentials
# from wallpaper import set_wallpaper, get_wallpaper
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

# credentials for twilio SMS client authorisation
account_sid = 'AC83dacc66cbdf1b6f8a278daba6a47c06'
auth_token = os.environ.get("auth_token")
client = Client(account_sid, auth_token)

# credentials for linking to google drive/ google sheets
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("RepairsTracker")


def print_title(text_string) -> bool:
    """
    The print_title function displays text with consistent appearance 
    """
    print(colored(text_string, "white", "on_green",
                  attrs=['reverse', 'blink']))
    return True


def print_subtitle(text_string):
    """
    The print_subtitle function displays text with consistent appearance 
    """
    print(colored(text_string, "white", "on_red", attrs=['reverse', 'blink']))
    return True


def print_body(text_string):
    """
    The print_body function displays text with consistent appearance 
    """
    print(colored(text_string, 'blue', 'on_white'))
    return True


def print_status(text_string):
    """
    The print_text function displays text with consistent appearance 
    """
    print(colored(text_string, "white", "on_green"))
    return True


def print_message(text_string):
    """
    The print_message function displays text with consistent appearance 
    """
    print(colored(text_string, 'black', 'on_white'))
    return True


def print_error(text_string):
    """
    The print_error function displays text with consistent appearance 
    """
    print(colored(text_string, 'black', 'on_yellow'))
    return True


def authenticate_user(user_name, password):
    """
    The autenticate_user function takes a user_name and password and compares
    it to the entries in the sys_users table.  If username is located and
    corresponding password matches the password parameter then
    return the level of user access (1=user, 2=super-user)
    else
    return 0 (false)
    """
    all_users = SHEET.worksheet("sys_users").get_all_values()
    all_users.pop(0)
    for ind_user in all_users:
        user_found = (set([user_name, password]) <= set(ind_user))
        if (user_found):
            print_body(f"Username & password verified, "
                       + f"security level {ind_user[3]}")
            print_status("")
            print_status(f"Welcome back, {ind_user[1]}!")
            print_status("")
            time.sleep(1)
            return ind_user[3]
    print_error("Invalid userid, please try again.....")
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


def find_row(search_string, col):
    """
    Utility function to find a particlar value (usually a record ID)
    in a particular column(usually column 1)
    """
    cell = sh.find(search_string, col)
    row = cell.row
    return row


def find_cust(search_string):
    """
    This is a utility function which searches for matching customer record(s)
    when passed a phone number or name
    It returns the customer index within the spreadsheet, or 0 if not found
    """
    all_custs = SHEET.worksheet("sys_cust").get_all_values()
    all_custs.pop(0)
 #   upper_custs = []
 #   upper_custs = all_upper(all_custs)
    all_custs = all_upper(all_custs)
    for ind_cust in all_custs:
        cust_found = (set([search_string]) <= set(ind_cust))
        if (cust_found):
            return ind_cust
    return False


def next_index(worksheet):
    """
    This function calculates the next index number in column 0 of
    repairs spreadsheet
    it is calculated as last index + 1
    return this value
    """
    all_repairs = SHEET.worksheet(worksheet).get_all_values()
    next_index = int(all_repairs[-1][0]) + 1
    print_message(f"Calculated next index: {next_index}")
    return next_index


def list_worksheet(worksheet):
    """
    This is a utility function to print all data from a given worksheet.
    Note that certain tables have adjustments to column names to 
    avoid text wrapping as this does not display well using Tabulate
    """
    all_data = get_worksheet(worksheet)
    print_cols = []
    print_title = []
    if worksheet == "repairs":
        
        for title in all_data[0]:
            print_title.append(title.strip("rep_"))
        all_data[0]=print_title    
        print(f"first line of data is {all_data[0]}")
        for data in all_data:
            print_cols.append([data[0], data[2], data[3], data[10], data[12]])
        all_data = print_cols
    elif worksheet == "sys_cust":
        for data in all_data:
            print_cols.append([data[0], data[1], data[2]])
        all_data = print_cols
    elif worksheet == "sys_users":
        for data in all_data:
            print_cols.append([data[0], data[1], data[3]])
        all_data = print_cols
    table1 = tabulate(all_data, headers='firstrow', tablefmt='fancy_grid')
    print(table1)
    time.sleep(3)


def get_worksheet(worksheet):
    """
    This is a utility function to return all data from a given worksheet
    """
    worksheet_to_return = SHEET.worksheet(worksheet)
    all_data = worksheet_to_return.get_all_values()
    return all_data


def nice_list_worksheet(worksheet):
    """
    This is a utility function to return a concatenated string in 'nice' format
    showing all entries in a system list as '(col[0]) col[1]'
    """
    all_data = get_worksheet(worksheet)
    all_data.pop(0)
    stringy = ""
    for data in all_data:
        stringy = stringy + "("+data[0]+")"+data[1]+" "
    return stringy


def update_worksheet(data, worksheet):
    """
    This function taken from love sandwiches
    Update any worksheet, add new row with the list data provided
    """
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print_status(f"{worksheet} worksheet updated successfully")
    print("")


def enter_repair(options):
    """
    This option can be used to enter an estimate which typically includes
    slightly different input fields.
    The enter_repair function is designed to make input as quick for the user
    Parameter 'options' is a string containing null or more characters,
    and it can be used for typeahead.
    If an option is not pre-selected, the user is offered a menu
    """
    print_title("------------------------------")
    print_title("--- ENTER ESTIMATE/ REPAIR ---")
    print_title("------------------------------")
    if (options != ""):
        user_option = options[0]
        print_message(f"\nEnter estimate/repair option {options}")
        print("")
    else:
        print_subtitle("    (E)stimate   ")
        print_subtitle("    (R)epair     ")
        print_subtitle("    e(X)it       ")
        input_string = input("Option:\n").upper()
        if input_string != "":
            user_option = input_string[0]
        else:
            print_error("Blank option, try again!")

    if (user_option == "X"):
        return False
    elif (user_option == "E"):
        record_type = "E"
        record_status = '10'
        print_message("Enter estimate")
    elif (user_option == "R"):
        record_type = "R"
        record_status = '20'
        print_message("Enter repair")

    search_string = input("Customer phone #: \n").upper()
    cust_index = find_cust(search_string)
    if (cust_index):
        print_status(f"Found customer: {cust_index}")

    if (cust_index) and (input("Correct Customer? (N if not) ").upper() != 'N'):
        rep_phone = cust_index[0]
        rep_cname = cust_index[1]
    else:
        print_error("Existing customer not found")
        rep_phone = search_string
        rep_cname = input("Customer name: \n")
    item_types = nice_list_worksheet("sys_item")
    rep_item_type = input(f"Type: {item_types}").upper()
    mat_types = nice_list_worksheet("sys_mat")
    rep_material = input(f"Material: {mat_types}").upper()
    rep_details = input("Repair details: ")
    rep_estimate = input("Estimated cost (if known): ")
    rep_deposit = input("Deposit taken: ")
    repair_record = [next_index("repairs"), record_type, rep_phone, rep_cname,
                     rep_item_type, rep_material, rep_details,  25, 10,
                     '01/07/23', '08/07/23', '01/01/1900', record_status]
    print_message(f"repair record is: {repair_record}")
    update_worksheet(repair_record, 'repairs')
    print("")
    input("Press any key to return to main menu....\n")
    return True

def find_repair(options):
    """
    Allows search by repair or phone number or customer name - from here can
    (U)pdate status ie estimate->order (in which case need to track
    deposit taken & assign completion date 7 days from today)
    (U)pdate status to in-progress->)
    (Note - need to deal with situation where options is blank or null)
    """
    print("")
    print_title("------------------------------------")
    print_title("---       FIND REPAIR            ---")
    print_title("------------------------------------")
    if options != "":
        print_subtitle(f"Find repair with options {options}")
    list_worksheet("repairs")
    print("")
    input("Press ENTER key to return to main menu....\n")
    return True


def notify_customer(options):
    """
    this will:
    @repair_num:  accept none, one, or more repair number(s)
    allow status update from in-progress to complete
    update the spreadsheet row completed status and notified date
    activate a trigger to send a customer notification (email or text)
    (Note - need to deal with situation where options is blank or null)
    """
    print("")
    print_title("------------------------------")
    print_title("--     NOTIFY CUSTOMER(s)   --")
    print_title("------------------------------")
    if options != "":
        print_subtitle(f"\nNotify customer(s) with options {repair_num}\n")
    message_body = ("Hi Deirdre your repair from Goldmark jewellers is ready"
                    + " for collection, regards, Derek")
    to_number = "+353" + "0876203184"[1:]
    try:
        message = client.messages.create(from_='+14847423801',
                                         body=message_body,
                                         to=to_number)
    except Exception:
        error_details = sys.exc_info()
        print_error(f"Error occurred sending SMS message {message_body}"
                    + f" to number {to_number}")
        print_error(f"Error occurred, details: {error_details[1]} ")
    print("")
    input("Press ENTER key to return to main menu....\n")
    return True


def maintain_sys(options):
    """
    this will:
    list contents of sys tables (user can choose from a menu)
    """
    print_title("------------------------------")
    print_title("--    MAINTAIN/ UPDATE:     --")
    print_title("------------------------------")

    if (options != ""):
        user_option = options[0]
        print_body(f"Option passed is {user_option}")
    else:
        print_subtitle("    (C)ustomer list ")
        print_subtitle("    (I)tem type     ")
        print_subtitle("    (M)aterials     ")
        print_subtitle("    (S)tatus Codes  ")
        print_subtitle("    (U)sers         ")
        print_subtitle("    (H)elp          ")
        print_subtitle("    e(X)it          ")

        input_string = input("Option:\n").upper()
        if input_string != "":
            user_option = input_string[0]
        else:
            print_error("Blank option, try again!")

    if (user_option == "X"):
        return False
    elif (user_option == "C"):
        list_worksheet('sys_cust')
    elif (user_option == "I"):
        list_worksheet('sys_item')
    elif (user_option == "M"):
        list_worksheet('sys_mat')
    elif (user_option == "S"):
        list_worksheet('sys_status')
    elif (user_option == "U"):
        list_worksheet('sys_users')
    elif (user_option == "H"):
        show_help("M")
    else:
        print_error("Invalid option, try again!")
    print("")
    input("Press ENTER key to return to main menu....\n")
    return True


def show_help(options):
    """
    This function show_help() prints a set of help text.
    It explains the type-ahead capabilities and how they can be used once
    a person understands the sys navigation.
    When RepairsTracker moves from demo to PROD the references to userids
    will need to be removed.
    """
    print_title("---------------------------------")
    print_title("- REPAIRS TRACKER - HELP SCREEN -")
    print_title("---------------------------------")
    print_body("")
    print_subtitle("    SECURITY                     ")
    print_body("To use the system, you must have a userid and password      ")
    print_body("Access is provided at User or Administrator(superuser) level")
    print_body("")
    print_subtitle("     MAIN MENU OPTIONS:                                 ")
    print_body("Type-ahead is supported, if you know sub-menu opt, e.g. ")
    print_body("EE Enter Est, ER Enter Repair, F12345 find repair 12345)")
    print_subtitle("    (E)nter new estimate/repair:                        ")
    print_body("Estimates: typically more complex, e.g. insurance claims")
    print_body("jobs needing extra pricing, or needing ordered-in items.")
    print_body("Repairs track phone#, name, item details, pricing, dates")
    print_subtitle("    (F)ind existing estimate/repair:                    ")
    print_body("Use typeahead if repair# known, else lists all repairs  "),
    print_body("Enter specific repair number to see just that record.   ")
    print_subtitle("    (N)otify customers of repair completion:            ")
    print_body("This updates the repairs record to completed and generates  ")
    print_body("customised SMS for sending. Typeahead w/repair # e.g. N12345")
    print_subtitle("    (M)aintain system:                                  ")
    print_body("This option is only available to administrator-level users.")
    print_body("For this demo version, M lists content of system files     ")
    print_body("Typeahead to choose which file e.g. MC Maintain Customers  ")
    print_subtitle("    (H)elp:                                            ")
    print_body("This text currently showing on-screen is the help text     ")
    print("")
    input("Press any key to return to main menu....\n")


def menu_manager(valid_user):
    """
    The menu_manager() function displays the main menu options.
    This is designed to continue running until the user selects
    option X to exit
    """
    print_title("----------------------------------------")
    print_title("  REPAIRS TRACKER - MAIN MENU:          ")
    print_title("----------------------------------------")
    print_subtitle("    (E)nter new estimate/repair            ")
    print_subtitle("    (F)ind existing estimate/repair        ")
    print_subtitle("    (N)otify customers of repair completion")
    print_subtitle("    (M)aintain system                      ")
    print_subtitle("    (H)elp                                 ")
    print_subtitle("    e(X)it                                 ")
    print("")
    print_message("(You can combine with submenu options ")
    print_message("e.g. EE to enter estimate, ER to enter repair)")

    input_string = input("Option:\n").upper()
    if input_string != "":
        user_option = input_string[0]
        if (user_option == "X"):
            return False

        if (input_string[1:] != ""):
            further_options = input_string[1:]
            print_message(f"Option selected is {user_option},"
                          + f" further input options {further_options}")
        else:
            further_options = ""

        if (user_option == "E"):
            enter_repair(further_options)
        elif (user_option == "F"):
            find_repair(further_options)
        elif (user_option == "N"):
            notify_customer(further_options)
        elif (user_option == "M"):
            if (valid_user == '2'):
                maintain_sys(further_options)
            else:
                print_error("Insufficient security privileges")
                time.sleep(2)
        elif (user_option == "H"):
            show_help(further_options)
        else:
            print_error("Invalid option, try again!")
    else:
        print_error("Blank option, try again!")
    return valid_user


def main():
    """
    Function main() runs all program functions.
    It begins with a call to valid_user() to establish if a user is authorised 
    to access the system.
    valid_user() returns a value of:
    * 0(False) 
    * 1(user-level security)
    *  2(super-user level security)
    """
    print_title("          ---------------------------          ")
    print_title("          ----  REPAIRS TRACKER  ----          ")
    print_title("          ---------------------------          ")
    print("")
    print_subtitle("DEMO VERSION:")
    print_body("user u, password u provides user-level  access")
    print_body("user s, password s provides admin-level access")
    print("")
    user_name = input(colored("Please enter username: ", 'blue', 'on_white'))
    password = input(colored("Password: ", 'blue', 'on_white'))
    valid_user = authenticate_user(user_name, password)
    while valid_user:
        valid_user = menu_manager(valid_user)
    print("Exiting... Thank you for using RepairTracker...\n")


main()
