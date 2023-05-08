"""
Main Admin Program

Student ID: p2227168
Name:       Andrew Dillon Poh Jie Hao
Class:      DISM/FT/1B/01
Assessment: CA1-1

Script name:
    admin.py

Purpose: 
    Runs the admin program, allowing admins to edit the wordpool, edit settings, display a report and change admin password.

Usage Syntax: 
    Run with play button

Input Files:
•	Simple Words: D:\psec\wordpool(simple).json
•	Complex Words: D:\psec\wordpool(complex).json
•	Simple Idioms: D:\psec\wordpool(simpleidioms).json
•	Complex Idioms: D:\psec\wordpool(complexidioms).json
•	Settings: D:\psec\settings.json
•	Game Logs: D:\psec\game_logs.json
•	Admin Password: D:\psec\adminpassword.txt

Output Files:
•	Simple Words: D:\psec\wordpool(simple).json
•	Complex Words: D:\psec\wordpool(complex).json
•	Simple Idioms: D:\psec\wordpool(simpleidioms).json
•	Complex Idioms: D:\psec\wordpool(complexidioms).json
•	Settings: D:\psec\settings.json
•	Game Logs: D:\psec\game_logs.json
•	Admin Password: D:\psec\adminpassword.txt

Python ver:
    Python 3.10

Reference:
    None
    
Library/Module:
    None

Known Issues:
    None
"""

import pathlib, json, datetime
directory = str(pathlib.Path(__file__).parent.resolve()) + '\\'

def adminlogin():  
    """Allows user to log in as admin
    """  
    print('Welcome to the admin interface.')
    username = input('Please enter admin username: ')
    if username == 'admin':
        password = input('Please enter password: ')
        with open(directory + 'storage\\adminpassword.txt', 'r') as adminpassword:
            if password == adminpassword.readline():        # if password is correct, continue the subsequent admin program.
                return
            else:
                print('Incorrect password. Terminating program...')
                exit()
    else:
        print(f'{username} is not an administrator. Terminating program...')
        exit()

def adminmenu():
    """Display admin menu
    """ 
    while True:
        menu_input = input(('\nAdmin Configuration Menu\n1. Edit word pool\n2. Edit settings\n3. Edit password\n4. Display report\n5. Exit\n>> '))
        while True:
            match menu_input:
                case '1':
                    editwordpool()
                    break
                case '2':
                    editsettings()
                    break
                case '3':
                    editpassword()
                    break
                case '4':
                    displayreport()
                    break
                case '5':
                    print('Admin session terminated.')
                    exit()
                case _:
                    while menu_input != '1' and menu_input != '2' and menu_input != '3' and menu_input != '4' and menu_input != '5':
                            menu_input = input(('Please enter a number from 1-5.\n>> '))
                
def editwordpool():
    """Display edit word pool options menu
    """  
    file_input = input('\nPick the file to edit:\n1. Simple words\n2. Complex words\n3. Simple idioms\n4. Complex idioms\n5. Back\n>> ')
    invalidinput = True
    global wordpool_file
    while invalidinput == True:
        if file_input == '1':
            wordpool_file = 'storage\\wordpool(simple).json'
            invalidinput = False
        elif file_input == '2':
            wordpool_file = 'storage\\wordpool(complex).json'
            invalidinput = False
        elif file_input == '3':
            wordpool_file = 'storage\\wordpool(simpleidioms).json'
            invalidinput = False
        elif file_input == '4':
            wordpool_file = 'storage\\wordpool(complexidioms).json'
            invalidinput = False
        elif file_input == '5':
            return
        else:
            file_input = input('Please enter a valid input.\n>> ')

    menu_input = input('\nWhat would you like to do?\n1. Add new word\n2. Edit word\n3. Delete word\n4. Recreate word pool\n5. Display words\n6. Back\n>> ')
    while True:
        match menu_input:
            case '1':
                addword()
                return
            case '2':
                editword()
                return
            case '3':
                deleteword()
                return
            case '4':
                recreatewordpool()
                return
            case '5':
                displaywords()
                return
            case '6':
                return
            case _:
                while menu_input != '1' and menu_input != '2' and menu_input != '3' and menu_input != '4' and menu_input != '5' and menu_input != '6':
                    menu_input = input(('Please enter a number from 1-6.\n>> '))
                
def addword():
    """Allows admin to add word with definition to word pool
    """    
    with open(directory + wordpool_file, 'r') as wordpool:
        word_dict = json.load(wordpool)

        # Entering word and definition
        word = input('Enter the word to add (ENTER to cancel): ')
        if word == '':
            return
        if word in word_dict:
            print('Word already exists in word pool.')
            return
        definition = input('Enter a definition for the word: ')

    # Confirmation
    confirm = ''
    while confirm != 'Y' and confirm != 'N':
        confirm = input(f'Word: {word}\nDefinition: {definition}\nConfirm entry? (Y/N)\n>> ').upper()
        if confirm == 'Y':
            word_dict[word] = definition
            with open(directory + wordpool_file, 'w') as wordpool:
                wordpool.write(json.dumps(word_dict, indent = 4))
        elif confirm == 'N':
            return
        else:
            print('Please enter a valid input')

