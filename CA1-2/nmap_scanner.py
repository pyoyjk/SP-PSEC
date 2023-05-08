"""
Nmap Scanner

Student ID: p2227168
Name:       Andrew Poh
Class:      DISM/FT/1B/01
Assessment: CA1-2

Script Name:
    nmap_scanner.py

Purpose:
    Scans top 10 TCP and UDP ports of localhost and nmap.scanme.org with OS and version detection, Script scanning, traceroute

Usage syntax:
    Run via main menu (option 1)

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
"""
import tabulate
import nmap

def scan():
    # initialize the port scanner
    nmScan = nmap.PortScanner()

    # specify scan IP and options
    IP = 'localhost scanme.nmap.org'
    options = '-O -sV -sC --traceroute -sTU -T5 --top-ports 5'
    print(f'Target IP       : {IP}')

    # perform the scan and return it in 'results'
    results = nmScan.scan(hosts=IP , arguments=options)

    # creating table headers for each column
    table = [ ['host','hostname','protocol','port ID','state','product','extrainfo','reason','cpe'] ]

    # creating list of protocols to loop through when printing
    protocol_list = ['tcp','udp']

    # create table
    for host in results['scan']:
        hostname = results['scan'][host]['hostnames'][0]['name']
        for protocol in protocol_list:
            for port,info in results['scan'][host][protocol].items():
                tmp = [host, hostname, protocol, port, info['state'] , info['product'] , info['extrainfo'] , info['reason'] , info['cpe']]
                table.append(tmp)

    # print table
    print(tabulate.tabulate(table, tablefmt='simple_grid'))

# scan()