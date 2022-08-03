import ftplib

ftp = ftplib.FTP("127.0.0.1")
ftp.login()

print(ftp.getwelcome())
print(ftp.pwd())
ftp.dir()
ftp.cwd("/")
ftp.quit()
