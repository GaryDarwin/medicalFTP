#importing required libraries
from dataclasses import dataclass
import ftplib
from datetime import datetime

#functon for FTP connection
def ftp_connect():
    #user input for server IP address
    ftp_inp = input("Enter the IP address of the FTP Server: \n")
    #ftp = ftplib.FTP("127.0.0.1:21")
    ftp = ftplib.FTP(ftp_inp)

    userN = input("Enter username:\n")
    passwd = input("Enter password:\n")
    #login to FTP server
    ftp.login(user=userN, passwd=passwd)
    return ftp

def ftp_browse(ftp):
    #print(ftp.getwelcome())
    #print(ftp.pwd())
    startRange = input("Enter starting date (DD/MM/YYYY): ")
    startTime = input("Enter starting time (HH:MM): ")
    endRange = input("Enter ending date (DD/MM/YYYY): ")
    endTime = input("Enter starting time (HH:MM): ")
    #ADD DATA VALIDATION

    data=[]
    range=False
    ftp.dir(data.append)
    for line in data:
        temp= line.split("DATA_")[1].split(".")[0]
        temp = datetime.strptime(temp,"%Y%m%d%H%M%S")
        print(temp)
        if range==True:
            ftp_download(line.split(" ")[-1])
def ftp_download(file):
    handle = open(file, 'wb')
    ftp.retrbinary('RETR %s' % file, handle.write)
    ftp.cwd("../")

    

def ftp_quit(ftp):
    ftp.quit()

ftp = ftp_connect()
ftp_browse(ftp)
ftp_quit(ftp)