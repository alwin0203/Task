import tkinter
from tkinter import*
from tkinter import messagebox
from functools import partial
import pymysql
t=tkinter.Tk()
t.geometry('500x500')
t.title("Registration Form")
l=tkinter.Label(t,text="Registration form",fg="blue",width=20,font=("bold",20))
l.place(x=90,y=53)
l_1 = Label(t, text="FullName",width=20,font=("bold", 10))
l_1.place(x=80,y=130)
entry = Entry(t)
entry.place(x=240,y=130)  
l_2 = Label(t, text="Email",width=20,font=("bold", 10))
l_2.place(x=68,y=180)  
entry_1 = Entry(t)
entry_1.place(x=240,y=180)
l_3 = Label(t, text="Age:",width=20,font=("bold", 10))
l_3.place(x=70,y=230)
entry_2 = Entry(t)
entry_2.place(x=240,y=230)

def validateLogin():
    v1=entry.get()
    print("FullName entered :", v1)
    v2=entry_1.get()
    print("Email entered :", v2)
    v3=entry_2.get()
    print("Age entered :", v3)
    db=pymysql.connect(host="localhost",user="root",password="root",database="registrationform")
    cursor=db.cursor()
    #cursor.execute("""create table Registrationss(FullName varchar(40),Email varchar(40),Age integer(40))""")
    print("Table Created")
    FullName=v1
    Email=v2
    Age=v3
    data="""insert into Registrationss values("%s","%s","%s")""" % (FullName,Email,Age)
    
    try:
         cursor.execute(data)
         db.commit()
         print("added registration details successfully")
    except:
        db.rollback()
        print("error")

B=tkinter.Button(t, text='Submit & Print',width=20,bg='brown',fg='white',command=validateLogin).place(x=180,y=380)

t.mainloop()
print("Registration form is created seccussfully...")  
