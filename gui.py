import tkinter
import tkcalendar
tk = tkinter.Tk()
tk.geometry("630x500")
tk.title("MEDICAL DATA DOWNLOAD")
tk.configure(bg="#b1c2de")
tkinter.Label(tk, text="Username").place(relx=0.4,rely=0.05,anchor=tkinter.CENTER)
e1 = tkinter.Entry(tk).place(relx=0.6,rely=0.05,anchor=tkinter.CENTER)

tkinter.Label(tk, text="Password").place(relx=0.4,rely=0.1,anchor=tkinter.CENTER)
e2 = tkinter.Entry(tk).place(relx=0.6,rely=0.1,anchor=tkinter.CENTER)
tkinter.Frame(tk,bg="lightgrey",width=550,height=270).place(relx=0.5,rely=0.42,anchor=tkinter.CENTER)
tkinter.Label(tk, text="Start Date",bg="lightgrey").place(relx=0.3,rely=0.18,anchor=tkinter.CENTER)
cal = tkcalendar.Calendar(master=tk).place(relx=0.3,rely=0.4,anchor=tkinter.CENTER)
tkinter.Label(tk, text="Start Time",bg="lightgrey").place(relx=0.2,rely=0.65,anchor=tkinter.CENTER)
st1 = tkinter.Entry(tk,width=3).place(relx=0.3,rely=0.65,anchor=tkinter.CENTER)
tkinter.Label(tk, text=":",bg="lightgrey").place(relx=0.35,rely=0.65,anchor=tkinter.CENTER)
st2 = tkinter.Entry(tk,width=3).place(relx=0.4,rely=0.65,anchor=tkinter.CENTER)


tkinter.Label(tk, text="End Date",bg="lightgrey").place(relx=0.7,rely=0.18,anchor=tkinter.CENTER)
cal2 = tkcalendar.Calendar(master=tk).place(relx=0.7,rely=0.4,anchor=tkinter.CENTER)
tkinter.Label(tk, text="End Time",bg="lightgrey").place(relx=0.6,rely=0.65,anchor=tkinter.CENTER)
et1 = tkinter.Entry(tk,width=3).place(relx=0.7,rely=0.65,anchor=tkinter.CENTER)
tkinter.Label(tk, text=":",bg="lightgrey").place(relx=0.75,rely=0.65,anchor=tkinter.CENTER)
et2 = tkinter.Entry(tk,width=3).place(relx=0.8,rely=0.65,anchor=tkinter.CENTER)


butt = tkinter.Button(tk,text="DOWNLOAD",bg="#5c8db5",width=40,height=5).place(relx=0.5,rely=0.8,anchor=tkinter.CENTER)
tk.mainloop()