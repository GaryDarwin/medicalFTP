from email import message
from turtle import title


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
tk.iconbitmap("icon.ico")
tk.geometry("630x510")
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
#st1 = tkinter.Entry(tk,width=3)
#h2 = tkinter.StringVar(tk)
st1 = ttk.Combobox(tk, values=[str(i).zfill(2) for i in list(range(24))],width=2)
st1.place(relx=0.3,rely=0.65,anchor=tkinter.CENTER)
tkinter.Label(tk, text=":",bg="lightgrey").place(relx=0.35,rely=0.65,anchor=tkinter.CENTER)
#st2 = tkinter.Entry(tk,width=3)
#m2 = tkinter.StringVar(tk)
st2 = ttk.Combobox(tk, values=[str(i).zfill(2) for i in list(range(60))],width=2)
st2.place(relx=0.4,rely=0.65,anchor=tkinter.CENTER)


tkinter.Label(tk, text="End Date",bg="lightgrey").place(relx=0.7,rely=0.18,anchor=tkinter.CENTER)
cal2 = tkcalendar.Calendar(master=tk)
cal2.place(relx=0.7,rely=0.4,anchor=tkinter.CENTER)
tkinter.Label(tk, text="End Time",bg="lightgrey").place(relx=0.6,rely=0.65,anchor=tkinter.CENTER)
et1 = ttk.Combobox(tk, values=[str(i).zfill(2) for i in list(range(24))],width=2)
et1.place(relx=0.7,rely=0.65,anchor=tkinter.CENTER)
tkinter.Label(tk, text=":",bg="lightgrey").place(relx=0.75,rely=0.65,anchor=tkinter.CENTER)
et2 = ttk.Combobox(tk, values=[str(i).zfill(2) for i in list(range(60))],width=2)
et2.place(relx=0.8,rely=0.65,anchor=tkinter.CENTER)
#functon for FTP connection
def ftp_connect(userN,passwd):
    try:
        #local ip address used for model
        ftp_inp = "127.0.0.1"
        ftp = ftplib.FTP(ftp_inp)

        #login to FTP server
        ftp.login(user=userN, passwd=passwd)
        return ftp
    except:
        tkinter.messagebox.showerror(title="FTP Test", message="The FTP server is either Unavailable or Incorrect Credentials were provided...")
        return
    
def ftp_browse(ftp,selected_start_point,selected_end_point):
    try:
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
                tkinter.messagebox.showerror(title="Date Selection", message="The selected date is out of range. Try again...")

    except:
        tkinter.messagebox.showerror(title="FTP Browse Error", message="There was an unexpected problem browsing the FTP server. Please try again later...")
    
def ftp_download(ftp,file):
    print(file)
    handle = open(os.path.dirname(__file__)+"/"+file, 'wb')
    ftp.retrbinary('RETR %s' % file, handle.write)
    handle.close()
    valid.data_validation(os.path.dirname(__file__)+"/"+file)
    if not headercheck.check_headers(os.path.dirname(__file__)+"/"+file):
        print("Bad headers")
        tkinter.messagebox.showinfo(title="File Header", message="File(s) Downloaded but ... the selected file/ files contain bad headers...")
        
    
def ftp_quit(ftp):
    ftp.quit()

def run():
    ftp=ftp_connect(e1.get(),e2.get())
    try:
        print(cal.get_date()+"|"+st1.get()+":"+st2.get())
        std = datetime.strptime(st1.get()+":"+st2.get(),"%H:%M")
        etd = datetime.strptime(et1.get()+":"+et2.get(),"%H:%M")
        calg = cal.selection_get()
        calg2 = cal2.selection_get()
        ftp_browse(ftp,datetime(calg.year, calg.month, calg.day)+timedelta(hours=std.hour,minutes=std.minute),datetime(calg2.year, calg2.month, calg2.day)+timedelta(hours=etd.hour,minutes=etd.minute))
    except:
        print ('Error, time and date incorrect format')
        tkinter.messagebox.showinfo(title="Formatting", message="The provided date/time formatting is invalid...")
    ftp_quit(ftp)

def testftp():
    ftp=ftp_connect(e1.get(),e2.get())
    if ftp == None :
        print ('Aknowledged Fail')
    elif ftp != None:
        tkinter.messagebox.showinfo(title="FTP Test", message="Successful FTP Connection Established...")
        ftp_quit(ftp)

butt = tkinter.Button(tk,text="DOWNLOAD",bg="#5c8db5",width=40,height=4,command=run).place(relx=0.5,rely=0.8,anchor=tkinter.CENTER)
butt2 = tkinter.Button(tk,text="Test FTP Connection",bg="#bbf99e",width=40,height=2,command=testftp).place(relx=0.5,rely=0.95,anchor=tkinter.CENTER)

tk.mainloop()