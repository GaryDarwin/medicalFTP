#importing required libraries
from dataclasses import dataclass
import ftplib
from datetime import datetime
import argparse

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
    startRange = input("Enter Starting Date (DD/MM/YYYY):")
    startTime = input("Enter Starting Time (HH:MM):")
    start_point = startRange + startTime
    endRange = input("Enter Ending Date (DD/MM/YYYY):")
    endTime = input("Enter Ending Time (HH:MM):")
    end_point = endRange + endTime

    selected_start_point = datetime.strptime(start_point, "%d/%m/%Y%H:%M")
    selected_end_point = datetime.strptime(end_point, "%d/%m/%Y%H:%M")
    print (selected_start_point)
    print (selected_end_point)

    files = ftp_get(ftp,selected_start_point,selected_end_point)
    #ADD DATA VALIDATION

    for file in files:
        ftp_download(file)
    

def ftp_get(ftp,selected_start_point,selected_end_point):
    data=[]
    range=False
    ftp.dir(data.append)
    files = []
    for line in data:
        temp=line.split("DATA_")[1].split(".")[0]
        temp = datetime.strptime(temp,"%Y%m%d%H%M%S")
        if range==True:
            files.append(line.split(" ")[-1])
    return files

def ftp_download(ftp, file):
    handle = open(file, 'wb')
    ftp.retrbinary('RETR %s' % file, handle.write)
    ftp.cwd("/")


def ftp_quit(ftp):
    ftp.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-g','--get', type=str, nargs=2, metavar=('Date', 'Time'), required=False, help="Download specific file")
    parser.add_argument('-f','--files', type=str, nargs=4, metavar=('Start date' ,'Start time' ,'End date' ,'End time'), required=False, help="Get file names in datetime range")
    parser.add_argument('-d','--download', type=str, nargs=4, metavar=('Start date' ,'Start time' ,'End date' ,'End time'), required=False, help="Download files in datetime range")

    args = parser.parse_args()
    
    if args.get is not None:
        try:
            ftp = ftp_connect()
        except:
            print("issue connecting to server")
        try:
            date,time = args.get
            file = date + ' ' + time
            ftp_download(ftp,file)
        except:
            print("issue downloading files")
        ftp_quit(ftp)
    
    elif args.files is not None:
        try:
            ftp = ftp_connect()
        except:
            print("issue connecting to server")
        startd, startt, endd, endt = args.files
        start = startd + ' ' + startt
        end = endd + ' ' + endt
        try:
            files = ftp_get(ftp, start, end)
            if len(files)==0:
                print("no files found")
            for file in files:
                print(file)
        except:
            print("issue downloading files")
        ftp_quit(ftp)
    
    elif args.download is not None:
        try:
            ftp = ftp_connect()
        except:
            print("issue connecting to server")
        startd, startt, endd, endt = args.download
        start = startd + ' ' + startt
        end = endd + ' ' + endt
        try:
            files = ftp_get(ftp, start, end)
            for file in files:
                ftp_download(ftp,file)
        except:
            print("issue downloading files")
        ftp_quit(ftp)
    
    else:
        try:
            ftp = ftp_connect()
        except:
            print("issue connecting to server")
        try:
            ftp_browse(ftp)
        except:
            print("issue downloading files")
        ftp_quit(ftp)
    
    #ftp = ftp_connect()
    #ftp_browse(ftp)
    #ftp_quit(ftp)
