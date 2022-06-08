from msilib.schema import Font
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import datetime as dt
from turtle import back
# from tkcalendar import DateEntry,Calender
root=Tk()
root.geometry("1860x900")
root.resizable(True, True)

root.title("TALLY PRIME")


curnt_period = Label(root, text="CURRENT PERIOD",fg="darkblue").place(x=40, y=30)
curnt_date = Label(root, text="CURRENT DATE",fg="darkblue").place(x=340, y=30)
prd = Label(root, text="1-Apr-22 to 31-March-2023", fg="black").place(x=40, y=60)
date = Label(root, text="Friday, 1-Apr-2022", fg="black").place(x=340, y=60)
cmpny = Label(root, text="Name Of Company",borderwidth=3,fg="darkblue").place(x=40, y=100)
lst_entry = Label(root, text="Date Of Last Entry", fg="darkblue").place(x=340, y=100)
cpny = Label(root, text="ABC Pvt ltd", fg="black").place(x=40, y=140)
date_entry = Label(root, text="1-Apr-22",fg="black").place(x=340, y=140)
separator = ttk.Separator(root,orient='vertical')
separator.place(relx=0.47,rely=0,relwidth=0.2,relheight=1)
frame = Label(root, text="Accounts Book",bg="grey",fg="white",width=40,padx=20,pady=10).place(x=740, y=110)
frame1 = Frame(root, bg="lightblue", width=305, height=540)
frame1.place(x=740, y=145)
frame2 = Frame(frame1, bg="lightblue", width=305, height=540)
frame2.pack(pady=10, padx=10)
mstrs = Label(root, text="Summary",bg="lightblue",fg="black",font="17").place(x=850,y=190)


def func1():
    screen1 = Toplevel(root)
    screen1.title('create')
    screen1.geometry('1860x900') 

