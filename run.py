# import matplotlib
# matplotlib.use('Agg')
import gspread
import time
from datetime import datetime, timedelta
import os
import sys
# import tk
# from termcolor import colored
from tabulate import tabulate
from colorama import Fore, Back, Style
from google.oauth2.service_account import Credentials
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
    for ind_cust in all_custs:
        cust_found = (set([search_string]) <= set(ind_cust))
        if (cust_found):
            return ind_cust
    return False


def find_repair_index(search_repair):
    """
    This is a utility function to located the row # of a given repair
    when passed a repair number
    """
    repair_nums = SHEET.worksheet("repairs").col_values(1)
    try:
        rownum = repair_nums.index(search_repair)
    except ValueError:
        print_error(f"Repair {search_repair} not found")
        return 0
    except IndexError:
        print_error(f"Repair {search_repair} not found")
        return 0
    return rownum


def next_index(worksheet):
    """
    This function calculates the next index number in column 0 of
    repairs spreadsheet
    it is calculated as last index + 1
    return this value
    """
    all_repairs = SHEET.worksheet(worksheet).get_all_values()
    next_index = int(all_repairs[-1][0]) + 1
    return next_index


def return_record(worksheet, row_num):
    """
    This is a utility function to return row data from a given worksheet.
    """
    record_data = []
    if (row_num > 0):
        record_data = get_worksheet(worksheet)[row_num]
    else:
        print_error(f"Invalid {worksheet} row # {row_num}")
    return record_data


def list_worksheet(worksheet, row_num):
    """
    This is a utility function to print all data from a given worksheet.
    Note that certain tables have adjustments to column names to
    avoid text wrapping as this does not display well using Tabulate
    If @row = 0 then list all rows,
    else list heading plus specific row only
    """
    if (row_num > 0):
        all_data = [get_worksheet(worksheet)[0],
                    get_worksheet(worksheet)[row_num]]
    else:
        all_data = get_worksheet(worksheet)
    print_cols = []
    if worksheet == "repairs":
        all_data[0] = ["id", "T", "Ph", "Name", "I", "M", "Dets", "est",
                       "paid", "in", "due", "date_coll", "st"]
        for data in all_data:
            print_cols.append([data[0], data[2][0:10], data[3][0:18],
                              data[6][0:20], data[10][0:5], data[12]])
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
    return True


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


def get_codes_worksheet(worksheet):
    """
    This is a utility function to return a list of values
    from the first column of a given worksheet
    """
    all_data = get_worksheet(worksheet)
    all_data.pop(0)
    stringy = ""
    for data in all_data:
        stringy = stringy + data[0]
    return stringy


def append_worksheet(worksheet, data):
    """
    Update any worksheet, add new row with the data provided
    """
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print_status(f"New {worksheet} record {data[1]} {data[0]} for"
                 + f" {data[3]} added")
    print("")
    return True


def get_valid_phone():
    """
    utility function to capture a valid phone number
    """
    valid_phone = False
    while not valid_phone:
        phone_num = input(colored("Customer phone #: ",
                          'black', 'on_white')).upper()
        if phone_num.isnumeric():
            valid_item = True
            return phone_num
        else:
            print_error("Phone must be all numbers, no spaces, try again")
    return []


def get_valid_cname(cust_phone):
    """
    utility function to retrieve customer name if phone number
    exists in sys_cust table, otherwise to allow entry
    of customer name
    """
    cust_index = find_cust(cust_phone)
    if (cust_index):
        print_status(f"Found customer: {cust_index}")
    if (cust_index) and (input(colored("Correct Customer? (N if not) ",
                         'black', 'on_white')).upper() != 'N'):
        cust_name = cust_index[1]
    else:
        print_error("Existing customer not found")
        cust_name = input(colored("Customer name: ", 'black', 'on_white'))
    return cust_name


def get_valid_item():
    """
    Utility function to capture a valid item type
    as per the types codes stored in the sys_items table
    """
    item_types = nice_list_worksheet("sys_item")
    item_codes = get_codes_worksheet("sys_item")
    valid_item = False
    while not valid_item:
        rep_item_type = input(colored(f"Type: {item_types}",
                              'black', 'on_white')).upper()
        if (rep_item_type) and (rep_item_type in item_codes):
            valid_item = True
            return rep_item_type
        else:
            print_error("Invalid item type, try again")
    return []


def get_valid_material():
    """
    Utility function to capture a valid material type
    as per the material codes stored in the sys_mat table
    """
    mat_types = nice_list_worksheet("sys_mat")
    mat_codes = get_codes_worksheet("sys_mat")
    valid_mat = False
    while not valid_mat:
        rep_material = input(colored(f"Material: {mat_types}",
                             'black', 'on_white')).upper()
        if (rep_material) and (rep_material in mat_codes):
            valid_mat = True
            return rep_material
        else:
            print_error("Invalid metal, try again")
    return []


