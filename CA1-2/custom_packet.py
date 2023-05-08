"""
Custom Packet

Student ID: p2227168
Name:       Andrew Poh
Class:      DISM/FT/1B/01
Assessment: CA1-2

Script Name:
    custom_packet.py

Purpose:
    Creates and sends out custom packet

Usage syntax:
    Run via main menu

Input file:
    None

Output file:
    None

Python ver:
    Python 3

Reference:
    None

Library/Module:
    Install scapy package - pip install scapy
"""
from scapy.all import send, IP, TCP, ICMP, UDP   
# srp and sr1 is for layer 2, send for layer 3

import re

def send_packet(src_addr:str , src_port:int , dest_addr:str, 
                 dest_port:int, pkt_type:str, pkt_data:str)  -> bool:
  """Create and send a packet based on the provided parameters

  Args:
      src_addr(str) : Source IP address
      src_port(int) : Source Port
      dest_addr(str): Destination IP address
      dest_port(int): Destination Port
      pkt_type(str) : Type of packet (T)TCP, (U)UDP, (I)ICMP echo request. Note it is case sensitive
      pkt_data(str) : Data in the packet
  Returns:
      bool: True if send successfull, False otherwise
  """    

  if pkt_type == "T":
    pkt = IP(dst=dest_addr,src=src_addr)/TCP(dport=dest_port,sport=src_port)/pkt_data
  elif  pkt_type == "U":
    pkt = IP(dst=dest_addr,src=src_addr)/UDP(dport=dest_port,sport=src_port)/pkt_data
  else:
    pkt = IP(dst=dest_addr,src=src_addr)/ICMP()/pkt_data
  try:
    send(pkt ,verbose = False)   # Hide "Send 1 packets" message on console
    return True
  except:
    return False
        
def print_custom_menu():
  """Obtain inputs to create custom packet

  Returns: Nil
  """    
  print("************************")
  print("* Custom Packet        *")
  print("************************\n")

  # validate URL (assuming URL is always www.[name].com)
  valid_input = False
  while valid_input != True:
    src_addr = input("Enter Source address of Packet: ")
    x = re.fullmatch(r'^(www\.)([a-zA-Z0-9-._]*)(\.com|\.org|\.sg)$', src_addr)
    if x:
        valid_input = True
    else:
        print('Invalid URL.')

  # validate number between 0 and 65535 DONE
  valid_input = False
  while valid_input != True:
    try:
        src_port = int(input("Enter Source Port of Packet: "))
        if src_port > 0 and src_port <= 65535:
            valid_input = True
        else:
          raise Exception  
    except:
        print('Invalid port number.')
    
  # validate URL (assuming URL is always www.[name].com)
  valid_input = False
  while valid_input != True:
    dest_addr = input("Enter Destination address of Packet: ")
    x = re.fullmatch(r'^(www\.)([a-zA-Z0-9-._]*)(\.com|\.org|\.sg)$', dest_addr)
    if x:
        valid_input = True
    else:
        print('Invalid URL.')

  # validate number between 0 and 65535 DONE
  valid_input = False
  while valid_input != True:
    try:
        dest_port= int(input("Enter Destination Port of Packet: "))
        if dest_port > 0 and dest_port <= 65535:
          valid_input = True
        else:
          raise Exception  
    except:
        print('Invalid port number.')

  # validate T U or I DONE
  valid_input = False
  while valid_input == False:
    # pkt_type = input("Enter Type (T) TCP, (U) UDP, (I) ICMP echo request (T/U/I): ")
    pkt_type = 'T'
    if pkt_type == 'T' or pkt_type == 'U' or pkt_type == 'I':
        valid_input = True
    else:
        print('Invalid packet type.')

  if pkt_type == "I":
    print("  Note: Port number for ICMP will be ignored")
        
  # no need validate DONE
  pkt_data = input("Packet RAW Data (optional, DISM-DISM-DISM-DISM left blank): ")
  if pkt_data == "":
    pkt_data = "DISM-DISM-DISM-DISM"
    
  # validate number between 1 and 65535 DONE
    valid_input = False
    while valid_input != True:
        try:
            pkt_count = int(input("No of Packet to send (1-65535): " ))
            if pkt_count > 0 and pkt_count <= 65535:
                valid_input = True
            else:
                raise Exception  
        except:
            print('Invalid input. No. of packets must be between 1 and 65535.')

  # validate Y or y DONE
    start_now = input("Enter Y to Start, Any other return to main menu: ")
    if start_now != 'Y' and start_now != 'y': 
        print('Packet aborted.')
        return

  # send the packets
  try:
    count = 0
    for i in range(pkt_count):
        if send_packet(src_addr, src_port, dest_addr, dest_port, pkt_type, pkt_data):
            count  = count + 1
    print(count , " packet(s) sent" )
  except:
    print('illegal IP address')
    return

# print_custom_menu()