"""
Main Hangman Program

Student ID: p2227168
Name:       Andrew Dillon Poh Jie Hao
Class:      DISM/FT/1B/01
Assessment: CA1-1

Script name:
    hangman.py

Purpose: 
    Runs the hangman game, using words from the various wordpool files and settings from the settings file.

Usage Syntax: 
    Run with play button

Input Files:
•	Simple Words: D:\psec\wordpool(simple).json
•	Complex Words: D:\psec\wordpool(complex).json
•	Simple Idioms: D:\psec\wordpool(simpleidioms).json
•	Complex Idioms: D:\psec\wordpool(complexidioms).json
•	Settings: D:\psec\settings.json
•	Game Logs: D:\psec\game_logs.json

Output Files:
•	None

Python ver:
    Python 3.10

Reference:
    None

Library/Module:
    None

Known Issues:
    None
"""

import json, random, pathlib, time, math
from datetime import datetime
directory = str(pathlib.Path(__file__).parent.resolve()) + '\\'

def playerlogin():
    """Allows player to input username
    """    
    print('Welcome to hangman!')
    global username
    invalidinput = True
    while invalidinput == True:
        invalidinput = False
        username = input('Enter username (uppercase and lowercase letters, \'-\' and \'/\' allowed)\n>> ')
        if username == '':
            invalidinput = True
        for character in username:  
            if character.isalpha() or character == '-' or character == '/':
                pass
            else:
                invalidinput = True
        if invalidinput == False:
            return
        else:
            print('Invalid username.')

def mainmenu():
    """Displays main menu for hangman.py
    """    
    while True:
        menu_input = input(f'\nHi {username}, what would you like to do?\n1. Play Hangman\n2. View Top Players\n3. Exit\n>> ')
        match menu_input:
            case '1':
                global startdate
                startdate = datetime.now().strftime('%d-%m-%Y %H:%M')    # Find current date and time
                playhangman()
                generatelogentry()
            case '2':
                displaytopplayers()
            case '3':
                print('See you next time!')
                exit()
            case _:
                print('Invalid input.')