def func3():     
    global screen2
    screen2 = Toplevel(root)
    screen2.resizable(False, False)
    screen2.title('CONTRA REGISTER')
    screen2.geometry('1500x770')
    sbmibtn13 = Button(screen2, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen2, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen2, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen2, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen2, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen2, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
   
    sbmibtn = Button(screen2, text='APRIL',command=create57,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=170)
    sbmibtn2 = Button(screen2, text='MAY',command=create58,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=200)
    sbmibtn3 = Button(screen2, text='JUNE',command=create59,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=230)
    sbmibtn4 = Button(screen2, text='JULY', command=create60, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=260)
    sbmibtn5 = Button(screen2, text='AUGUST',command=create61,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=290)
    sbmibtn6 = Button(screen2, text='SEPTEMBER',command=create62,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=320)
    sbmibtn7 = Button(screen2, text='OCTOBER',command=create63,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=350)
    sbmibtn8 = Button(screen2, text='NOVEMBER', command=create64, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=380)
    sbmibtn9 = Button(screen2, text='DECEMBER',command=create65,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=410)
    sbmibtn10 = Button(screen2, text='JANUARY',command=create66,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=440)
    sbmibtn11 = Button(screen2, text='FEBRUARY',command=create67,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=470)
    sbmibtn12 = Button(screen2, text='MARCH', command=create68, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=500)
    frame4 = Frame(screen2, bg="lightblue", width=180, height=790)
    frame4.place(x=1400, y=0)
    date = Button(frame4, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame4, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame4, command='screen1.destroy', text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700)
    Label(screen2, text='CONTRA REGISTER',bg="lightblue",font='17',fg="black",width=430).pack() 
    Label(screen2, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()

    
    
def func4():
    global screen2
    screen2 = Toplevel(root)
    screen2.resizable(False, False)
    screen2.title('payment register')
    screen2.geometry('1500x770')
    sbmibtn13 = Button(screen2, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen2, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen2, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen2, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen2, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen2, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    
    sbmibtn = Button(screen2, text='APRIL',command=create69,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=170)
    sbmibtn2 = Button(screen2, text='MAY',command=create70,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=200)
    sbmibtn3 = Button(screen2, text='JUNE',command=create71,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=230)
    sbmibtn4 = Button(screen2, text='JULY', command=create72, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=260)
    sbmibtn5 = Button(screen2, text='AUGUST',command=create73,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=290)
    sbmibtn6 = Button(screen2, text='SEPTEMBER',command=create74,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=320)
    sbmibtn7 = Button(screen2, text='OCTOBER',command=create75,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=350)
    sbmibtn8 = Button(screen2, text='NOVEMBER', command=create76, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=380)
    sbmibtn9 = Button(screen2, text='DECEMBER',command=create77,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=410)
    sbmibtn10 = Button(screen2, text='JANUARY',command=create78,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=440)
    sbmibtn11 = Button(screen2, text='FEBRUARY',command=create79,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=470)
    sbmibtn12 = Button(screen2, text='MARCH', command=create80, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=500)
    
    frame5 = Frame(screen2, bg="lightblue", width=180, height=790)
    frame5.place(x=1400, y=0)
    date = Button(frame5, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame5, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame5, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700)
    Label(screen2, text='PAYMENT REGISTER',bg="lightblue",font='17',fg="black",width=430).pack()  
    Label(screen2, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()
def func5():
    global screen2
    screen2 = Toplevel(root)
    screen2.resizable(False, False)
    screen2.title('receipt register')
    screen2.geometry('1500x770')
    sbmibtn13 = Button(screen2, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen2, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen2, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen2, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen2, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen2, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)

    sbmibtn = Button(screen2, text='APRIL',command=create81,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=170)
    sbmibtn2 = Button(screen2, text='MAY',command=create82,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=200)
    sbmibtn3 = Button(screen2, text='JUNE',command=create83,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=230)
    sbmibtn4 = Button(screen2, text='JULY', command=create84, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=260)
    sbmibtn5 = Button(screen2, text='AUGUST',command=create85,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=290)
    sbmibtn6 = Button(screen2, text='SEPTEMBER',command=create86,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=320)
    sbmibtn7 = Button(screen2, text='OCTOBER',command=create87,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=350)
    sbmibtn8 = Button(screen2, text='NOVEMBER', command=create88, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=380)
    sbmibtn9 = Button(screen2, text='DECEMBER',command=create89,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=410)
    sbmibtn10 = Button(screen2, text='JANUARY',command=create90,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=440)
    sbmibtn11 = Button(screen2, text='FEBRUARY',command=create91,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=470)
    sbmibtn12 = Button(screen2, text='MARCH', command=create92, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=500)
    frame6 = Frame(screen2, bg="lightblue", width=180, height=790)
    frame6.place(x=1400, y=0)
    date = Button(frame6, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame6, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame6, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700)
    Label(screen2, text='RECEIPT REGISTER',bg="lightblue",font='17',fg="black",width=430).pack()  
    Label(screen2, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()    
def func6():     
    global screen2
    screen2 = Toplevel(root)
    screen2.resizable(False, False)
    screen2.title('sales register')
    screen2.geometry('1500x770')
    sbmibtn13 = Button(screen2, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen2, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen2, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen2, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen2, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen2, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)


    sbmibtn = Button(screen2, text='APRIL',command=create93,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=170)
    sbmibtn2 = Button(screen2, text='MAY',command=create94,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=200)
    sbmibtn3 = Button(screen2, text='JUNE',command=create95,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=230)
    sbmibtn4 = Button(screen2, text='JULY', command=create96, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=260)
    sbmibtn5 = Button(screen2, text='AUGUST',command=create97,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=290)
    sbmibtn6 = Button(screen2, text='SEPTEMBER',command=create98,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=320)
    sbmibtn7 = Button(screen2, text='OCTOBER',command=create99,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=350)
    sbmibtn8 = Button(screen2, text='NOVEMBER', command=create100, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=380)
    sbmibtn9 = Button(screen2, text='DECEMBER',command=create101,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=410)
    sbmibtn10 = Button(screen2, text='JANUARY',command=create102,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=440)
    sbmibtn11 = Button(screen2, text='FEBRUARY',command=create103,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=470)
    sbmibtn12 = Button(screen2, text='MARCH', command=create104, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=500)
    frame7 = Frame(screen2, bg="lightblue", width=180, height=790)
    frame7.place(x=1400, y=0)
    date = Button(frame7, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame7, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame7, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700)
    Label(screen2, text='SALES REGISTER',bg="lightblue",font='17',fg="black",width=430).pack()  
    Label(screen2, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()
def func7():
    global screen2
    screen2 = Toplevel(root)
    screen2.resizable(False, False)
    screen2.title('purchase register')
    screen2.geometry('1500x770')
    sbmibtn13 = Button(screen2, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen2, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen2, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen2, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen2, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen2, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)


    sbmibtn = Button(screen2, text='APRIL',command=create105,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=170)
    sbmibtn2 = Button(screen2, text='MAY',command=create106,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=200)
    sbmibtn3 = Button(screen2, text='JUNE',command=create107,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=230)
    sbmibtn4 = Button(screen2, text='JULY', command=create108, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=260)
    sbmibtn5 = Button(screen2, text='AUGUST',command=create109,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=290)
    sbmibtn6 = Button(screen2, text='SEPTEMBER',command=create110,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=320)
    sbmibtn7 = Button(screen2, text='OCTOBER',command=create111,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=350)
    sbmibtn8 = Button(screen2, text='NOVEMBER', command=create112, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=380)
    sbmibtn9 = Button(screen2, text='DECEMBER',command=create113,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=410)
    sbmibtn10 = Button(screen2, text='JANUARY',command=create114,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=440)
    sbmibtn11 = Button(screen2, text='FEBRUARY',command=create115,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=470)
    sbmibtn12 = Button(screen2, text='MARCH', command=create116, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=500)
    frame8 = Frame(screen2, bg="lightblue", width=180, height=790)
    frame8.place(x=1400, y=0)
    date = Button(frame8, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame8, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame8, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700)
    Label(screen2, text='PURCHASE REGISTER',bg="lightblue",font='17',fg="black",width=430).pack()  
    Label(screen2, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()
def func8():
    global screen2
    screen2 = Toplevel(root)
    screen2.resizable(False, False)
    screen2.title('journal register')
    screen2.geometry('1500x770')
    sbmibtn13 = Button(screen2, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen2, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen2, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen2, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen2, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen2, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)

    sbmibtn = Button(screen2, text='APRIL',command=create117,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=170)
    sbmibtn2 = Button(screen2, text='MAY',command=create118,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=200)
    sbmibtn3 = Button(screen2, text='JUNE',command=create119,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=230)
    sbmibtn4 = Button(screen2, text='JULY', command=create120, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=260)
    sbmibtn5 = Button(screen2, text='AUGUST',command=create121,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=290)
    sbmibtn6 = Button(screen2, text='SEPTEMBER',command=create122,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=320)
    sbmibtn7 = Button(screen2, text='OCTOBER',command=create123,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=350)
    sbmibtn8 = Button(screen2, text='NOVEMBER', command=create124, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=380)
    sbmibtn9 = Button(screen2, text='DECEMBER',command=create125,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=410)
    sbmibtn10 = Button(screen2, text='JANUARY',command=create126,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=440)
    sbmibtn11 = Button(screen2, text='FEBRUARY',command=create127,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=470)
    sbmibtn12 = Button(screen2, text='MARCH', command=create128, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=500)
    frame9 = Frame(screen2, bg="lightblue", width=180, height=790)
    frame9.place(x=1400, y=0)
    date = Button(frame9, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame9, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame9, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700)
    Label(screen2, text='JOURNAL REGISTER',bg="lightblue",font='17',fg="black",width=430).pack()  
    Label(screen2, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()    
def func9():
    global screen2
    screen2 = Toplevel(root)
    screen2.resizable(False, False)
    screen2.title('debit note register')
    screen2.geometry('1500x770')
    sbmibtn13 = Button(screen2, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen2, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen2, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen2, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen2, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen2, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)


    sbmibtn = Button(screen2, text='APRIL',command=create129,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=170)
    sbmibtn2 = Button(screen2, text='MAY',command=create130,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=200)
    sbmibtn3 = Button(screen2, text='JUNE',command=create131,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=230)
    sbmibtn4 = Button(screen2, text='JULY', command=create132, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=260)
    sbmibtn5 = Button(screen2, text='AUGUST',command=create133,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=290)
    sbmibtn6 = Button(screen2, text='SEPTEMBER',command=create134,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=320)
    sbmibtn7 = Button(screen2, text='OCTOBER',command=create135,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=350)
    sbmibtn8 = Button(screen2, text='NOVEMBER', command=create136, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=380)
    sbmibtn9 = Button(screen2, text='DECEMBER',command=create137,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=410)
    sbmibtn10 = Button(screen2, text='JANUARY',command=create138,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=440)
    sbmibtn11 = Button(screen2, text='FEBRUARY',command=create139,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=470)
    sbmibtn12 = Button(screen2, text='MARCH', command=create140, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=500)
    frame10 = Frame(screen2, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700)
    Label(screen2, text='DEBIT NOTE REGISTER',bg="lightblue",font='17',fg="black",width=430).pack()  
    Label(screen2, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()
def func10():
    global screen2
    screen2 = Toplevel(root)
    screen2.resizable(False, False)
    screen2.title('credit note register')
    screen2.geometry('1500x770')
    sbmibtn13 = Button(screen2, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen2, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen2, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen2, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen2, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen2, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)


    sbmibtn = Button(screen2, text='APRIL',command=create141,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=170)
    sbmibtn2 = Button(screen2, text='MAY',command=create142,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=200)
    sbmibtn3 = Button(screen2, text='JUNE',command=create143,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=230)
    sbmibtn4 = Button(screen2, text='JULY', command=create144, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=260)
    sbmibtn5 = Button(screen2, text='AUGUST',command=create145,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=290)
    sbmibtn6 = Button(screen2, text='SEPTEMBER',command=create146,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=320)
    sbmibtn7 = Button(screen2, text='OCTOBER',command=create147,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=350)
    sbmibtn8 = Button(screen2, text='NOVEMBER', command=create148, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=380)
    sbmibtn9 = Button(screen2, text='DECEMBER',command=create149,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=410)
    sbmibtn10 = Button(screen2, text='JANUARY',command=create150,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=440)
    sbmibtn11 = Button(screen2, text='FEBRUARY',command=create151,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(y=470)
    sbmibtn12 = Button(screen2, text='MARCH', command=create152, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(y=500)
    frame11 = Frame(screen2, bg="lightblue", width=180, height=790)
    frame11.place(x=1400, y=0)
    date = Button(frame11, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame11, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame11, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700)
    Label(screen2, text='CREDIT NOTE REGISTER',bg="lightblue",font='17',fg="black",width=430).pack()  
    Label(screen2, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()      
def func11():
    global screen2
    screen2 = Toplevel(root)
    screen2.resizable(False, False)
    screen2.title('CASH / BANK SUMMARY')
    screen2.geometry('1500x770') 
    sbmibtn13 = Button(screen2, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen2, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen2, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen2, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen2, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen2, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
 
    frame12 = Frame(screen2, bg="lightblue", width=180, height=790)
    frame12.place(x=1400, y=0)
    date = Button(frame12, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame12, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60) 
    back = Button(frame12, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen2, text='CASH/BANK SUMMARY',bg="lightblue",font='17',fg="black",width=430).pack()  
    Label(screen2, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()

def func12():
    global screen2
    screen2 = Toplevel(root)
    screen2.resizable(False, False)
    screen2.title('LEDGER')
    screen2.geometry('1500x770')
    frame131 = Frame(screen2, bg="lightblue", width=250, height=600)
    frame131.place(x=650, y=0)
    frame131 = Label(screen2, text="LIST OF LEDGERS",bg="black",fg="white",width=32,padx=10,pady=10).place(x=650, y=20)
    frame13 = Frame(screen2, bg="lightblue", width=180, height=790)
    frame13.place(x=1400, y=0)
    date = Button(frame13, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame13, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame13, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700)
    sbmibtn = Button(screen2, text='Create',command=create8,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=170)
    sbmibtn = Button(screen2, text='Cash',command=create8,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665, 
    y=200)
    sbmibtn = Button(screen2, text='Profit & loss A/C',command=create8,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=220)
    e11 = Entry(screen2,).place(x=710, y=100)
    Label(screen2, text='LEDGER',bg="lightblue",font='17',fg="black",width=430).pack() 

    
def func13():
    global screen2
    screen2 = Toplevel(root)
    screen2.resizable(False, False)
    screen2.title('GROUP SUMMARY')
    screen2.geometry('1500x770') 
    frame141 = Frame(screen2, bg="lightblue", width=250, height=600)
    frame141.place(x=650, y=0)
    frame141 = Label(screen2, text="LIST OF GROUPS",bg="black",fg="white",width=32,padx=10,pady=10).place(x=650, y=20)   
    frame14 = Frame(screen2, bg="lightblue", width=180, height=790)
    frame14.place(x=1400, y=0)
    date = Button(frame14, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame14, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame14, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700)

    sbmibtn = Button(screen2, text='Primary',command=create9,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=100)
    sbmibtn = Button(screen2, text='Bank Accounts',command=create10,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=120)
    sbmibtn = Button(screen2, text='Bank OCC A/c',command=create11,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=140)
    sbmibtn = Button(screen2, text='Bank OD A/c',command=create12,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=160)
    sbmibtn = Button(screen2, text='Branch /Divisions',command=create13,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=180)
    sbmibtn = Button(screen2, text='Capital Account',command=create14,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=200)
    sbmibtn = Button(screen2, text='Cash in Hand ',command=create15,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=220)
    sbmibtn = Button(screen2, text='Current Assets',command=create16,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=240)
    sbmibtn = Button(screen2, text='Current Liabilities',command=create17,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=260)
    sbmibtn = Button(screen2, text='Deposits (Assets)',command=create18,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=280)
    sbmibtn = Button(screen2, text='Direct Expenses',command=create19,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=300)
    sbmibtn = Button(screen2, text='Direct Incomes',command=create20,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=320)
    sbmibtn = Button(screen2, text='Duties and Taxes',command=create21,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=340)
    sbmibtn = Button(screen2, text='Expenses(Direct)',command=create22,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=360)
    sbmibtn = Button(screen2, text='Expenses(Indirect)',command=create23,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=380)
    sbmibtn = Button(screen2, text='Fixed Assets',command=create24,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=400)
    sbmibtn = Button(screen2, text='Income(Direct)',command=create25,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=420)
    sbmibtn = Button(screen2, text='Income (Indirect)',command=create26,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=440)
    sbmibtn = Button(screen2, text='Indirect Expenses',command=create27,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=460)
    sbmibtn = Button(screen2, text='Indirect Incomes',command=create28,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=480)
    sbmibtn = Button(screen2, text='Investments',command=create29,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=500)
    sbmibtn = Button(screen2, text='Loans and Advances(Assets)',command=create30,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=520)
    sbmibtn = Button(screen2, text='Loans (Liability)',command=create31,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=540)
    sbmibtn = Button(screen2, text='Misc. Expenses(ASSET)',command=create32,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=560  )
    Label(screen2, text='GROUP SUMMARY',bg="lightblue",font='17',fg="black",width=430).pack()    
def func14():
    global screen2
    screen2 = Toplevel(root)
    screen2.resizable(False, False)
    screen2.title('GROUP VOUCHERS')
    screen2.geometry('1500x770') 

    frame151 = Frame(screen2, bg="lightblue", width=250, height=600)
    frame151.place(x=650, y=0)
    frame151 = Label(screen2, text="LIST OF GROUPS",bg="black",fg="white",width=32,padx=10,pady=10).place(x=650, y=20)
    frame15 = Frame(screen2, bg="lightblue", width=180, height=790)
    frame15.place(x=1400, y=0)
    date = Button(frame15, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame15, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame15, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700)  
    sbmibtn = Button(screen2, text='Primary',command=create33,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=100)
    sbmibtn = Button(screen2, text='Bank Accounts',command=create34,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=120)
    sbmibtn = Button(screen2, text='Bank OCC A/c',command=create35,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=140)
    sbmibtn = Button(screen2, text='Bank OD A/c',command=create36,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=160)
    sbmibtn = Button(screen2, text='Branch /Divisions',command=create37,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=180)
    sbmibtn = Button(screen2, text='Capital Account',command=create38,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=200)
    sbmibtn = Button(screen2, text='Cash in Hand ',command=create39,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=220)
    sbmibtn = Button(screen2, text='Current Assets',command=create40,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=240)
    sbmibtn = Button(screen2, text='Current Liabilities',command=create41,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=260)
    sbmibtn = Button(screen2, text='Deposits (Assets)',command=create42,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=280)
    sbmibtn = Button(screen2, text='Direct Expenses',command=create43,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=300)
    sbmibtn = Button(screen2, text='Direct Incomes',command=create44,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=320)
    sbmibtn = Button(screen2, text='Duties and Taxes',command=create45,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=340)
    sbmibtn = Button(screen2, text='Expenses(Direct)',command=create46,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=360)
    sbmibtn = Button(screen2, text='Expenses(Indirect)',command=create47,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=380)
    sbmibtn = Button(screen2, text='Fixed Assets',command=create48,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=400)
    sbmibtn = Button(screen2, text='Income(Direct)',command=create49,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=420)
    sbmibtn = Button(screen2, text='Income (Indirect)',command=create50,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=440)
    sbmibtn = Button(screen2, text='Indirect Expenses',command=create51,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=460)
    sbmibtn = Button(screen2, text='Indirect Incomes',command=create52,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=480)
    sbmibtn = Button(screen2, text='Investments',command=create53,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=500)
    sbmibtn = Button(screen2, text='Loans and Advances(Assets)',command=create54,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=520)
    sbmibtn = Button(screen2, text='Loans (Liability)',command=create55,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=540)
    sbmibtn = Button(screen2, text='Misc. Expenses(ASSET)',command=create56,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=665,y=560  )
    Label(screen2, text='GROUP VOUCHER',bg="lightblue",font='17',fg="black",width=430).pack()   
def func15():
    global screen2
    screen2 = Toplevel(root)
    screen2.resizable(False, False)
    screen2.title('QUIT')
    screen2.geometry('1500x770')  
    frame151 = Frame(screen2, bg="lightblue", width=250, height=400)
    frame151.place(x=650, y=0)
    frame151 = Label(screen2, text="ARE YOU SURE WANT TO QUIT? ?",bg="black",fg="white",width=32,padx=10,pady=10).place(x=650, y=20) 
    b131 = Button(screen2, text="YES", fg="black", activebackground="palegreen",
             bg="white", width=20, height=1, command=func15).place(x=697, y=200)
    b1311 = Button(screen2, text="NO", fg="black", activebackground="palegreen",
             bg="white", width=20, height=1, command=func15).place(x=697, y=240)     




b1 = Button(root, text="Cash/Bank Book(s)", fg="black", activebackground="palegreen",
            bg="white", width=20, height=1, command=func11).place(x=830, y=230)

b2 = Button(root, text="Ledger", fg="black", activebackground="palegreen",
            bg="white", width=20, height=1, command=func12).place(x=830, y=260)
b3 = Button(root, text="Group summary", fg="black", activebackground="palegreen",
            bg="white", width=20, height=1, command=func13).place(x=830, y=290)
b4 = Button(root, text="Group Vouchers",fg="black", activebackground="palegreen",
            bg="white", width=20, height=1, command=func14).place(x=830, y=320)
mstrs1 = Label(root, text="Registers",bg="lightblue",fg="black",font="13").place(x=850,y=355)

b6 = Button(root, text="ConTra Register", fg="black", activebackground="palegreen",
            bg="white", width=20, height=1, command=func3).place(x=830, y=390)
b7 = Button(root, text="Payment Register", fg="black", activebackground="palegreen",
            bg="white", width=20, height=1, command=func4).place(x=830, y=420)


b8 = Button(root, text="Reciept Register", fg="black", activebackground="palegreen",
            bg="white", width=20, height=1, command=func5).place(x=830, y=450)
b9 = Button(root, text="Sales Register", fg="black", activebackground="palegreen",
            bg="white", width=20, height=1, command=func6).place(x=830, y=500)
b10 = Button(root, text="Purchase Register", fg="black", activebackground="palegreen",
            bg="white", width=20, height=1, command=func7).place(x=830, y=530)

b10 = Button(root, text="Journal Register", fg="black", activebackground="palegreen",
            bg="white", width=20, height=1, command=func8).place(x=830, y=580)
b11 = Button(root, text="Debit Note Register", fg="black", activebackground="palegreen",
             bg="white", width=20, height=1, command=func9).place(x=830, y=610)

b12 = Button(root, text="Credit Note Register", fg="black", activebackground="palegreen",
             bg="white", width=20, height=1, command=func10).place(x=830, y=640)

             
b13 = Button(root, text="Quit", fg="black", activebackground="palegreen",
             bg="white", width=20, height=1, command=func15).place(x=830, y=670)           
             
frame3 = Frame(root, bg="lightblue", width=140, height=790)
frame3.place(x=1400, y=0)
date = Button(frame3, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), command=func1, activebackground="palegreen", activeforeground="red")
date.place(x=13, y=20)


def func2():
    global screen2
    screen2 = Toplevel(root)
    screen2.resizable(False, False)
    screen2.title('Company')
    screen2.geometry('1500x770')
    Label(screen2, text='List Of Companies',bg="lightblue",font='17',fg="white",width=430).pack()
    sbmibtn = Button(screen2, text='Create Company',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=650,y=40)
    sbmibtn2 = Button(screen2, text='Alter Company',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=650,y=70)
    sbmibtn3 = Button(screen2, text='Select Company',command=create,fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=650,y=100)
    sbmibtn4 = Button(screen2, text='Shut Company', command=create, fg='black',font=('Arial',9),activebackground='palegreen', width=30, border=0).place(x=650, y=130)


def create():
    global screen3
    screen3 = Toplevel(root)
    screen3.resizable(False, False)
    screen3.title('create company')
    screen3.geometry('940x520')
    Label(screen3, text='COMPANY CREATION',bg="lightblue",font='15',fg="white",width=640).pack()
    global  Cname,Cmailing,Caddress, email,state,country,pcode,tphone,mphone,fax,site,symbol,format
    Cname = StringVar()
    Cmailing = StringVar()
    Caddress = StringVar()
    email = StringVar()
    state = StringVar()
    country = StringVar()
    pcode = IntVar()
    tphone = StringVar()
    mphone = StringVar()
    fax = StringVar()
    site = StringVar()
    symbol = StringVar()
    format = StringVar()
    
    
    cname = Label(screen3, text='Company Name:').place(x=20, y=70)
    e1 = Entry(screen3, textvariable=Cname,width=40).place(x=120, y=70)
    y1 = Label(screen3, text='Financial Year begining From:').place(x=450, y=70)
    # e2 = DateEntry(screen3,width=25)
    adrs1 = Label(screen3, text='Mailing Name:').place(x=20, y=110)
    e3 = Entry(screen3, textvariable=Cmailing, width=40).place(x=120, y=110)
    y2 = Label(screen3, text='Books Begining From:').place(x=450, y=110)
    adrs = Label(screen3, text='Address:').place(x=20, y=150)
    e4 = Entry(screen3,textvariable=Caddress,width=40).place(x=120, y=150)

def create1():
    global screen3
    screen3 = Toplevel(root)
    screen3.resizable(False, False)
    screen3.title('VOUCHER REGISTER')
    screen3.geometry('1500x770')
    Label(screen3, text='LIST OF ALL CONTRA VOUCHERS',bg="lightblue",font='15',fg="BLACK",width=640).pack()
def create2():
    global screen3
    screen3 = Toplevel(root)
    screen3.resizable(False, False)
    screen3.title('VOUCHER REGISTER')
    screen3.geometry('1500x770')
    Label(screen3, text='LIST OF ALL PAYMENT VOUCHERS',bg="lightblue",font='15',fg="BLACK",width=640).pack()
def create3():
    global screen3
    screen3 = Toplevel(root)
    screen3.resizable(False, False)
    screen3.title('VOUCHER REGISTER')
    screen3.geometry('1500x770')
    Label(screen3, text='LIST OF ALL RECEIPT VOUCHERS',bg="lightblue",font='15',fg="BLACK",width=640).pack()
def create4():
    global screen3
    screen3 = Toplevel(root)
    screen3.resizable(False, False)
    screen3.title('VOUCHER REGISTER')
    screen3.geometry('1500x770')
    Label(screen3, text='LIST OF ALL SALES VOUCHERS',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
def create5():
    global screen3
    screen3 = Toplevel(root)
    screen3.resizable(False, False)
    screen3.title('VOUCHER REGISTER')
    screen3.geometry('1500x770')
    Label(screen3, text='LIST OF ALL PURCHASE VOUCHERS',bg="lightblue",font='15',fg="BLACK",width=640).pack()
def create6():
    global screen3
    screen3 = Toplevel(root)
    screen3.resizable(False, False)
    screen3.title('VOUCHER REGISTER')
    screen3.geometry('1500x770')
    Label(screen3, text='LIST OF ALL JOURNAL VOUCHERS',bg="lightblue",font='15',fg="BLACK",width=640).pack()    
def create7():
    global screen3
    screen3 = Toplevel(root)
    screen3.resizable(False, False)
    screen3.title('VOUCHER REGISTER')
    screen3.geometry('1500x770')
    Label(screen3, text='LIST OF ALL DEBIT NOTE VOUCHERS',bg="lightblue",font='15',fg="BLACK",width=640).pack()
def create8():
    global screen3
    screen3 = Toplevel(root)
    screen3.resizable(False, False)
    screen3.title('VOUCHER REGISTER')
    screen3.geometry('1500x770')
    Label(screen3, text='LIST OF ALL CREDIT NOTE VOUCHERS',bg="lightblue",font='15',fg="BLACK",width=640).pack()           


def create9():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('primary')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack() 
    
def create10():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('Bank Accounts')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  
    
def create11():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('Bank OCC Accounts')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create12():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('Bank od Accounts')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create13():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('Branch divisions')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create14():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('capital Accounts')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create15():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('cash in hand')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create16():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('Current Assets')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create17():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('Current Liabilities')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create18():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('Deposits')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create19():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('Direct Expenses')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create20():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('Direct Income')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()

def create21():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('Duties and Taxes')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create22():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('Expenses Direct')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9),command=screen4.destroy(), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create23():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('Expenses Indirect')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create24():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('Fixed Asset')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()

def create25():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('income direct')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create26():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('income indirect')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create27():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('indirect expenses')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create28():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('indirect income')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()

def create29():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('investments')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create30():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('loans and advances')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create31():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('loans')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create32():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('misc expenses')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9),command=func2, activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()

def create33():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('Direct Income')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()

def create34():
    global screen4
    screen4 = Toplevel(root)  
    screen4.resizable(False, False)
    screen4.title('Duties and Taxes')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create35():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('Expenses Direct')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create36():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('Expenses Indirect')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create37():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('Fixed Asset')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()

def create38():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('income direct')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create39():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('income indirect')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create40():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('indirect expenses')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create41():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('indirect income')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()

def create42():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('investments')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create43():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('loans and advances')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create44():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('loans')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create45():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('misc expenses')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()

def create46():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('Expenses Direct')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create47():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('Expenses Indirect')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create48():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('Fixed Asset')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()

def create49():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('income direct')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create50():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('income indirect')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create51():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('indirect expenses')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create52():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('indirect income')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()

def create53():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('investments')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create54():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('loans and advances')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create55():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('loans')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create56():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('misc expenses')
    screen4.geometry('1500x770')
    Label(screen4, text='Abc',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  
def create57():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='April',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create58():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='May',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create59():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='June',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()

def create60():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='July',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create61():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='August',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create62():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='September',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create63():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='October',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()

def create64():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='November',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create65():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='December',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create66():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='January',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create67():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='February',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()      
def create68():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='March',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()                  
def create69():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='April',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create70():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='May',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create71():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='June',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()

def create72():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='July',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create73():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='August',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create74():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='September',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create75():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='October',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()

def create76():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='November',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create77():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='December',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create78():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='January',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create79():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='February',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()      
def create80():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='March',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()                  
def create81():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='April',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create82():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='May',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create83():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='June',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()

def create84():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='July',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create85():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='August',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create86():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='September',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create87():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='October',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()

def create88():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='November',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create89():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='December',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create90():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='January',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create91():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='February',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()      
def create92():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='March',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()                  
def create93():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='April',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create94():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='May',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create95():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='June',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()

def create96():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='July',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create97():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='August',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create98():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='September',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create99():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='October',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()

def create100():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='November',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create101():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='December',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create102():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='January',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create103():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='February',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()      
def create104():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='March',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()                  
def create105():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='April',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create106():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='May',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create107():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='June',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()

def create108():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='July',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create109():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='August',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create110():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='September',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create111():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='October',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()

def create112():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='November',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create113():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='December',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create114():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='January',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create115():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='February',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()      
def create116():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='March',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()                  
def create117():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='April',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create118():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='May',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create119():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='June',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()

def create120():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='July',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create121():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='August',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create122():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='September',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create123():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='October',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()

def create124():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='November',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create125():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='December',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create126():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='January',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create127():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='February',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()      
def create128():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='March',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()
def create129():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='April',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create130():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='May',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create131():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='June',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()

def create132():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='July',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create133():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='August',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create134():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='September',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create135():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='October',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()

def create136():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='November',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create137():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='December',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create138():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='January',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create139():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='February',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()      
def create140():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='March',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack() 
def create141():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='April',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create142():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='May',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create143():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='June',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()

def create144():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='July',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create145():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='August',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create146():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='September',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create147():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='October',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()

def create148():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='November',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create149():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='December',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create150():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='January',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()  

def create151():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='February',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()      
def create152():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('registers')
    screen4.geometry('1500x770')
    Label(screen4, text='March',bg="lightblue",font='15',fg="BLACK",width=640).pack() 
    sbmibtn13 = Button(screen4, text='Cash',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=50)
    sbmibtn14 = Button(screen4, text='Abc Pvt Ltd',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=70)
    sbmibtn15 = Button(screen4, text='For 1-April-22',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1200, y=90)
    sbmibtn16 = Button(screen4, text='Transactions',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1030, y=110)
    sbmibtn16 = Button(screen4, text='Credit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=1100, y=130)
    sbmibtn16 = Button(screen4, text='Debit',fg='black',font=('Arial',9),activebackground='palegreen',width=30,border=0).place(x=950, y=130)
    frame10 = Frame(screen4, bg="lightblue", width=180, height=790)
    frame10.place(x=1400, y=0)
    date = Button(frame10, text="Date", width=14, fg="black", font=(
    "timesnewroman",9), activebackground="palegreen", activeforeground="red")
    date.place(x=8, y=25)
    company = Button(frame10, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=60)
    back = Button(frame10, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=700) 
    Label(screen4, text='PARTICULAR').place(x=20, y=70)(font="timesnewroman").pack()       


company = Button(frame3, text="Company", width=14, fg="black", font=(
    "timesnewroman", 9), command=func2, activebackground="palegreen", activeforeground="red").place(x=13, y=50)
back = Button(frame3, text="back", width=14, fg="black", font=(
    "timesnewroman", 9), activebackground="palegreen", activeforeground="red").place(x=8, y=750)    
root.mainloop()

