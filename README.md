# RepairTracker
(Developer:  Deirdre McCarthy, July 2023)

# Table of Contents:
1. [About](#about)
2. [Project Goals: ](#project-goals)
    1. [UX Design - Strategy ](#ux-design-strategy) 
    2. [UX Design - Strategy - Competitor Portals](#ux-design-strategy-analysis-of-competitor-offerings)
    3. [UX Design - Strategy - Target Audience](#ux-design-strategy-target-audience)
3. [UX Design - Scope](#ux-design-scope)
    1. [UX Design - Scope - User Requirements and Expectations](#ux-design-scope-user-requirements-and-expectations)
    2. [UX Design - Scope - Data](#ux-design-scope-data)
    3. [UX Design - Scope - Viewing Device](#ux-design-scope-viewing-device)
4. [User goals/ user stories: ](#user-goals-user-stories)
    1. [Site Owner Goals](#site-owner-goals)
    2. [First-time User Goals](#first-time-user-goals)
    3. [Returning User Goals](#returning-user-goals)
    4. [Other stakeholder Goals](#other-stakeholder-goals)
5. [Further UX Design: ](#ux-design-decisions)
    1. [Skeleton - Flowcharts; ](#flowcharts)
    2. [Surface - Fonts; ](#fonts-chosen)
    3. [Surface - Colours](#colour-scheme)
    4. [Surface - Imagery](#design-images)
6. [Features](#features)
    1. [Included](#features-in-scope)
    2. [Future Development](#features-left-to-implement)
7. [Technology](#technologies)
    1. [Languages](#langugages)
    2. [Frameworks and Tools](#frameworks--tools)
8. [Validation](#validation)
    1. [Python Validation](#python-validation)
    2. [Accessibility](#accessibility)
    3. [Performance](#performance)
    4. [Multi-device Testing](#multi-device-testing)
    5. [Multi-browser Testing](#multi-browser-testing)
    6. [Testing user stories](#testing-user-stories)
    7. [Unfixed Bugs](#unfixed-bugs)
9. [Accessibility](#accessibility)
10. [Performance](#performance)
11. [Deployment](#deployment)
12. [Credits](#credits)
    1. [Content](#content)
    2. [Media](#media)
    3. [Code](#code)
    4. [References](#references)
    5. [Acknowledgements](#acknowledgements)

## About
---------
RepairTracker is a python- and google-sheets DBMS application intended to replace a manual (paper-based) system for tracking the lifecycle of jewellery repair.  This is a real-world requirement, and while the version of RepairTracker presented is a demo version, the app is aiming towards live use.
 
<ul> <em>Help:</em>  
    <li>  </li>
    <li>  </li>
refer to 'Help' for more details - https://repairs-tracker-aa30320aef0e.herokuapp.com/

### Responsive Mockup
A responsive mockup is given here,  although in practice the user interface is a 80-char x 24 line text display regardless of device:
https://ui.dev/amiresponsive?url=https://repairs-tracker-aa30320aef0e.herokuapp.com/
(and, in fact, the user interface when tested on a mobile device did not function correctly, and operated with anomolies when used on a Samsung Galaxy tablet)

### Live webpage link
https://repairs-tracker-aa30320aef0e.herokuapp.com/

## Project Goals
----------------
1. To automate the existing manual steps for repair tracking, from initial entry through to in-progress, customer notification and collection/payment. 
2. Using the integration capabilities of python (and associated libraries) to link to Google Sheets as a reasonaby basic DBMS, and bolt-on libraries for SMS notifications (and, in the future, label printing).  
3. Which is not significantly slower than the current manual (handwritten) system.
4. And which provides additional functionality for customer tracking, repairs status reporting.
5. And which provides some capabilities for customisation/ configuration, ie access to maintain certain system parameters.
  
### UX Design Strategy
As this program is delivered using Python, the emphasis is on functionality rather than appearance.
However, in line with project goal #3, some features have been included to streamline data entry.  For example, on the main menu, the user can enter a single-character option (E)nter, (H)elp, etc.  When presented with a sub-menu, they can then enter a further single-character option, e.g. the 'Enter' sub-menu has options for (E)stimate, (R)epair, etc.
To streamline data entry, a user familiar with the menu structure can directly enter a multi-character string to immediately access a sub-menu.  A typical example would be ER to choose Enter - Repair.   

Other UX design considerations include meaningful error messages and status messages.
Status code is used track each repair lifecycle.  This makes current status, worklaod and throughput of estimates/repairs clearly visible.
As per project goal #4, functionality within RepairTracker allows repairs status to be filtered and reported on.
<br>
<br>
### UX Design Strategy Analysis - Existing Repair Tracking Apps
Commercially available repair tracking apps do exist, however, these often form part of a larger suite of business modules, integrated with payment and inventory systems. As such, implementation involves monthly subscription costs and an implementation effort.
RepairTracker is a simple approach to meet the repair tracking aspects only.  It is sufficiently customisable for use in a small-medium sized business, and is quick to use 'out of the box'.

### UX Design Strategy Target Audience
Target users are small-medium sized jewellery shops who perform repairs for inhouse (and possibly external) customers.

## UX Design Scope
----------------

### UX Design Scope User Requirements and Expectations
<br>
<ul>MVP Requirements:
<li>Must be intuitive to use</li>
<li>Must be easy to learn</li>
<li>Good for first time or returning users</li>
</ul>
<br>
<ul>Requirements - Desirable:
<li>Would like to track status of repairs</li>
<li>Would like to be able to configure with system with new options, e.g. for item or metal types</li>
<li>Would like to be able to maintain/ review a list of customers</li>
<li>Would like to be able to automatically notify customers of repairs which are due for collection</li>
<li>Would like to be able to track repairs which are (over)due for collection</li>
<li>Would like to gather data for ad-hoc statistical analysis of repairs (average price, weekly throughput, etc) </li>
</ul>
<br>
### UX Design Scope - Data
A single Google spreadsheet is used to hold the DMBS.
This is pre-populated with configuration data as follows:
* sys_cust holds a list of the customers known to the system;
* sys_mat holds the type of material/metals and is recorded when a repair is received;
* sys_users holds a list of userids and passwords known to the system, and whether each has user or administrator access;
* sys_item holds jewellery item types, e.g. (W)atch, (E)arrings;
* sys_status holds the lifecycle of an estimate/ repair


## User Goals/ User Stories
----------------
    
### Site owner Goals
* SO_01 As site owner I want to provide a jewellery repair tracking system which meets user requirements
* SO_02 As site owner I want the jewellery repair tracking system to be more efficient than current manual processes
* SO_03 As site owner I want to provide a system which is intuitive and easy to learn 
* SO_04 As site owner I want to provide shortcuts for experienced users, to speed up data entry
* SO_05 As site owner I want to provide automated customer notification when repairs are complete
* SO_06 As site owner I want to ensure that all data entry is validated and captured in conistent format (e.g. mixed case or upper-case as appropriate) to allow for consistent reporting
* SO-07 As site owner I want to provide immediate feedback on erroneous data entry 
* SO-08 As site owner I want to provide basic authentication and security to prevent unauthorised usage
* SO-09 As site owner I want to provide reporting capabilities e.g. for repair status tracking
* SO_10 As site owner I want to develop code and documentation which meets industry (PEP8) standards
* SO-11 (FUTURE) As site owner I want to implement label printing as each repair is entered
* SO_12 (FUTURE) As site owner I want to allow authorised users the ability to configure and expand the system

### First-time User Goals
* FTU_01 As a first time user I want to be able to enter repair details quickly and accurately
* FTU_02 As a first time user I would like to be able to easily navigate the site and quickly learn its functionality 
* FTU_03 As a first time user I would like to be able to access help for the various system functions
* FTU_04 As a first-time user I want clear, timely and unambiguous feedback and interaction 
* FTU_05 As a first-time user I expect links and functions that work as expected

### Returning User Goals
* RU_01 As a returning user I want keyboard shortcuts to speed up data entry, rather than menu-only navigation
* RU_02 As a returning user I want to enter estimates quickly and accurately
* RU_03 As a returning user I want to enter repairs quickly and accurately
* RU_04 As a returning user I want to convert an estimate to a repair 
* RU_05 As a returning user I want to view status of repairs, on an individual or group basis
* RU_06 As a returning user I want to notify customers that their repair is completed and awaiting collection
* RU_07 As a returning user I want to update a repair to show that it has been collected
* RU_08 As a returning user (administrator) I want visibility of system setup data
* RU_09 As a returning user I want to be able to view data (e.g. customers) within the RepairTracker system
* RU_10 (FUTURE) As a returning user (administrator) I want to amend RepairTracker system data
* RU_11 (FUTURE) As a returning user I want to report on repairs by status (e.g. entered, awaiting parts, completed, awaiting collection)
* RU_12 (FUTURE) As a returning user I want to report on repairs by due date (e.g. overdue) 
* RU_13 (FUTURE) As a returning user (administrator) I want to modify the status of a repair record e.g. to 99 (closed by Administrator)

### Other stakeholder Goals
* OT_01 As a customer I want to receive a repair docket with a unique repair # and accurate details when I submit my repair
* OT_02 As a customer I want an initial estimate of when my repair will be ready to collect
* OT_03 As a customer I want to receive prompt notification when my repair is completed
* OT_04 As a cutomer I want to enquire as to the currents status of my repair
* OT_05 (FUTURE) As a customer I would like to receive a reminder if I am overdue in collecting my repair


## UX Design Decisions
----------------

### Flowcharts
<details><summary>Main Menu</summary>
<img src="https://github.com/DeeMcCart/CI_PP3_RepairsTracker/blob/main/assets/images/readme_images/flowchart_overview_with_authentication.jpg">
</details>

<details><summary>Enter repair/estimate</summary>
<img src="https://github.com/DeeMcCart/CI_PP3_RepairsTracker/blob/main/assets/images/readme_images/flowchart_enter_repair.jpg">
</details>

<details><summary>Complete Repair - Notify Customer</summary>
<img src="https://github.com/DeeMcCart/CI_PP3_RepairsTracker/blob/main/assets/images/readme_images/flowchart_complete_notify.jpg">
</details>

<details><summary>Customer Collect/ Completion</summary>
<img src="https://github.com/DeeMcCart/CI_PP3_RepairsTracker/blob/main/assets/images/readme_images/flowchart_collect.jpg">
</details>

  
### Fonts Chosen
n/a as quite limited..... however would ideally like to apply some colours to the text.

### Colour Scheme 
Would like to have different colours for error messages, status messages etc.

<details><summary>Colours- used for prompt & feedback to user & to aid user learning</summary>
<img src="https://deemccart.github.io/CI_PP3_RepairsTracker/docs/readme_images/colour_examples.jpg">
</details>

### Design Images
Ideally would like to have a background or splash image which bounds the entry screen as the black and white text based screen drives me up the wall.
<details><summary>Background image</summary>
<img src="https://deemccart.github.io/CI_PP3_RepairsTracker/docs/readme_images/background_image.jpg">
</details>

### Design Images - Icons and Symbols
N/a to text-based display

## Features 
 
### F01 Authentication
The user must give a valid userid and password to gain entry to the system (this demo version is provided with u-u for user-level access and s-s for administrator/super-user access) 
These userids and passwords are stored within Google sheets
<br>
The use of basic authentication satisfies user requirements SO-01, SO-08, SO-12, FTU-04, RU-08, RU-09, RU-13<br>
<br>

### F02 'MAIN MENU' & Navigation
<details><summary>Main Menu options</summary>
<img src="https://deemccart.github.io/CI_PP3_RepairsTracker/docs/readme_images/f02_main_menu.jpg"></details>
<br>
The main menu lists options each of which is identified by a letter of the alphabet.  The user can enter an option (in upper or lower case) and will be brought to the linked sub-menu.
Heading title., subtitle and content are presented with consistent appearance and colours.  
<br>
This meets user requirements SO03, FTU02, FTU05.
<br>      

### F03 Typeahead
<details><summary>typeahead</summary>
<img src="https://deemccart.github.io/CI_PP3_RepairsTracker/docs/readme_images/f03 Typeahead.jpg"></details>
If, from the main,menu, the user already knows the submenu option they can key this also, e.g. EE to take the (E)nter option from main menu then (E)stimate from sub-menu.<br>
For more complex processes which may involve updates/searching for a number of repair records, the user can typeahead giving multiple repair numbers, separated by a comma:
e.g. F12345,13456,15567 opens the find option and asks it to process 3 specific repairs records.
<br>
This satisfies user stories SO_02, SO_04, RU_01.
<br>
### F04 'Help' Screen
<details><summary>Help screen</summary>
<img src="https://deemccart.github.io/CI_PP2_HumbleNumble/docs/readme_images/f04_help.jpg"></details>
<br>
A modal 'How to Play' explains how to play and some of the subtleties of the calculations.  Available from the 'how to play' button on the Intro screen, or from the navbar help icon on all screens.   The 'How to Play' window can be scrolled to see full text, and is closed by clicking on the X in top right hand corner, at which point it disappears from screen.
<br>
<br>      

### F03 Play button
The Play button ![Play button](./docs/readme_images/f03_play_button.jpg?raw=true "Image of Play button") allows the user to go directly to a game screen, and immediately play a game ('call to action').
<br>
<br>

### F04 Randomly selected solution
<details><summary>Array of potential solutions</summary>
<img src="https://deemccart.github.io/CI_PP2_HumbleNumble/docs/readme_images/f04_solution_array.jpg"></details>
(Dont look too closely or you will ruin the surprise of playing the game!)<br>
An array of solutions is maintained, and, when the game starts, an entry is randomly chosen from this array.  At the time of development this array contained approx 20 entries, which is sufficient for demo purposes, it is envisioned that this will be extended in the future.
<br>
<br>

### F05 Uncluttered game screen
<details><summary>Initialised game screen</summary>
<img src="https://deemccart.github.io/CI_PP2_HumbleNumble/docs/readme_images/f05_uncluttered_game_screen.jpg"></details>
The game screen is presented to the user fully initialised (ie a target value has been set and populated to each grid row).  The screen is free of ads and supplemental displays, which allows the user to focus on the game.
<br>
<br>

### F06 Consistent Navbar<br>
The Navbar is consistent throughout the website, 404 and feedback pages.  (modals/pop-ups are used to show intro and help pages, which don't show the navbar but when they are closed, the navbar can be seen on the underlying page)  Contains icons for Help, Stats and Settings.
![Navbar](./docs/readme_images/f06_navbar.jpg?raw=true "Navbar image")
<br>
<br>

### F07 Game grid
<details><summary>Game panel</summary>
<img src="https://deemccart.github.io/CI_PP2_HumbleNumble/docs/readme_images/f07_game_grid_in_progress.jpg"></details>
Interactive and responsive game panel which allows the user to record one set of guess tiles per attempt (the current attempt # is shown at top of screen).  The game grid is initially blank, and will be populated with successive user guesses.
Interactivity/feedback:  when the user presses ENTER to submit a guess, the guessed tiles update as green(correct); orange(present) or grey(absent).
<br>
<br>

### F08 Keyboard display
<details><summary>Keyboard</summary>
<img src="https://deemccart.github.io/CI_PP2_HumbleNumble/docs/readme_images/f08_keyboard_grid.jpg"></details>
A pseudo-keyboard shows the permitted entries.  The user must click on the keys using a mouse pointer to select an entry.  When a keyboard key is pressed, its colour flickers to light blue, and the key value is loaded to the current guess row on the game grid.  So the keyboard is the main user control for the game, and each press of a keyboard key triggers an action.   (keys 1-20, */-+ populate the game grid).<br>
When the user presses ENTER to submit a guess, the keyboard elements used within the guess also update as green(correct); orange(present) or grey(absent).
<br>
<br>

### F09 DEL key
A backspace key is provided which allows the user to remove the last keyed entry on the current grid row.
<br>
<br>

### F10 ENTER key
The ENTER key submits the current guess row for validation. 
<br>
<br>

### F11 Equation validation
When a guess is submitted, the equation which the user has submitted is parsed and validated as follows - the entries at the second and fourth columns are assessed to ensure these contain an operator (plus minus multiply divide); the guessed equation is then validated to check if it equates to the target value.  If not, an error message is shown, however the game (at this version) will still progress to individual element valuation.
![If equation has wrong total](./assets/readme_images/f11_wrong_total.jpg?raw=true "Equation calculates to incorrect total")
<br>
<br>

### F12  Individual guess element validation
<details><summary>Feedback on keyboard re guessed solution</summary>
<img src="https://deemccart.github.io/CI_PP2_HumbleNumble/docs/readme_images/f12_keyboard_interaction_feeback.jpg"></details>
Each element of the guess is compared to the solution, and its tile colour amended according to whether the guessed tile is:
* correct (green)- tile value is at this position in the solution;
* present (orange)- tile value is at a different position in the solution;
* absent (grey) - tile value is not in the solution.
![Feedback on game panel re guessed solution](./docs/readme_images/f12_game_interaction_feeback.jpg?raw=true "Image of guessed tiles changing colour")

The corresponding keyboard grid value is coloured on the lower part of the screen, e.g. '5' guessed correct; will colour both the row tile and the keyboard key green.  A (hidden) count of the number of correct elements is maintained.
<br>
<br>

### F13 Success message
<details><summary>Appropriate success message, content varies by # of attempts</summary>
<img src="https://deemccart.github.io/CI_PP2_HumbleNumble/docs/readme_images/f13_attempt4_result.jpg"></details>
 This displays when all elements correctly guessed.  A pop-up message with the appropriate text appears.  This text mimics the Wordle site, so depending on the  number of attempts the successful user can get (Genius, Magnificent, Impressive, Splendid, Great, Phew).
<br>
<br>

### F14 Solution display if exceeded 6 attempts
<details><summary>Solution display if 6 unsuccessful guesses</summary>
<img src="https://deemccart.github.io/CI_PP2_HumbleNumble/docs/readme_images/f14_exceeded_6attempts.jpg"></details>
A pop-up message with the appropriate text appears if the user has matched the entire solution equation.  This text mimics the Wordle site, so depending on the  number of attempts the user can get (Genius, Magnificent, Impressive, Splendid, Great, Phew)
<br>
<br>

### F15 User Statistics 
<details><summary>User statistics</summary>
<img src="https://deemccart.github.io/CI_PP2_HumbleNumble/docs/readme_images/f15_user_statistics.jpg"></details>

This screen is really a placeholder for future functionality as would like to display some of the statistics for a player over a number of games<br>
<br>

### F16 Settings and Feedback
<details><summary>User settings</summary>
<img src="https://deemccart.github.io/CI_PP2_HumbleNumble/docs/readme_images/f16_settings_feedback.jpg"></details>

This allows the user to provide feedback and to choose to join a daily reminder mailing list.  There are placeholder questions here for future Limit to one game daily (preset to 'no limit');
Difficulty levels: easy or difficult (preset to 'difficult').
Share image of solution to clipboard (future)
<br>
<br>

### F17 Responsiveness
The site is designed to be fully responsive so it can be played on a range of convenient devices.

### Features in Scope 

<details><summary>Mapping of user stories to features</summary>
<img src="https://deemccart.github.io/CI_PP2_HumbleNumble/docs/readme_images/user_stories_vs_features.jpg"></details>

This website includes 3 pages and 16 features 
The pages - which effectively bring the features lited in the previous section together - are:
* Landing Page (see feature F01 Intro Screen)
* Settings page (see feature F16 Feedback and settings )
* 404 error page 

- __404 Error Page__ 
This allows graceful failure, where the header and footer are preserved, allowing the user to navigate away from an error page using the site navigation (rather than the back button).

<details><summary>404 error page</summary>
<img src="https://deemccart.github.io/CI_PP2_HumbleNumble/docs/readme_images/p03_error_404_page.jpg"></details>

### Implementation Decisions
Pre-defined calculations are stored in a multi-dimensional array as follows:
Solution [
[ 3, *,_ 7 * 2, 41_], // ie 3 * 7 * 2 = 41
[2, + , 5 * 7, 41] //ie 2 + 5 * 7 = (7) * 7 = 41
]
Each day's equation can therefore be referenced as Solution[day#]
Each days' elements can be referenced as solution[day#, element#]
This is useful when comparing a user entry for a match.

Daily user entries are stored in an array of 7 x 6 rows as follows:
Attempt [(undef, green, orange), (undef/green/orange), (undef/green/orange), (underf/green/orange), (undef/green/orange), (success)]
Attempt attempt#, element# can be compared to each of the entries in solution [day#, element#y] to search for a match - if found then if attempt.element# matches solution.element# then green, else orange.

Break out of loop when success, or when 6 tries reached.
<br>

### Features Left to Implement
While Humble Numble, at the current version, provides the 'engine' for pattern matching and calculation, there are a number of desirable features which exist in the current version of Wordle and which would greatly add to the user experience for Numble.

Choose difficulty level
* Allow the user to choose difficulty level EASY (all numbers <= 10) or DIFFICULT (numbers <=20 included).  Note that this has been allowed for in the array of solutions, these are classified according to difficulty, so this may be an 'easy win' future feature.

Allow the user to limit to one game daily
* One of the beautiful features of wordle is its limited-release mode whereby only one puzzle is released daily ... this creates a sense of anticipation and the user wants more, they don't get the chance to become bored or tired with the game.  
* Humble Numble at the current version, allows the user to play continuously by refreshing the browser.  This is useful when in testing and demonstration mode, but ideally the default would be one game per day.

Preserve user statistics from one game to the next
* This has been allowed for within the user interface by providing a statistics page, however the stats currently only relate to the latest game played.   Tracking of # of days 'winning streak' is very motivating to the user.

Share results
* Wordle has a feature whereby a user can share their pattern matching results without revealing the underlying solution.
<br>
<br>
               
## Technologies

### Langugages
- HTML 
- CSS
- Javascript

### Frameworks & Tools
* Github:  used to maintain the code repository, and for some readme edits and commits
* Git
* Gitpod:  used for editing and for tracking code commits back to Github
* Balsamiq:  used for wireframing
* Google Fonts: used to locate suitable fonts for website

### Libraries
* Twilio Client - used to generate SMS for customer notification once repair is completed
* gspread - used to access google worksheets/ spreadsheets 
* google.oauth2.service_account used for Credentials/ permissions management
* os - used to pickup environment variable(s)
* dotenv - used to picup environment variables
* time - used for sleep function
from termcolor import colored
from tabulate import tabulate
matplotlib.use('Agg')
* # from wallpaper import set_wallpaper, get_wallpaper
import tk
# import tkinter


## Validation 

### Python Validation 
- PEP8 validation
- The pycodestyle validator within the GitPod environment was used on 04/07/23 and, after corrections, returned 0 errors.
- Corrections required included over-long lines; whitespaces at end of lines - or on blank lines, missing spaces around operators
- under- or over-indentation, incorrect # of blank lines between functions.  When first run there were over 50 PEP8 errors present, 
- this was reduced to 0 by applying advised corrections, then verifying that the resulting code still functioned correctly.

https://pep8ci.herokuapp.com/#
The CI PEP8 validator was also used, by pasting my run.py code into here, and on 04/07/23 confirmed 0 linting issues.
<details><summary>Validation: CI PEP8 validator</summary>
<img src="https://github.com/DeeMcCart/CI_PP3_RepairsTracker/blob/main/assets/images/readme_images/val_ci_pep8.jpg">
</details>

### Accessibility
N/A for Python project

### Performance
Performance  - N/A for Python project?
Just in case - Ran Lighthouse over the heroku app and got 93% performance.

<details><summary>Performance: heroku deployed app</summary>
<img src="https://github.com/DeeMcCart/CI_PP3_RepairsTracker/blob/main/assets/images/readme_images/val_lighthouse_perf.jpg">
</details>


### Device Testing
The website was tested on the following devices:
* HP laptop
* Samsung Galaxy S10 tablet
* Motorola G(7) android phone

### Multi-browser Testing
The website was tested on the following browsers:
* Google Chrome v112.0.5615.138 (HP laptop)
* Google Chrome v112.0.5615.136 (Samsung Galaxy tablet)
* Mozilla Firefox v112.1.0 (Motorola g(7) phone)

### Testing User Stories
![User story testing](./assets/readme_images/user-stories-checked-against-features.jpg?raw=true "testing user stories")

### Bugs and issues
<details><summary>issue tracker</summary>
<img src="https://deemccart.github.io/CI_PP2_HumbleNumble/docs/readme_images/issue_tracker.jpg">
</details>
Quite a few calculation and display issues were encountered during development, the above lists the issues encountered and resolved.

## Deployment
<br>
* The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab - pages 
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

The live link can be found here - https://deemccart.github.io/CI_PP2_Humble_Numble/index.html

* To fork the repository:
- Go to the GitHub repository
- Click on Fork button in the upper right hand corner

* To clone the repository:
- Go to the GitHub repository
- Locate the Coe button above the list of files and click it
- Select if you prefer to clone using HTTPS, SSH, or Github CLI and click the copy button to copy the URL to you clipboard
- Open Git Bash
- Change the current working directory to the one where you want the cloned directory
- Type git clone and paste the URL from the clipboard($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)
- Press Enter to create your local clone


## Credits 
Multiple sources were used in assembling this site.

* Image credits:  https://www.istockphoto.com/ for wallpaper photo of jewellers bench


### Content - Humble Numble
* Inspiration taken from wordle.com
 
### Code - Humble Numble
* https://laracasts.com/series/wordle-workshop/episodes/2 for tips on building a wordle-like grid (using HTML or JS)
* https://www.youtube.com/watch?v=j7OhcuZQ-q8 Build a Wordle clone using HTML, CSS & Javascript! : used for tips on keyboard panel building (but thereafter preferred to code independently as found that coding shortcuts proposed were not always comprehensible to a new JS developer!)

### References
The following sites were used for research and improving  understanding while creating this website: 
* https://pythonguides.com/remove-first-character-from-a-string-in-python/
* https://stackoverflow.com/questions/11552320/correct-way-to-pause-a-python-program
* https://blog.finxter.com/python-convert-string-list-to-uppercase/#:~:text=The%20most%20Pythonic%20way%20to,new%20string%20list%2C%20all%20uppercase.
* https://www.studytonight.com/python-howtos/how-to-print-colored-text-in-python
* useriasminna - referenced project to see about tabulating, printing coloured text and adding a background image.  Located at the following URL:  https://github.com/useriasminna/american_pizza_order_system/tree/main 
* My fellow student Leonie McLaughlin for demonstrating Tabulate functionality
* https://stackoverflow.com/questions/1977694/how-can-i-change-my-desktop-background-with-python?rq=4 
* https://stackoverflow.com/questions/71678738/how-i-convert-a-string-representation-of-a-nested-list-into-a-nested-list
* https://tkdocs.com/
* Ulrike Riemenschneider for hints re background image 
* https://devcenter.heroku.com/articles/config-vars for details of how to map environment variables onto the runtime environment
* https://sparkbyexamples.com/python/using-python-dotenv-load-environment-variables/?expand_article=1
* https://www.trendmicro.com/en_ie/research/22/h/analyzing-hidden-danger-of-environment-variables-for-keeping-secrets.html
* https://www.askpython.com/python-modules/tabulate-tables-in-python
* https://twilio.com/docs/libraries/reference/twilio-python/
* https://www.youtube.com/watch?v=n2cF1e2tyhI What Is Twilio? SMS and Voice API's explained - Matt Kander
* https://realpython.com/python-testing/#:~:text=Automated%20testing%20is%20the%20execution,automated%20tests%20for%20your%20application.


 
### Acknowledgements
* I would like to sincerely thank my mentor, Mo Shami for his excellent guidance and support.
* I would also like to thank Derek and my family for their personal support.




# Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.