def playhangman():
    """Function for user to play hangman
    """    
    # Load in settings
    with open(directory + 'storage\\settings.json', 'r') as settings:
        settings_dict = json.load(settings)
        global num_of_attempts, num_of_words, wordpool_dict
        num_of_attempts = settings_dict["number of attempts"]
        num_of_words = settings_dict["number of words"]
    
    global word_difficulty
    invalidinput = True
    while invalidinput:
        difficulty = input('\nSelect a difficulty:\n1. Simple Words\n2. Complex Words\n3. Simple Idioms-Proverbs\n4. Complex Idioms-Proverbs\n>> ')
        if difficulty == '1':
            with open(directory + 'storage\\wordpool(simple).json', 'r') as wordpool:
                wordpool_dict = json.load(wordpool)
            word_difficulty = 'Simple Words'
            invalidinput = False
        elif difficulty == '2':
            with open(directory + 'storage\\wordpool(complex).json', 'r') as wordpool:
                wordpool_dict = json.load(wordpool)
            word_difficulty = 'Complex Words'
            invalidinput = False
        elif difficulty == '3':
            with open(directory + 'storage\\wordpool(simpleidioms).json', 'r') as wordpool:
                wordpool_dict = json.load(wordpool)
            word_difficulty = 'Simple Idioms'
            invalidinput = False
        elif difficulty == '4':
            with open(directory + 'storage\\wordpool(complexidioms).json', 'r') as wordpool:
                wordpool_dict = json.load(wordpool)
            word_difficulty = 'Complex Idioms'
            invalidinput = False
        else:
            print('Invalid input.')
            
    print(f'You have {num_of_attempts} attempts of {num_of_words} words each. Good Luck!')

    # Generate all words to be used in the hangman session
    session_word_list = generatewords(wordpool_dict)
    global points
    points = 0

    # Loop through attempts
    for i in range(num_of_attempts):
        attempt_word_list = session_word_list[i]    # Use the list of words for the attempt from within the session list
        global set_lifeline_count
        set_lifeline_count = 0

        # Loop through words
        for j in range(num_of_words):
            global word, guess, correct_letters, num_of_correct_letters, correct_letters_display, lifeline_vowels
            word = attempt_word_list[j]
            incorrect_letters = ''
            num_of_incorrect_letters = 0
            correct_letters = []
            num_of_correct_letters = 0
            num_of_spaces = 0
            correct_letters_display = ''
            lifeline_vowels = 0
            word_lifeline_count = 0

            for k in range(len(word)):
                if word[k] == ' ':
                    correct_letters.append(' ')
                    correct_letters_display += ' '
                    num_of_spaces += 1
                else:
                    correct_letters.append('_')
                    correct_letters_display += '_'

            # Actions to perform in one guess
            while num_of_incorrect_letters < 5 and num_of_correct_letters < (len(word) - num_of_spaces):
                print(f"\nH A N G M A N\n\nPlayer: {username}\nAttempt: {i+1} of {num_of_attempts}\nWord: {j+1} of {num_of_words}")
                print(hangmanart(num_of_incorrect_letters))
                print(f'Incorrect letters: {incorrect_letters}({math.floor(len(incorrect_letters)/2)})')
                print(correct_letters_display)
                invalidguess = True
                while invalidguess:
                    guess = input('Select a valid character [a-z, \'] ("!" for lifeline): ').lower()
                    if guess == '!':
                        invalidguess = False
                        if set_lifeline_count < 2 and word_lifeline_count < 1:
                            picklifeline()
                            points -= 4
                            set_lifeline_count += 1
                            word_lifeline_count += 1
                        else:
                            print('You have no remaining lifelines.')
                    elif (guess.isalpha() or guess == "'") and len(guess) == 1:
                        invalidguess = False
                    else:
                        print('Invalid input.')
                if guess != '!':

                    # If letter guessed is correct
                    if guess in word:                           
                        
                        # Awarding of points
                        if points < 29:
                            points += 2
                        elif points == 29:
                            points += 1
                        elif points == 30:
                            pass
                        
                        # Checks if character was guessed previously
                        if guess in correct_letters:    
                            print('You already guessed this letter.')
                        else:
                            # Determines characters to display
                            correct_letters_display = ''            
                            for h in range(len(word)):             
                                if guess == word[h]:               
                                    correct_letters[h] = guess     
                                    num_of_correct_letters += 1
                                correct_letters_display += correct_letters[h]    

                    # If letter guessed is incorrect
                    else:
                        if guess in incorrect_letters:
                            print('You already guessed this letter.')
                        else:
                            incorrect_letters += guess + ' '
                            num_of_incorrect_letters += 1

            # If word is fully guessed or word is failed  
            if num_of_correct_letters == (len(word) - num_of_spaces):
                print(f'Congratulations! The secret word ({word_difficulty}) is "{word}": {wordpool_dict[word]}')
            elif num_of_incorrect_letters >= 5:
                print(f"\nH A N G M A N\n\nPlayer: {username}\nAttempt: {i+1} of {num_of_attempts}\nWord: {j+1} of {num_of_words}")
                print(hangmanart(num_of_incorrect_letters))
                print(f'Incorrect letters: {incorrect_letters}({math.floor(len(incorrect_letters)/2)})')
                print(correct_letters_display)                
                print(f'Maximum number of guesses!\nAfter {num_of_incorrect_letters} incorrect guess(es) and {num_of_correct_letters - lifeline_vowels} correct guess(es), the word was "{word}": {wordpool_dict[word]}')

            if j+1 < num_of_words:
                keepplaying = input('*****\nEnter [Y] to move on to the next word or [N] to quit: ').upper()
                valid = False
                while valid == False:
                    if keepplaying == 'Y':
                        valid = True
                    elif keepplaying == 'N':
                        valid = True
                        print('Thanks for playing!')
                        return
                    else:
                        keepplaying = input('Please enter a valid input.\n>> ').upper()
        
        # When attempt has ended, check is user wants to move on to the next attempt
        if i+1 < num_of_attempts:
            playagain = input(f'*****\nYour score is {points}\nEnter [Y] to play again or [N] to quit: ').upper()
            valid = False
            while valid == False:
                if playagain == 'Y':
                    valid = True
                elif playagain == 'N':
                    valid = True
                    if points > 15:
                        print(f'\nYou won, nice job!')
                    else:
                        print(f'\nBetter luck next time!')
                    print('Thanks for playing!')
                    return
                else:
                    playagain = input('Please enter a valid input.\n>> ').upper()

    # After all attempts are used up, displays highest score
    if points > 15:
        print(f'\nYour score is {points}, you won!')
    else:
        print(f'\nYour score is {points}, better luck next time!')

