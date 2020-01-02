import mysql.connector
import mysql.connector.errors
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog


mydb=mysql.connector.connect(host="localhost",user="root",passwd="teqhub",charset="utf8")
if mydb.is_connected():
    print("connected")
else:
    print("fail!!!")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists bank")
mycursor.execute("use bank")
mycursor.execute("create table if not exists bank_master(ACCOUNT_NO char(16) primary key,NAME varchar(30),CITY char(60),MOBILE_NO char(10),BALANCE int(16))")
mycursor.execute("create table if not exists banktrans(ACCOUNT_NO char (16),AMOUNT int(16),DATE_Txn date ,Txn_type char(100),foreign key (ACCOUNT_NO) references bank_master(ACCOUNT_NO))")
mydb.commit()

window = Tk()
window.geometry("900x600")
window.title("**ABHISHEK PROJECT**")
#============= global variable for  entries===========
#========CreateAcc variable========
accountVar = StringVar()
nameVar = StringVar()
cityVar=StringVar()
mobileVar=StringVar()
dateVar=StringVar()
amountVar=StringVar()

#==========function to remove all widget
def remove_all_widgets():
    global window
    for widget in window.winfo_children():
        widget.grid_remove()
        
def CreateAc():   
        global accountVar
        global nameVar,cityVar,mobileVar
        
        
        remove_all_widgets()
        reset()
        titleLabel = Label(window,text="ABHI BANK(CREATING A/c)",font="Arial 30",fg="orange")
        titleLabel.grid(row=0,column=2,columnspan=3,pady=(10,0))


        itemLabel = Label(window, text="All information prompted are mandatory to be filled",fg="red")
        itemLabel.grid(row=3,column=2,padx=(50,0),columnspan=2, pady=10)
        
        acnoLabel = Label(window, text="ACCOUNT NUMBER")
        acnoLabel.grid(row=4, column=2,padx=20,pady=5)
        acnoEntry= Entry(window, textvariable=accountVar)
        acnoEntry.grid(row=4, column=3,padx=20,pady=5)

      
        nameLabel = Label(window, text="NAME")
        nameLabel.grid(row=5, column=2,padx=20,pady=5)
        nameEntry= Entry(window, textvariable=nameVar)
        nameEntry.grid(row=5, column=3,padx=20,pady=5)
        
    
        cityLabel = Label(window, text="CITY")
        cityLabel.grid(row=6, column=2,padx=20,pady=5)
        cityEntry= Entry(window, textvariable=cityVar)
        cityEntry.grid(row=6, column=3,padx=20,pady=5)


        mobileLabel = Label(window, text="MOBILE NUMBER")
        mobileLabel.grid(row=7, column=2,padx=20,pady=5)
        mobileEntry= Entry(window, textvariable=mobileVar)
        mobileEntry.grid(row=7, column=3,padx=20,pady=5)
        addNewCust = Button(window, text="Add Customer", width=15, height=2, command=lambda: CreateAcSubmit())
        addNewCust.grid(row=9, column=3, padx=(10,0),pady=(10,0))
        Backmain_menu(10,3)

def CreateAcSubmit():
        balance=0
        acno=accountVar.get()
        name=nameVar.get()
        city=cityVar.get()
        mn=mobileVar.get()
        mycursor.execute("insert into bank_master values('"+acno+"','"+name+"','"+city+"','"+mn+"','"+str(balance)+"')")
        mydb.commit()
        messagebox.showinfo("Welcome", "Account created successfully")

def DepositMoney():
        global dateVar,amountVar,accountVar
        remove_all_widgets()
        reset()
        titleLabel = Label(window,text="   ABHI BANK(DEPOSIT MONEY)",font="Arial 30",fg="orange")
        titleLabel.grid(row=0,column=2,columnspan=3,pady=(10,0))


        itemLabel = Label(window, text="All information prompted are mandatory to be filled",fg="red")
        itemLabel.grid(row=3,column=2,padx=(50,0),columnspan=2, pady=10)

        
        acnoLabel = Label(window, text="ACCOUNT NUMBER")
        acnoLabel.grid(row=4, column=2,padx=20,pady=5)
        acnoEntry= Entry(window, textvariable=accountVar)
        acnoEntry.grid(row=4, column=3,padx=20,pady=5)
        
        
        depositLabel = Label(window, text="AMOUNT TO DEPOSIT")
        depositLabel.grid(row=5, column=2,padx=20,pady=5)
        depositEntry= Entry(window, textvariable=amountVar)
        depositEntry.grid(row=5, column=3,padx=20,pady=5)
        
        
        dateLabel = Label(window, text="Date(YYYY-MM-DD)")
        dateLabel.grid(row=6, column=2,padx=20,pady=5)
        dateEntry= Entry(window, textvariable=dateVar)
        dateEntry.grid(row=6, column=3,padx=20,pady=5)
        btnsubmit= Button(window, text="SUBMIT", width=15, height=2, command=lambda: depositsubmit())
        btnsubmit.grid(row=7, column=3, padx=(10,0),pady=(10,0))
        Backmain_menu(8,3)
        
def depositsubmit():
        ttype="d"
        acno=accountVar.get()
        dp=amountVar.get()
        dot=dateVar.get()
        mycursor.execute("insert into banktrans values('"+acno+"','"+str(dp)+"','"+dot+"','"+ttype+"')")
        mycursor.execute("update bank_master set balance=balance+'"+str(dp)+"' where ACCOUNT_NO='"+acno+"'")
        mydb.commit()
        messagebox.showinfo("Welcome","**"+dp+"Rupees has been deposited successully**")