def get_valid_amount(prompt_text):
    """
    Utility function to input a valid amount (0-99999)
    """
    valid_num = False
    while not valid_num:
        entered_amt = input(colored(prompt_text,
                            'black', 'on_white'))
        if (entered_amt.isnumeric()) and (int(entered_amt) > 0
                                          and int(entered_amt) < 99999):
            valid_num = True
            return entered_amt
        else:
            print_error("Amount must be between 0 and 99999")
    return entered_amt


def enter_repair(options):
    """
    This option can be used to enter an estimate (status 10) or repair (20).
    The enter_repair function is designed to make input as quick for the user
    Parameter 'options' is a string containing null or more characters,
    and it can be used for typeahead.
    If an option is not pre-selected, the user is offered a menu
    """
    print("")
    print_title("------------------------------")
    print_title("--  ENTER ESTIMATE/ REPAIR  --")
    print_title("------------------------------")
    if (options != ""):
        user_option = options[0]
        print_subtitle(f"Enter estimate/repair option {options}")
    else:
        print_subtitle("    (E)stimate                ")
        print_subtitle("    (R)epair                  ")
        print_subtitle("    e(X)it                    ")
        print("")
        input_string = input(colored("Option: ", 'black', 'on_white')).upper()
        if input_string != "":
            user_option = input_string[0]
        else:
            print_error("Blank option, try again")

    if (user_option == "X"):
        return False
    elif (user_option == "E"):
        print("")
        print_subtitle("------------------------------")
        print_subtitle("---      New Estimate      ---")
        print_subtitle("------------------------------")
        print("")
        record_type = "E"
        record_status = '10'
    elif (user_option == "R"):
        print("")
        print_subtitle("------------------------------")
        print_subtitle("---       New Repair       ---")
        print_subtitle("------------------------------")
        print("")
        record_type = "R"
        record_status = '20'
    else:
        print_error("Invalid option")
        print("")
        input(colored("Press ENTER key to return to main menu....",
              'black', 'on_white'))
        return False

    rep_phone = get_valid_phone()
    rep_cname = get_valid_cname(rep_phone)
    rep_item_type = get_valid_item()
    rep_material = get_valid_material()
    rep_details = input(colored("Repair details: ", 'black', 'on_white'))
    rep_estimate = get_valid_amount("Estimated cost (if known): ")
    rep_deposit = get_valid_amount("Deposit taken: ")
    rep_date_in = datetime.now().strftime("%d/%m/%Y")
    rep_date_due = (datetime.now() + timedelta(days=7)).strftime("%d/%m/%Y")
    repair_record = [next_index("repairs"), record_type, rep_phone, rep_cname,
                     rep_item_type, rep_material, rep_details, rep_estimate,
                     rep_deposit, rep_date_in, rep_date_due, '01/01/1900',
                     record_status]
    append_worksheet("repairs", repair_record)
    print("")
    input(colored("Press any key to return to main menu....",
                  'black', 'on_white'))
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
    print("")
    if options != "":
        print_subtitle(f"Find repair {options}")
    else:
        options = input(colored("Repair #: ", 'black', 'on_white'))
    row_num = find_repair_index(options)
    if (row_num == 0):
        disp_all = input(colored("List all repairs? (N for no) ",
                                 'black', 'on_white')).upper()
        if (disp_all == 'N'):
            return False
    list_worksheet("repairs", row_num)
    print("")
    input(colored("Press ENTER key to return to main menu....",
                  'black', 'on_white'))
    return True


def notify_customer(options):
    """
    @options:  Option to provide a repair number
    allow status update from in-progress (20) to customer notified(50)
    update the spreadsheet row completed status and notified date
    activate a trigger to send a customer notification (email or text)
    """
    print("")
    print_title("------------------------------")
    print_title("--     NOTIFY CUSTOMER(s)   --")
    print_title("------------------------------")
    print("")
    if options != "":
        print_subtitle(f"Notify customer of repair {options}")
    else:
        options = input(colored("Repair #: ", 'black', 'on_white'))
    row_num = find_repair_index(options)
    if (row_num > 0):
        record_data = return_record("repairs", row_num)
    else:
        print("")
        input(colored("Press ENTER key to return to main menu....",
              'black', 'on_white'))
        return False
    message_body = (f"Hi {record_data[3]} your repair from Goldmark jewellers"
                    " is ready for collection, regards, Derek")
    to_number = "+353" + "0876203184"[1:]
    try:
        message = client.messages.create(from_='+14847423801',
                                         body=message_body,
                                         to=to_number)
        print(f"SMS sent to customer on phone # {record_data[2]},"
              + " message content {message_body}")
        repairs_sheet = SHEET.worksheet("repairs")
        repairs_sheet.update_cell((row_num + 1), 13, "'50")
        print_status(f"Repair {options} status updated to 50:"
                     + " Customer Notified")
    except Exception:
        error_details = sys.exc_info()
        print_error(f"Error occurred sending SMS message: {message_body}"
                    + f" to number {record_data[2]}")
        print(f"Details: {error_details[1]} ")
        repairs_sheet = SHEET.worksheet("repairs")
        repairs_sheet.update_cell((row_num + 1), 13, "'40")
        print_status(f"Repair {options} status updated to 40: Completed")
    print("")
    input(colored("Press ENTER key to return to main menu....",
                  'black', 'on_white'))
    return True