def generatewords(wordpool_dict):  
    """Generates a list of words for each attempt. The words for each attempt are stored as separated list within the parent list session_word_list.

    Args:
        wordpool_dict (dict): tells the function which wordpool_dict to use

    Returns:
        List: List containing lists which contain words for each attempt.
    """ 
    all_wordpool_indexes = []           # Create blank list to fill with all wordpool indexes (0 - last index of total wordpool)

    # session_word_list will be a 2D list that contains attempt_word_lists. e.g. [ ["dog","cat"], ["rock", "paper"], ["jump","duck"] ]
    session_word_list = []              
    for i in range(num_of_attempts):           
        session_word_list.append([])

    # Assign an index to each item in the wordpool
    for i in range(len(wordpool_dict)):
        all_wordpool_indexes.append(i)

    # Generates random word indexes to be taken from the wordpool  
    try:
        word_indexes = random.sample(all_wordpool_indexes, num_of_words * num_of_attempts)
    except:
        print(f'Insufficient words in word pool! {num_of_words*num_of_attempts} words required, but only {len(wordpool_dict)} words exist. Please edit the word pool or settings.')
        print(f'Terminating program...')
        exit()
        
    # Add the words with the random indexes from the previous part into a 2D list
    buffer = 0
    for i in range(num_of_attempts):
        for j in range(num_of_words):
            session_word_list[i].append(list(wordpool_dict.keys())[word_indexes[buffer+j]])          # Appends the words with the random index to each list in session_word_list 
        buffer += int(num_of_words)     # add buffer for index to generate words for next attempt 
    return session_word_list

def hangmanart(num_of_incorrect):
    """Prints hangman ascii art depending on the number of incorrectly guessed letters

    Args:
        num_of_incorrect (int): Integer stating number of incorrectly guessed letters

    Returns:
        str: Hangman ascii art
    """    
    match num_of_incorrect:
        case 0:
            return '   _____\n  |     |\n  |      \n  |      \n  |\n  |\n _|_\n|   |_______\n|           |\n|___________|'
        case 1:
            return '   _____\n  |     |\n  |     o\n  |     |\n  |\n  |\n _|_\n|   |_______\n|           |\n|___________|'
        case 2:
            return '   _____\n  |     |\n  |     o\n  |    /|\n  |\n _|_\n|   |_______\n|           |\n|___________|'
        case 3:
            return '   _____\n  |     |\n  |     o\n  |    /|\\\n  |\n  |\n _|_\n|   |_______\n|           |\n|___________|'
        case 4:
            return '   _____\n  |     |\n  |     o\n  |    /|\\\n  |    /\n  |\n _|_\n|   |_______\n|           |\n|___________|'
        case 5:
            return '   _____\n  |     |\n  |     o\n  |    /|\\\n  |    / \\\n  |\n _|_\n|   |_______\n|           |\n|___________|'

