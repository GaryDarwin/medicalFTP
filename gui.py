try:
    import tkinter
    from tkinter import messagebox
    from tkinter import ttk
    import tkcalendar
    #importing required libraries
    from dataclasses import dataclass
    import ftplib
    from datetime import datetime,timedelta
    import os
    import valid
    import headercheck
except:
    print ("Error importing modules. Are all installed?")
    tkinter.messagebox.showerror(title="Module Error", message="Not all required modules/ dependencies are installed. Please ensure all required dependencies are available...")


tk = tkinter.Tk()
#tk.iconbitmap("myIcon.ico")
tk.geometry("630x500")
tk.resizable(False,False)
tk.title("MEDICAL DATA DOWNLOAD")
tk.configure(bg="#b1c2de")
tkinter.Label(tk, text="Username").place(relx=0.4,rely=0.05,anchor=tkinter.CENTER)
e1 = tkinter.Entry(tk)
e1.place(relx=0.6,rely=0.05,anchor=tkinter.CENTER)

tkinter.Label(tk, text="Password").place(relx=0.4,rely=0.1,anchor=tkinter.CENTER)
e2 = tkinter.Entry(tk)
e2.place(relx=0.6,rely=0.1,anchor=tkinter.CENTER)
tkinter.Frame(tk,bg="lightgrey",width=550,height=270).place(relx=0.5,rely=0.42,anchor=tkinter.CENTER)
tkinter.Label(tk, text="Start Date",bg="lightgrey").place(relx=0.3,rely=0.18,anchor=tkinter.CENTER)
cal = tkcalendar.Calendar(master=tk)
cal.place(relx=0.3,rely=0.4,anchor=tkinter.CENTER)
tkinter.Label(tk, text="Start Time",bg="lightgrey").place(relx=0.2,rely=0.65,anchor=tkinter.CENTER)
st1 = tkinter.Entry(tk,width=3)
#h2 = tkinter.StringVar(tk)
#h = ttk.Combobox(tk, values=[i.zfill("2") for i in list(range(24))])
st1.place(relx=0.3,rely=0.65,anchor=tkinter.CENTER)
tkinter.Label(tk, text=":",bg="lightgrey").place(relx=0.35,rely=0.65,anchor=tkinter.CENTER)
st2 = tkinter.Entry(tk,width=3)
#m2 = tkinter.StringVar(tk)
#m = tkinter.OptionMenu(tk, m2, *[i.zfill("2") for i in list(range(60))])
st2.place(relx=0.4,rely=0.65,anchor=tkinter.CENTER)


tkinter.Label(tk, text="End Date",bg="lightgrey").place(relx=0.7,rely=0.18,anchor=tkinter.CENTER)
cal2 = tkcalendar.Calendar(master=tk)
cal2.place(relx=0.7,rely=0.4,anchor=tkinter.CENTER)
tkinter.Label(tk, text="End Time",bg="lightgrey").place(relx=0.6,rely=0.65,anchor=tkinter.CENTER)
et1 = tkinter.Entry(tk,width=3)
et1.place(relx=0.7,rely=0.65,anchor=tkinter.CENTER)
tkinter.Label(tk, text=":",bg="lightgrey").place(relx=0.75,rely=0.65,anchor=tkinter.CENTER)
et2 = tkinter.Entry(tk,width=3)
et2.place(relx=0.8,rely=0.65,anchor=tkinter.CENTER)
#functon for FTP connection
def ftp_connect(userN,passwd):
    #user input for server IP address
    #ftp_inp = input("Enter the IP address of the FTP Server: \n")
    ftp_inp = "127.0.0.1"
    ftp = ftplib.FTP(ftp_inp)

    #login to FTP server
    ftp.login(user=userN, passwd=passwd)
    return ftp
def ftp_browse(ftp,selected_start_point,selected_end_point):
    #print(ftp.getwelcome())
    #print(ftp.pwd())
    '''
    startRange = input("Enter starting date (DD/MM/YYYY): ")
    startTime = input("Enter starting time (HH:MM): ")
    endRange = input("Enter ending date (DD/MM/YYYY): ")
    endTime = input("Enter starting time (HH:MM): ")
    '''
    print(selected_start_point)
    print(selected_end_point)
    #ADD DATA VALIDATION

    data=[]
    ftp.dir(data.append)
    for line in data:
        temp= line.split("DATA_")[1].split(".")[0]
        temp = datetime.strptime(temp,"%Y%m%d%H%M%S")
        if temp>selected_start_point and temp<selected_end_point:
            ftp_download(ftp,line.split(" ")[-1])
        else:
            print("OUT OF RANGE")
def ftp_download(ftp,file):
    print(file)
    handle = open(os.path.dirname(__file__)+"/"+file, 'wb')
    ftp.retrbinary('RETR %s' % file, handle.write)
    handle.close()
    valid.data_validation(os.path.dirname(__file__)+"/"+file)
    if not headercheck.check_headers(os.path.dirname(__file__)+"/"+file):
        print("Bad headers")
    #ftp.cwd("/")
    
def ftp_quit(ftp):
    ftp.quit()
def run():
    ftp=ftp_connect(e1.get(),e2.get())
    print(cal.get_date()+"|"+st1.get()+":"+st2.get())
    std = datetime.strptime(st1.get()+":"+st2.get(),"%H:%M")
    etd = datetime.strptime(et1.get()+":"+et2.get(),"%H:%M")
    calg = cal.selection_get()
    calg2 = cal2.selection_get()
    ftp_browse(ftp,datetime(calg.year, calg.month, calg.day)+timedelta(hours=std.hour,minutes=std.minute),datetime(calg2.year, calg2.month, calg2.day)+timedelta(hours=etd.hour,minutes=etd.minute))
    ftp_quit(ftp)

butt = tkinter.Button(tk,text="DOWNLOAD",bg="#5c8db5",width=40,height=5,command=run).place(relx=0.5,rely=0.8,anchor=tkinter.CENTER)

tk.mainloop()