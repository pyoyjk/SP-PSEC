"""
FTP Client

Student ID: p2227168
Name:       Andrew Poh
Class:      DISM/FT/1B/01
Assessment: CA1-2

Script Name:
    ftp_server.py

Purpose:
    Used to access ftp_server

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
    None
"""
# Ref: https://pythonspot.com/ftp-client-in-python/

def client():
    """Runs client program
    
    Returns: NIL
    """    
    import ftplib, os, pathlib
    pwd = str(pathlib.Path(__file__).parent.resolve()) + '\\'
    ftp = ftplib.FTP()
    try:
        ftp.connect('localhost', 2121)
    except:
        print('Server not running.')
        return
    ftp.login()

    # download file to folder ftpClientData
    def getFile(ftp, filename):
        try:
            ftp.retrbinary("RETR " + filename, open('ftpClientData\\' + filename, 'wb').write)
            return(True)
        except:
            return(False)

    # upload file from folder ftpClientData
    def uploadFile(ftp, filename):
        try:
            ftp.storbinary("STOR " + filename, open('ftpClientData\\' + filename, 'rb'))
            return(True)
        except:
            return(False)

    # option to download/upload
    valid_input = False
    while valid_input == False:
        ftp_menu_input = input('\nSelect an option: \n1. Download file \n2. Upload file \n3. Exit \n>> ')

        if ftp_menu_input == '1':
            # file input
            file_download = input('Enter file to download: ')
            # download the file
            if (getFile(ftp,file_download)):
                print(f'Downloaded file: {file_download}')
            else:
                print(f'Error in downloading: {file_download}')
                os.remove(pwd + f'ftpClientData\\{file_download}')
            valid_input = True

        elif ftp_menu_input == '2':
            # file input
            file_upload = input('Enter file to upload: ')
            # upload the file
            if (uploadFile(ftp,file_upload)):
                print(f'Uploaded file: {file_upload}')
            else:
                print(f'Error in uploading: {file_upload}')
            valid_input = True

        elif ftp_menu_input == '3':
            print('Exiting...')
            valid_input = True

        else: 
            print('Invalid input.')
            
    ftp.quit()

# client()