def editword():
    """Allows admin to edit spelling or definition of a word in the word pool
    """   
    with open(directory + wordpool_file, 'r') as wordpool:
        word_dict = json.load(wordpool)
        wordinput = input('Enter the word to edit: ')

        # Edit Spelling or Definition if word exists in dictionary
        if wordinput in word_dict:
            while True:
                spellingordefinition = input(f'What would you like to edit about the word "{wordinput}"? \n1. Spelling \n2. Definition?\n>> ')
                
                # Edit Spelling
                if spellingordefinition == '1': 
                    newspelling = input(f'Enter new spelling for {wordinput}: ')
                    word_dict[newspelling] = word_dict[wordinput]
                    del(word_dict[wordinput])
                    with open(directory + wordpool_file, 'w') as wordpool:
                        wordpool.write(json.dumps(word_dict, indent = 4))
                    return
                
                # Edit Definition
                elif spellingordefinition == '2':
                    newdefinition = input(f'Enter new definition for {wordinput}: ')
                    word_dict[wordinput] = newdefinition
                    with open(directory + wordpool_file, 'w') as wordpool:
                        wordpool.write(json.dumps(word_dict, indent = 4))
                    return

                # Invalid input
                else:
                    print('Please enter a valid input.')

        # Returns if word does not exist
        else:
            print('Word does not exist in word pool.')
            return

def deleteword():
    """Allows admin to delete word in word pool
    """    
    with open(directory + wordpool_file, 'r') as wordpool:
        word_dict = json.load(wordpool)
        wordinput = input('Enter the word to delete: ')
        if wordinput in word_dict:
            word_dict.pop(wordinput)
            with open(directory + wordpool_file, 'w') as wordpool:
                wordpool.write(json.dumps(word_dict, indent = 4))
            print(f'"{wordinput}" has been deleted from word pool')
            return
        else:
            print('Word does not exist in word pool.')
            return

def recreatewordpool():
    """Allows admin to recreate the word pool from scratch
    """    
    wordinput = 'placeholder'
    definitioninput = 'placeholder'
    i = 1
    word_dict = {}

    # Input new words until input = ''
    while wordinput != '':
        wordinput = input(f'Enter word {i} ([ENTER] to quit): ')
        if wordinput == '':
            break
        definitioninput = input(f'Enter definition for {wordinput}: ')
        word_dict[wordinput] = definitioninput
        i += 1
    
    # Displays new word pool
    if len(word_dict) == 0:
        print('Cannot create empty word pool. Exiting process...')
        return
    if wordpool_file == 'storage\\wordpool(simple).json' or wordpool_file == 'storage\\wordpool(complex).json':
        print('New word pool is: \nWord\t\t\tDefinition')
        for word, definition in word_dict.items():  # Calculate number of '\t' based on word length (for formatting)
            if len(word) < 8:
                print(f'{word}\t\t\t{definition}')
            elif len(word) >= 8:
                print(f'{word}\t\t{definition}')
    else:
        for word, definition in word_dict.items():  # Calculate number of '\t' based on word length (for formatting)
            print(f'\nWord: {word}\nDefiniton: {definition}')
    
    # Confirm new word pool
    confirm = ''
    while confirm != 'Y' and confirm != 'N':
        confirm = input('Confirm new word pool? (Y/N) \n>> ').upper()
        if confirm == 'Y':
            with open(directory + wordpool_file, 'w') as wordpool:
                wordpool.write(json.dumps(word_dict, indent = 4))
            print('Word pool has been updated.')
            return
        elif confirm == 'N':
            print('Operation cancelled. Word pool remains unchanged.')
            return
        else:
            print('Please enter a valid input.')

def displaywords():
    """Displays words in word pool
    """   
    with open(directory + wordpool_file, 'r') as wordpool:
        word_dict = json.load(wordpool)
    if wordpool_file == 'storage\\wordpool(simple).json' or wordpool_file == 'storage\\wordpool(complex).json':
        print('New word pool is: \nWord\t\t\tDefinition')
        for word, definition in word_dict.items():  # Calculate number of '\t' based on word length (for formatting)
            if len(word) < 8:
                print(f'{word}\t\t\t{definition}')
            elif len(word) >= 8:
                print(f'{word}\t\t{definition}')
    else:      
        for word, definition in word_dict.items():  # Calculate number of '\t' based on word length (for formatting)
            print(f'\nWord: {word}\nDefiniton: {definition}')

        