def maintain_sys(options):
    """
    this will:
    list contents of sys tables (user can choose from a menu)
    """
    print_title("------------------------------")
    print_title("--      MAINTAIN/ LIST:     --")
    print_title("------------------------------")

    if (options != ""):
        user_option = options[0]
        print_body(f"Option passed is {user_option}")
    else:
        print_subtitle("    (C)ustomer list           ")
        print_subtitle("    (I)tem type               ")
        print_subtitle("    (M)aterials               ")
        print_subtitle("    (S)tatus Codes            ")
        print_subtitle("    (U)sers                   ")
        print_subtitle("    (H)elp                    ")
        print_subtitle("    e(X)it                    ")

        input_string = input(colored("Option:", 'black', 'on_white')).upper()
        if input_string != "":
            user_option = input_string[0]
        else:
            print_error("Blank option, try again")

    if (user_option == "X"):
        return False
    elif (user_option == "C"):
        list_worksheet('sys_cust', 0)
    elif (user_option == "I"):
        list_worksheet('sys_item', 0)
    elif (user_option == "M"):
        list_worksheet('sys_mat', 0)
    elif (user_option == "S"):
        list_worksheet('sys_status', 0)
    elif (user_option == "U"):
        list_worksheet('sys_users', 0)
    elif (user_option == "H"):
        show_help("M")
    else:
        print_error("Invalid option, try again")
    print("")
    input(colored("Press ENTER key to return to main menu....",
                  'black', 'on_white'))
    return True


def show_help(options):
    """
    This function show_help() prints a set of help text.
    It explains the type-ahead capabilities and how they can be used once
    a person understands the sys navigation.
    When RepairsTracker moves from demo to PROD the references to userids
    will need to be removed.
    """
    print("")
    print_title("---------------------------------")
    print_title("- REPAIRS TRACKER - HELP SCREEN -")
    print_title("---------------------------------")
    print_subtitle("     SECURITY:                                           "
                   + "    ")
    print_body("To use the system, you must have a userid and password      ")
    print_body("Access is provided at User or Administrator(superuser) level")
    print_subtitle("     MAIN MENU OPTIONS:                                 "
                   + "    ")
    print_body("Type-ahead is supported, if you know sub-menu opt, e.g.     ")
    print_body("EE Enter Est, ER Enter Repair, F12345 find repair 12345    ")
    print_subtitle("    (E)nter new estimate/repair:                        "
                   + "    ")
    print_body("Repairs track phone#, name, item details, pricing, dates    ")
    print_body("Estimates: typically more complex, e.g. jobs needing extra  ")
    print_body("pricing, or requiring ordered-in components.                ")
    print_subtitle("    (F)ind existing estimate/repair:                    "
                   + "    ")
    print_body("Use typeahead if repair# known, or enter specific #         ")
    print_body("If not found, all repairs can be listed.                    ")
    print_subtitle("    (N)otify customers of repair completion:            "
                   + "    ")
    print_body("This updates the repairs record to completed and generates  ")
    print_body("customised SMS for sending. Typeahead w/repair # e.g. N12345")
    print_subtitle("    (M)aintain system:                                  "
                   + "    ")
    print_body("Only available to administrator-level users.  This displays ")
    print_body("system files, e.g. customers, item types, users.            ")
    print_body("Typeahead to choose which file e.g. MC Maintain Customers   ")
    print_subtitle("    (H)elp:                                             "
                   + "    ")
    print_body("This text currently showing on-screen is the help text      ")
    print("")
    input(colored("Press any key to return to main menu....",
                  'black', 'on_white'))
    return True


def menu_manager(valid_user):
    """
    The menu_manager() function displays the main menu options.
    This is designed to continue running until the user selects
    option X to exit
    """
    print_title("-------------------------------------------")
    print_title("--     REPAIRS TRACKER - MAIN MENU:      --")
    print_title("-------------------------------------------")
    print_subtitle("    (E)nter new estimate/repair            ")
    print_subtitle("    (F)ind existing estimate/repair        ")
    print_subtitle("    (N)otify customers of repair completion")
    print_subtitle("    (M)aintain system                      ")
    print_subtitle("    (H)elp                                 ")
    print_subtitle("    e(X)it                                 ")
    print("")

    input_string = input(colored("Option: ", 'black', 'on_white')).upper()
    if input_string != "":
        user_option = input_string[0]
        if (user_option == "X"):
            valid_user = False
            return valid_user

        if (input_string[1:] != ""):
            further_options = input_string[1:]
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
            print_error("Invalid option, try again")
    else:
        print_error("Blank option, try again")
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
    user_name = input(colored("Please enter username: ", 'black', 'on_white'))
    password = input(colored("Password: ", 'black', 'on_white'))
    valid_user = authenticate_user(user_name, password)
    while valid_user:
        valid_user = menu_manager(valid_user)
    print_message("Exiting... Thank you for using RepairsTracker...")
    print("")
    return True


main()
