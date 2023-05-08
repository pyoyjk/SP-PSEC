"""
Main Hangman Program

Student ID: p2227168
Name:       Andrew Dillon Poh Jie Hao
Class:      DISM/FT/1B/01
Assessment: CA1-1

Script name:
    reset.py

Purpose: 
    Resets all other input/output files for CA1 purposes
    
Usage Syntax: 
    Run with play button

Input Files:
•	Reset File: D:\psec\reset.json

Output Files:
•	Simple Words: D:\psec\wordpool(simple).json
•	Complex Words: D:\psec\wordpool(complex).json
•	Simple Idioms: D:\psec\wordpool(simpleidioms).json
•	Complex Idioms: D:\psec\wordpool(complexidioms).json
•	Settings: D:\psec\settings.json
•	Game Logs: D:\psec\game_logs.json

Python ver:
    Python 3.10

Reference:
    None

Library/Module:
    None

Known Issues:
    None
"""

import pathlib, json
directory = str(pathlib.Path(__file__).parent.resolve()) + '\\'

with open(directory + 'reset.json', 'r') as resetfile:
    print(resetfile)
    reset_dict = json.load(resetfile)
    with open(directory + 'wordpool(simple).json', 'w') as file:
        file.write(json.dumps(reset_dict["wordpool(simple)"], indent = 4))
    with open(directory + 'wordpool(complex).json', 'w') as file:
        file.write(json.dumps(reset_dict["wordpool(complex)"], indent = 4))
    with open(directory + 'wordpool(simpleidioms).json', 'w') as file:
        file.write(json.dumps(reset_dict["wordpool(simpleidioms)"], indent = 4))
    with open(directory + 'wordpool(complexidioms).json', 'w') as file:
        file.write(json.dumps(reset_dict["wordpool(complexidioms)"], indent = 4))
    with open(directory + 'settings.json', 'w') as file:
        file.write(json.dumps(reset_dict["settings"], indent = 4))
    with open(directory + 'game_logs.json', 'w') as file:
        file.write(json.dumps(reset_dict["game_logs"], indent = 4))
    with open(directory + 'adminpassword.txt', 'w') as file:
        file.write(reset_dict["adminpassword"])

print('Reset complete. Ready for CA1.')