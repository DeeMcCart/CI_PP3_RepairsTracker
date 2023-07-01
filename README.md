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
    1. [Skeleton - Wireframes; ](#wireframes)
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
    1. [HTML Validation](#html-validation)
    2. [CSS Validation](#css-validation)
    3. [Javascript Validation](#javascript-validation)
    4. [Accessibility](#accessibility)
    5. [Performance](#performance)
    6. [Multi-device Testing](#multi-device-testing)
    7. [Multi-browser Testing](#multi-browser-testing)
    8. [Testing user stories](#testing-user-stories)
    9. [Unfixed Bugs](#unfixed-bugs)
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
RepairTracker is a python-based database application designed to replace a manual (paper-based) system of jewellery repair tracking.  This is a real-world requirement, and while the version of RepairTracker presented is a demo version, the app is intended for live use in the near future.
 
<ul> <em>Help:</em>  
    <li>  </li>
    <li>  </li>
(refer to 'Help' for more details - https://repairs-tracker-aa30320aef0e.herokuapp.com/

### Responsive Mockup
https://ui.dev/amiresponsive?url=https://deemccart.github.io/CI_PP2_HumbleNumble/

### Live webpage link
https://deemccart.github.io/CI_PP2_HumbleNumble

## Project Goals
----------------
1. To produce a 6-try numbers-based game. 
2. Using a mobile-friendly development development approach.  
3. Which uses the capabilities of HTML, CSS and Javascript.
4. And is possible to play with a reasonable chance of success.
  
### UX Design Strategy
Wordle (https://www.nytimes.com/games/wordle/index.html) is a game which began as a personal project for software engineer Josh Wardle.   As of Jan 2022 it had 2M weekend players (theguardian.com 'Wordle-creator-overwhelmed-by-global-success-of-his-puzzle') and was subsequently acquired by the New York Times.  The Guardian wrote that 'Wordle’s popularity is thought to be partly because, in an era of apps aggressively competing for your attention and time, the game was deliberately built to be played once a day, and without features designed to promote its growth such as push notifications and email sign ups.'  Current estimates are of 250K daily users, many of whom are repeat users, and 57% of whom play the game on their smartphone (blog.gitnux.com).

Humble Numble aims to piggyback on the Wordle philosophies of:
* simple interface with uncluttered screen
* clearly understood rules
* scarcity - user can only access one game per day
* reponsiveness - ability to play on small screens (convenient for user)
* no time-out - can fit into small pockets of time as game remains on-screen until 6 guesses completed
* feedback and interaction - user immediately gets feedback when they press ENTER on a guess
* statistic tracking - user can track # of attempts to solve, number of days solved, success rates
* peer-group communication - user can share their problem-solving pattern (without revealing any part of the solution) to friends who may also play
<br>
<br>
### UX Design Strategy Analysis - Existing Numble Games

Using Google search, the following were identified as possible Numble websites -
<br>
https://thenumble.app/ <br>
https://numble.wtf <br>
https://numble.game <br>
https://numble.win<br>
https://numble.online<br>
https://en.wikipedia.org/wiki/Numble (wikipedia)<br>
Whilst these sites individually contain some good features, none is comparable to the range of functionality, and simplicity of design, available from the Wordle site.   

<details><summary>Analysis of Existing Numble Websites</summary>
<img src="https://deemccart.github.io/CI_PP2_HumbleNumble/docs/readme_images/strategy_competitive_analysis.jpg"></details>

### UX Design Strategy Target Audience
The aim of this specific website is develop a Numble game which can be played in simple form

The target audience is:<br>
a. People who enjoy puzzle-solving<br>
b. People who already play Wordle and are familiar with the user interface (e.g. grey, orange, green guess-letter evaluation; 6 tries,  grid layout)<br>
c. People who want to have a reliable consistent experience through out the game (in other words, they want an opportunity to finish the game by reaching the end, and they want to be able to trust the process (ie they can understand how they move forward or backwards, and they dont feel it is unfair or impossible to complete).<br>
d. People who like to practice their mathematical skills<br>

* Game players
* who enjoy mathematical puzzles
* and want to have a bit of fun doing it

## UX Design Scope
----------------

### UX Design Scope User Requirements and Expectations
<br>
From the analysis of existing games, a set of possible requirements was identified for a new portal.
<br><br>
The basic requirement for users is to have access to a 'fair' game where they have a possibility of reaching the goal.
Humble Numble is a fun way of applying simple mathematical principles
    
<ul>MVP Requirements:
<li>Must be intuitive to use</li>
<li>Must be easy to learn</li>
<li>Good for first time or returning users</li>
<li>Accessible - no ad display & no paywall</li>
<li>Familiar interface for Wordle consumers</li>
</ul>
<br>
<ul>Requirements - Desirable:
<li>Would like to share results (graphic showing the pattern of result)</li>
<li>Would like to be able to track user statistics (cookies)</li>
<li>Would like to be able to auto-generate new equations</li>
<li>Would like to be able to track equations already used</li>
<li>Would like to be able to set difficulty levels</li>
</ul>
<br>
<ul>To incorporate as many of the Wordle characteristics below as possible:
<li>Simple interface with uncluttered screen</li>
<li>clearly understood rules</li>
<li>scarcity - user can only access one game per day</li>
<li>reponsiveness - ability to play on small screens (convenient for user)</li>
<li>no time-out - can fit into small pockets of time as game will remain on-screen until 6 guesses completed</li>
<li>feedback and interaction - user immediately gets feedback for each guess</li>
<li>statistic tracking - user can track # of attempts to solve, number of days solved, success rates</li>
<li>peer-group communication - user can share their problem-solving pattern (without revealing any part of the solution) to friends who may also play</li>
</ul>

### UX Design Scope - Data
A set of equations are pre-loaded which are consistent with game rules (e.g. operator numbers not > 20, calculations return an integer value)
Currently Humble Numble will randomly select one of these equations for each game.

## User Goals/ User Stories
----------------
    
### Site owner Goals
* SO_01 As site owner I want to provide a fun, satisfying game which is visually engaging and highly interactive
* SO_02 As site owner I want to provide a familiar interface for Wordle consumers (to assist in user learning and ease of adoption for a large pre-existing user base)
* SO_03 As site owner I want to provide an interface which is uncluttered, free from ads, and not behind a paywall
* SO_04 As site owner I want to include a mathematical learning experience in this game
* SO_05 As site owner I want to provide straightforward, intuitive, consistent website navigation
* SO_06 As site owner I want to provide a website, which meets current programming, performance and accessibility standards (html, css, javascript, responsive, accessibility, performance)
* SO_07 As site owner I want to provide an opportunity for the user to provide feedback, including reporting issues, or suggesting improvements to the Humble Numble site
* SO-08 As site owner I want to acknowledge to the user that their feedback has been received
* SO-09 (FUTURE) As site owner I would like to implement scarcity - so that user can only access one game per day
* SO-10 (FUTURE) As site owner, I would like to auto-generate new equations
* SO_11 (FUTURE) As site owner, I would like to be able to track equations already used
* SO_12 (FUTURE) As site owner, I would like to be able to set difficulty levels
* SO_13 (FUTURE) As site owner, I would like to provide player stats - user can track # of attempts to solve, number of days solved, success rates
* SO_14 (FUTURE) As site owner, I would like to facilitate users to share their problem-solving pattern (without revealing any part of the solution) 

### First-time User Goals
* FTU_01 As a first time user I am curious about what this site does, and may just want to quickly play a game
* FTU_02 As a first time user I would like to be able to easily navigate the site and quickly learn its functionality (particularly if I am already a Wordle user)
* FTU_03 As a first time user I would like to easily understand game rules
* FTU_04 As a first-time user I want clear, timely and unambiguous feedback and interaction 
* FTU_05 As a first-time user I expect links and functions that work as expected
* FTU_06 As a first-time user who is curious about mathematical equations, I want to practice mental maths using a puzzle solving game
* FTU_07 As a first time user I would like to see my score and receive feedback on my performance
* FTU_08 As a first time user I would like to play on my device of choice (quite likely my mobile - reponsiveness)  

### Returning User Goals
* RU_01 As a returning user I wish to play the game, just because I enjoy it
* RU_02 As a returning user I want to 'beat the computer' by guessing the solution within 6 tries
* RU_03 no time-out - can fit into small pockets of time as game will remain on-screen until 6 guesses completed
* RU_04 As a returning user I definitely want to be able to see any equation which I didn't guess within 6 tries
* RU_05 As a returning user I would like to receive a 'fresh' challenge each time I play (ie not an equation thats been used before)
* RU_06 As a returning user I want to feel that the game is 'fair' and that I can apply my skills to playing it
* RU_07 As a returning user I would like to be able to contact the developer and to provide suggestions for game enhancement
* RU_08 (FUTURE) As a returning user I would like to be able to share my results with my friends (graphic showing the pattern of result)
* RU_09 (FUTURE) As a returning user I would like to receive only one challenge per day (to avoid being sucked into a timewarp of endless gaming)
* RU_10 (FUTURE) As a returning user I would like to be able to track my statistics and to track/ maintain/ improve my winning streak

### Other stakeholder Goals
* OT_01 As an educator I might wish to suggest new equations to be solved by Humble Numble players 
* OT_02 As an educator I might promote the use of this game amongst my students to increase their mathematical skills


## UX Design Decisions
----------------

### Wireframes
<details><summary>Landing Page</summary>
<img src="https://deemccart.github.io/CI_PP2_HumbleNumble/docs/readme_images/wf1_hn_landing.png">
</details>

<details><summary>How To Play</summary>
<img src="https://deemccart.github.io/CI_PP2_HumbleNumble/docs/readme_images/wf2_hn_howtoplay.png">
</details>

<details><summary>Game screen</summary>
<img src="https://deemccart.github.io/CI_PP2_HumbleNumble/docs/readme_images/wf3_hn_game.png">
</details>

<details><summary>Game screen in progress</summary>
<img src="https://deemccart.github.io/CI_PP2_HumbleNumble/docs/readme_images/wf4_hn_game_inprogress.png">
</details>

  
### Fonts Chosen
The fonts are deliberately chosen to mimic appearance of Wordle screen. 
In real life, Wordle uses proprietary fonts (NYT Karnak Condensed), with Helventica Sans for the grid and button text.  A reasonably close match, which is widely available on a range of devices, was thought to be the Google bebas Neue font.

However, when testing the site this did not present a good look, and so Roboto Slab was chosen as a better alternative.
Fallback fronts are used in both cases

### Colour Scheme 
The colour combinations mimic Wordle's game (for consistency and to ease the user learning experience).
   
The choice of colours for Humble Numble is very much in accordance with user stories S_02 (closely emulate the Wordle look & feel); FTU_02 (first-time user to easily navigate and learn the site) - consistent with Wordle so as to speed the learning process and encourage the focus on the game content, rather than on how to use it.

<details><summary>Colours- similar to Wordle</summary>
<img src="https://deemccart.github.io/CI_PP2_HumbleNumble/docs/readme_images/f07_game_grid_in_progress.jpg">
</details>

### Design Images
This site has very few images as the focus is on the game content.
A 'Wordle-type' logo is used on the Intro page.
<details><summary>'Wordle-type' logo</summary>
<img src="https://deemccart.github.io/CI_PP2_HumbleNumble/docs/readme_images/numble_icon.jpg">
</details>

### Design Images - Icons and Symbols

Certain icons and symbols (again based on Wordle look & feel) are used for quicklinks e.g. ? for About page, graphy symbol for Stats page, cog symbol for settings page. 


## Features 
 
### F01 Intro Screen
<details><summary>Introduction screen</summary>
<img src="https://deemccart.github.io/CI_PP2_HumbleNumble/docs/readme_images/f01_intro.jpg"></details>
<br>
On first using the game an introduction window is shown, the user can choose 'Play' or 'How to Play' buttons.  The intro page shows the current date, the Humble Numble day number, and some copyright and acknowledgement notices.
This addresses user stories SO_01, SO_02, FTU_01, FTU_02, FTU_03
<br>
<br>

### F02 'How To Play' Screen
<details><summary>How To Play screen</summary>
<img src="https://deemccart.github.io/CI_PP2_HumbleNumble/docs/readme_images/f02_help.jpg"></details>
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


## Validation 

### HTML Validation 
- HTML
  - No errors returned on the index html pages when checked in the W3C validator:
  - [W3C validator - index page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fdeemccart.github.io%2FCI_PP2_HumbleNumble%2Findex.html) 
  - [W3C validator - 404 page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fdeemccart.github.io%2FCI_PP2_HumbleNumble%2F404.html)
  
  - [W3C validator - settings page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fdeemccart.github.io%2FCI_PP2_HumbleNumble%2Fsettings.html)

### CSS Validation
  - No errors returned when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https://deemccart.github.io/CI_PP2_HumbleNumble/&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) 

### Javascript Validation
  - No errors returned, when javascript was pasted into the jshint validator - however 10 unused variables were identified, which are the function names.    
<details><summary>jshint - no errors however the function names were identified as unused variables</summary>
<img src="https://deemccart.github.io/CI_PP2_HumbleNumble/docs/readme_images/jshint_result.jpg">
</details>

### Accessibility
The site was tested using the WAVE WebAIM accessibility evaluation tool.
All pages pass with 0 errors 
- [Accessibility: index page](https://wave.webaim.org/report#/https://deemccart.github.io/CI_PP2_HumbleNumble/)
- [Accessibility: 404 page](https://wave.webaim.org/report#/https://deemccart.github.io/CI_PP2_HumbleNumble/404.html)


### Performance
Performance for all pages was tested using the Lighthouse tool within Google Chrome.  Performance was at 98% for the index page (intro modal).

<details><summary>Performance: Index page</summary>
<img src="https://deemccart.github.io/CI_PP2_HumbleNumble/docs/readme_images/performance_lighthouse_intro_page_230602.jpg">
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
* https://stackoverflow.com/questions/1977694/how-can-i-change-my-desktop-background-with-python?rq=4 
* https://tkdocs.com/


 
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