def generatelogentry():
    """Generates the log entry for the session and adds it to game_logs.json
    """    
    log_entry = {}                                      # Create blank log entry 
    time_since_epoch = int(time.time())                 # Calculates the time since epoch in seconds. This will be used as the dictionary key of the entry.
    enddate = datetime.now().strftime('%d-%m-%Y %H:%M')    # Find current date and time
    log_entry["Start Date"] = startdate
    log_entry["End Date"] = enddate
    log_entry["Player"] = username
    log_entry["Score"] = points
    log_entry["Difficulty"] = word_difficulty
    with open(directory + 'storage\\game_logs.json', 'r') as game_logs:
        game_logs_dict = json.load(game_logs)
        game_logs_dict[time_since_epoch] = log_entry
    with open(directory + 'storage\\game_logs.json', 'w') as game_logs:
        game_logs.write(json.dumps(game_logs_dict, indent = 4))

def displaytopplayers():
    """Displays top players based on number of top players specific in settings
    """    
    with open(directory + 'storage\\game_logs.json', 'r') as game_logs:
        game_logs_dict = json.load(game_logs)
    with open(directory + 'storage\\settings.json', 'r') as settings:
        num_of_top_players = json.load(settings)["number of top players"]

    # Find top player
    print(f'\nTop {num_of_top_players} players are:')
    for i in range(num_of_top_players):
        logs_highest_score = -1     
        logs_highest_player = 'No Player'   
        for log in game_logs_dict:
            if game_logs_dict[log]["Score"] > logs_highest_score:
                highscorer_key = log
                logs_highest_score = game_logs_dict[log]["Score"]
                logs_highest_player = game_logs_dict[log]["Player"]

        # If there are no players left in dict        
        if logs_highest_score == -1:
            logs_highest_score = 'N/A'

        # Display top players    
        print(f'{i+1}. {logs_highest_player} ({logs_highest_score} pts)')

        # Remove already listed top player
        if len(game_logs_dict) > 0:
            game_logs_dict.pop(highscorer_key)

def picklifeline():
    """Allows user to pick one lifeline between show all vowels and show definition
    """    
    lifeline = input('\nPick a lifeline:\n1. Show all vowels\n2. Show definition\n>> ')
    validinput = False
    while validinput == False:
        # For vowel lifeline
        if lifeline == '1':
            validinput = True
            print(f'You picked: Show all vowels.\n4 points have been deducted.')
            global correct_letters, correct_letters_display, lifeline_vowels, num_of_correct_letters
            lifeline_vowels = 0
            correct_letters_display = ''            
            for l in range(len(word)):             
                if 'a' == word[l] and correct_letters[l] != 'a':               
                    correct_letters[l] = 'a'   
                    num_of_correct_letters += 1
                    lifeline_vowels += 1
                elif 'e'== word[l] and correct_letters[l] != 'e':
                    correct_letters[l] = 'e'
                    num_of_correct_letters += 1
                    lifeline_vowels += 1
                elif 'i'== word[l] and correct_letters[l] != 'i':
                    correct_letters[l] = 'i'
                    num_of_correct_letters += 1
                    lifeline_vowels += 1
                elif 'o'== word[l] and correct_letters[l] != 'o':
                    correct_letters[l] = 'o'
                    num_of_correct_letters += 1
                    lifeline_vowels += 1
                elif 'u'== word[l] and correct_letters[l] != 'u':
                    correct_letters[l] = 'u' 
                    num_of_correct_letters += 1
                    lifeline_vowels += 1   
                correct_letters_display += correct_letters[l] 
            return
        # For definition lifeline
        elif lifeline == '2':
            validinput = True
            print(f'You picked: Show definition\n4 points have been deducted.')
            print(f'Definition is: {wordpool_dict[word]}')
            return
        else:
            validinput = False
            lifeline = input('Please enter a valid input\n>> ')


playerlogin()
mainmenu()