def WithdrawMoney():
        global dateVar,amountVar,accountVar
        remove_all_widgets()
        reset()
        
        titleLabel = Label(window,text="   ABHI BANK(WITHDRAW MONEY)",font="Arial 30",fg="orange")
        titleLabel.grid(row=0,column=2,columnspan=3,pady=(10,0))


        itemLabel = Label(window, text="All information prompted are mandatory to be filled",fg="red")
        itemLabel.grid(row=3,column=2,padx=(50,0),columnspan=2, pady=10)

        
        acnoLabel = Label(window, text="ACCOUNT NUMBER")
        acnoLabel.grid(row=4, column=2,padx=20,pady=5)
        acnoEntry= Entry(window, textvariable=accountVar)
        acnoEntry.grid(row=4, column=3,padx=20,pady=5)
        
        
        withdrawLabel = Label(window, text="AMOUNT TO WITHDRAW")
        withdrawLabel.grid(row=5, column=2,padx=20,pady=5)
        withdrawEntry= Entry(window, textvariable=amountVar)
        withdrawEntry.grid(row=5, column=3,padx=20,pady=5)
        
        
        dateLabel = Label(window, text="Date(YYYY-MM-DD)")
        dateLabel.grid(row=6, column=2,padx=20,pady=5)
        dateEntry= Entry(window, textvariable=dateVar)
        dateEntry.grid(row=6, column=3,padx=20,pady=5)
        btnsubmit= Button(window, text="SUBMIT", width=15, height=2, command=lambda: withdrawsubmit())
        btnsubmit.grid(row=9, column=3, padx=(10,0),pady=(10,0))
        Backmain_menu(10,3)
        
def withdrawsubmit():
            ttype="w"
            acno=accountVar.get()
            wd=amountVar.get()
            dot=dateVar.get()
            mycursor.execute("insert into banktrans values('"+acno+"','"+str(wd)+"','"+dot+"','"+ttype+"')")
            mycursor.execute("update bank_master set balance=balance-'"+str(wd)+"' where ACCOUNT_NO='"+acno+"'")
            mydb.commit()
            messagebox.showinfo("Welcome ", "**"+wd+" Rupees has been withdrawn successully**")

def Display():
        remove_all_widgets()
        reset()
        titleLabel = Label(window,text="ABHI BANK(DISPLAY DETAILS)",font="Arial 30",fg="orange")
        titleLabel.grid(row=0,column=2,columnspan=3,pady=(10,0))


        itemLabel = Label(window, text="All information prompted are mandatory to be filled",fg="red")
        itemLabel.grid(row=3,column=2,padx=(50,0),columnspan=2, pady=10)
        acnoLabel = Label(window, text="account number:")
        acnoLabel.grid(row=4, column=2,padx=20,pady=5)
        acnoEntry= Entry(window, textvariable=accountVar)
        acnoEntry.grid(row=4, column=3,padx=20,pady=5)
        btnSubmit = Button(window, text="Submit", width=15, height=2, command=lambda: DisplaySubmit())
        btnSubmit.grid(row=5, column=3, padx=(10,0),pady=(10,0))
        Backmain_menu(6,3)
def DisplaySubmit():        
        userDetailField=["Account Number","Name","City","Mobile","Amount"]
        acno=accountVar.get()
        mycursor.execute("select * from bank_master where ACCOUNT_NO='"+acno+"'")
        
        f=0      
        for row in mycursor:
            for data in row:
                field=Label(window,text=userDetailField[f]+":       "+str(data))
                field.grid(row=f+7, column=2,padx=20,pady=5)
                f=f+1
                      
def reset():
    accountVar.set("")
    amountVar.set("")
    dateVar.set("")
def Backmain_menu(r,c):
    btnBack = Button(window, text="Back Main Menu", width=15, height=2, command=lambda: mainwindow())
    btnBack.grid(row=r, column=c, padx=(10,0),pady=(10,0))
    
    
def mainwindow():
    global itemVariable
    remove_all_widgets()
    titleLabel = Label(window,text="ABHI BANK",font="Arial 30",fg="orange")
    titleLabel.grid(row=0,column=1,columnspan=3,pady=(10,0))

    itemLabel = Label(window, text="Select Item")
    itemLabel.grid(row=1, column=2, padx=(5,0),pady=(10,0))
    btnCreate = Button(window, text="Create account", width=15, height=2, command=lambda: CreateAc())
    btnCreate.grid(row=2, column=2, padx=(10,0),pady=(10,0))
    btnDiposit = Button(window, text="Deposit money", width=15, height=2,command=lambda: DepositMoney())
    btnDiposit.grid(row=3, column=2, padx=(10,0), pady=(10,0))

    btnWithdraw= Button(window, text="Withdraw money", width=15, height=2,command=lambda:WithdrawMoney())
    btnWithdraw.grid(row=4, column=2, padx=(10,0), pady=(10,0))

    btnExit = Button(window, text = "Display A/C Detail",width=15, height=2,command=lambda:Display())
    btnExit.grid(row=5, column=2,pady=(10,0))
mainwindow()
window.mainloop()