def editsettings():
    """Allows admin to change settings
    """    
    with open(directory + 'storage\\settings.json', 'r') as settings:
        settings_dict = json.load(settings)

        # Print Settings menu
        while True:
            print('\nSelect setting to edit:')
            i = 1
            for name, num in settings_dict.items():
                print(f'{i}. {name.capitalize()}: {num}')
                i += 1
            print('4. Back')
            menu_input = ''
            menu_input = input('>> ')

            # Edit individual settings
            if menu_input == '1':
                while True:
                    try:    
                        new_attempts = int(input('Enter new number of attempts: '))
                        if new_attempts < 1:
                            raise Exception
                        else:
                            settings_dict["number of attempts"] = new_attempts
                        break
                    except:
                        print('Please enter a valid integer')
            elif menu_input == '2':
                while True:
                    try:    
                        new_num_of_words = int(input('Enter new number of words: '))
                        if new_num_of_words < 1:
                            raise Exception
                        else:
                            settings_dict["number of words"] = new_num_of_words
                        break
                    except:
                        print('Please enter a valid integer')
            elif menu_input == '3':
                while True:
                    try:    
                        num_of_top_players = int(input('Enter new number of top players: '))
                        if num_of_top_players < 1:
                            raise Exception
                        else:
                            settings_dict["number of top players"] = num_of_top_players
                        break
                    except:
                        print('Please enter a valid integer')
            elif menu_input == '4':     # Rewrites settings.json with updated settings then goes back to menu
                with open(directory + 'storage\\settings.json', 'w') as settings:
                    settings.write(json.dumps(settings_dict, indent = 4))
                return
            else:
                print('Please enter a valid input.')     

def editpassword():
    """Allows admin to change password
    """   
    checkpassword = input('Enter current password (ENTER to cancel): ')
    with open(directory + 'storage\\adminpassword.txt', 'r') as adminpassword:
        if checkpassword == adminpassword.readline():
            passwordinvalid = True

            # Check if new password meets password requirements
            while passwordinvalid:
                newpassword = input('\nPassword must comply with the following:\n • At least one number.\n • At least one uppercase and one lowercase character.\n • At least one of these special symbols (!@#$%).\n • Between 4 to 20 characters long\nEnter new password: ')
                if newpassword == '':
                    print('Operation cancelled.')
                    return
                onenumber, upperletter, lowerletter, specialchar, length = False, False, False, False, False
                for letter in newpassword:
                    if letter.isnumeric():
                        onenumber = True
                    if letter.isupper():
                        upperletter = True
                    if letter.islower():
                        lowerletter = True
                    if letter == '!' or letter == '@' or letter == '#' or letter == '$' or letter == '%':
                        specialchar = True
                if len(newpassword) >= 4 and len(newpassword) <= 20:
                    length = True
                if onenumber and upperletter and lowerletter and specialchar and length:
                    passwordinvalid = False
                else: 
                    print('Password does not meet requirements.')

            # Writes new password into adminpassword.txt
            with open(directory + 'storage\\adminpassword.txt', 'w') as adminpassword:
                adminpassword.write(newpassword)
            print('Password has been changed successfully.')
            return
        elif checkpassword == '':       # Cancel password change
            return
        else:                           # Cancel if password is incorrect
            print('Incorrect password. Returning to admin menu...')
            return

def displayreport():
    """Displays a report of game logs from between specified start and end dates
    """    
    # Input start and end times and converting them to time since epoch
    with open(directory + 'storage\\game_logs.json', 'r') as logs_file:
        logs = json.load(logs_file)
    invalidinput = True
    while invalidinput:
        startdate = input('Enter start date as DD/MM/YYYY ([ENTER] for none): ')
        enddate = input('Enter end date as DD/MM/YYYY ([ENTER] for none): ')
        try:
            if startdate == '':
                start = datetime.datetime(1970, 1, 1)
            else:
                startdate = startdate.split(sep='/')
                start = datetime.datetime(int(startdate[2]), int(startdate[1]), int(startdate[0]))
            if enddate == '':
                end = datetime.datetime(2099, 1, 1)
            else:
                enddate = enddate.split(sep='/')
                end = datetime.datetime(int(enddate[2]), int(enddate[1]), int(enddate[0]))
            invalidinput = False
        except:
            print('Invalid date entered.')
    epoch = datetime.datetime(1970, 1, 1)
    start_time_since_epoch = (start - epoch).total_seconds()
    end_time_since_epoch = (end - epoch).total_seconds()

    # Displaying
    print('Player:\t\tScore:\tDifficulty:\tStart Date: \t   End Date: ')
    exists = False
    for key in list(logs.keys()):
        if start_time_since_epoch < int(key) and end_time_since_epoch > int(key):
            exists = True
            if len(logs[key]["Player"]) < 8:
                print(f'{logs[key]["Player"]}\t\t{logs[key]["Score"]}\t{logs[key]["Difficulty"]}\t{logs[key]["Start Date"]}   {logs[key]["End Date"]}\t')
            else:
                print(f'{logs[key]["Player"]}\t{logs[key]["Score"]}\t{logs[key]["Difficulty"]}\t{logs[key]["Start Date"]}   {logs[key]["End Date"]}\t')
            
    if exists == False:
        print('N/A\t\tN/A\tN/A\t\tN/A.\t\t   N/A')


adminlogin()
adminmenu()