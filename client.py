#importing required libraries
import ftplib

#functon for FTP connection
def ftp_connect():
    #user input for server IP address
    ftp_inp = input("Enter the IP address of the FTP Server: \n")
    #ftp = ftplib.FTP("127.0.0.1:21")
    ftp = ftplib.FTP(ftp_inp)

    #login to FTP server
    ftp.login(user='user', passwd='12345')
    return ftp

def ftp_download(ftp):
    #print(ftp.getwelcome())
    #print(ftp.pwd())
    ftp.dir()
    handle = open("medicaldata.csv", 'wb')
    ftp.retrbinary('RETR %s' % "medicaldata.csv", handle.write)
    ftp.cwd("/")

    

def ftp_quit(ftp):
    ftp.quit()

ftp = ftp_connect()
ftp_download(ftp)
ftp_quit(ftp)