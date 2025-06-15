from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
import os

root=Tk()
root.title("Login System")
root.geometry("1350x700+0+0")
root.config(bg="white")

# ==============image====================
menulogo_path = "C:\\Users\\sai\\Desktop\\IMS\\login.jpg"
menulogo = Image.open(menulogo_path)
menulogo = menulogo.resize((500, 500), Image.ADAPTIVE)
menulogo = ImageTk.PhotoImage(menulogo)

label_menulogo = Label(root, image=menulogo,borderwidth=0)
label_menulogo.place(x=200, y=50)


# =========Vaiables====================

var_username=StringVar()
var_password=StringVar()

# ==============Login Frame===================
login_frame=Frame(root,relief=RAISED,bg="white")
login_frame.place(x=650,y=90,width=350,height=460)

# =============================================================================
# Label
title=Label(login_frame,text="Login System",font=("elephant",30,"bold"),fg="black",bg="white")
title.place(x=40,y=30)
# Username
lbl_username=Label(login_frame,text="Employee ID",font=("Andalus",15),fg="black",bg="White")
lbl_username.place(x=60,y=100)

txt_username=Entry(login_frame,textvariable=var_username,font=("times new roman",15),bg="lightyellow")
txt_username.place(x=60,y=140,width=250)

# password
lbl_password=Label(login_frame,text="Password",font=("Andalus",15),fg="black",bg="White")
lbl_password.place(x=60,y=190)

txt_password=Entry(login_frame,textvariable=var_password,show="*",font=("times new roman",15),bg="lightyellow")
txt_password.place(x=60,y=230,width=250)

# ===============================================================================


def login():
    conn=sqlite3.connect("IMS.db")
    cur=conn.cursor()
    try:
        if var_username.get()=="" and var_password.get()=="":
            messagebox.showerror("Error","All Fields are required")
        else:
           cur.execute("select utype from employee where eid=? AND pass=?",(var_username.get(),var_password.get()))
           user=cur.fetchone()

           if user==None:
               messagebox.showerror("Error","Invalid Employee ID/Password")
           else:
            #    print(user)
               if user[0]=='Admin':
                   root.destroy()
                   os.system("python project.py")
               else:
                   root.destroy()
                   os.system("python Billing.py")
               
    except :
        conn.close()


# ===============================================================================

# Button
btn_login=Button(login_frame,text= "Log In",command=login,font=("Arial",15,"bold"),bg="blue"
                 ,activebackground= "grey",fg="white",activeforeground="white",cursor="hand2")
btn_login.place(x=60,y=300,width=250,height=35)
 
# Horizontal Line
hr=Label(login_frame,bg="black")
hr.place(x=60,y=370,width=250,height=2)

or_=Label(login_frame,text="OR",font=("times new roman",15,"bold"),bg="white")
or_.place(x=170,y=355)

# Forget Password
btn_forget=Button(login_frame,text="Forget Password?",font=("arial",13),bg="White",fg="blue",bd=0,
                  activebackground="white",activeforeground= "Black")
btn_forget.place(x=120,y=390)




root.mainloop()