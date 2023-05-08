"""
Main Menu

Student ID: p2227168
Name:       Andrew Poh
Class:      DISM/FT/1B/01
Assessment: CA1-2

Script Name:
    menu.py

Purpose:
    Displays main menu to allow user to select 1. Scan network, 2. Upload/download file using FTP, 3. Send custom packet or 4. Quit

Usage syntax:
    Run with play button / command line, e.g. py menu.py

Input file:
    None

Output file:
    None

Python ver:
    Python 3

Reference:
    None

Library/Module:
    Install tabulate package - pip install tabulate
    Install nmap package - pip install python-nmap
    Install pyftpdlib package - pip install pyftpdlib
    Install scapy package - pip install scapy
"""
import nmap_scanner, ftp_client, custom_packet
menu_input = 0
while menu_input != '4':
    print('\n**PSEC Info Security Apps**\n1. Scan network\n2. Upload/download file using FTP\n3. Send custom packet\n4. Quit')
    menu_input = input('>> ')
    while menu_input != '1' and menu_input != '2' and menu_input != '3' and menu_input != '4':
        print('Please enter a valid input.')
        menu_input = input('>> ')
    match(menu_input):
        case '1':
            nmap_scanner.scan()
        case '2':
            ftp_client.client()
        case '3':
            custom_packet.print_custom_menu()
        case '4':
            print('Goodbye!')