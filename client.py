import ftplib

ftp = ftplib.FTP("127.0.0.1")
ftp.login()

print(ftp.getwelcome())
print(ftp.pwd())
ftp.dir()
handle = open("medicaldata.csv", 'wb')
ftp.retrbinary('RETR %s' % "medicaldata.csv", handle.write)
ftp.cwd("/")
ftp.quit()
