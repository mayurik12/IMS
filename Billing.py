from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import time
import os
import tempfile

root = Tk()
root.geometry("1350x700+0+0")

# icon = Image.open("C:\\Users\\sai\\Downloads\\icon.png")
# icon_label = Label(image=icon,compound=LEFT)

root.title("Warehouse Stock Management System ")
root.config(bg="White")

title = Label(root,text="Warehouse Stock Management System", font=("times new roman",40,"bold"),
              bg="skyblue",fg="black",anchor="w",padx=20)
title.place(x=0,y=0,relwidth=1,height=70)

cart_list=[]
chk_print=()
# icon_label.pack()
# ====================================================================
# logout
def logout():
    root.destroy()
    os.system("python Login.py")
# ========================================================

# Logout button

btn = Button(root,text="Logout",command=logout,font=("times new roman",15,"bold"),bg="yellow",cursor="hand2")
btn.place(x=1100,y=10,height=50,width=150)

# clock
clock = Label(root,text="Welcome to Warehouse Stock Management System\t\t Date:DD-MM-YYYY\t\t Time:HH:MM:SS",
              font=("times new roman",18),
              bg="grey",fg="white")
clock.place(x=0,y=70,relwidth=1,height=30)
# ===========Variables=================

var_search=StringVar()
var_name=StringVar()
var_contact=StringVar()


var_pid=StringVar()
var_pname=StringVar()
var_qty=StringVar()
var_price=StringVar()
var_status=StringVar()
var_stock=StringVar()

# ===========product Frame=======
productframe1=Frame(root,bd=4,relief=RIDGE,bg="white")
productframe1.place(x=10,y=110,width=410,height=500)

pTitle=Label(productframe1,text="All Products",font=("times new roman",20,"bold"),bg="black",fg="white")
pTitle.pack(side=TOP,fill=X)


# ===================================================================================

def prod_show():
        conn = sqlite3.connect("IMS.db")
        # cur=conn.cursor()
        cursor = conn.cursor()

        try:
           cursor.execute("SELECT pid,name,price,qty,status FROM product")
           rows = cursor.fetchall()
        
        # Assuming Emp1 is a ttk.Treeview widget, you need to replace Emp1 with your actual Treeview widget instance
           product_Table.delete(*product_Table.get_children())

           for row in rows:
            product_Table.insert('', 'end', values=row)

        except Exception as ex:
        #    messagebox.showerror("Error", f"Error due to: {str(ex)}")
        # finally:
           conn.close() 
# =======================================================================
def search():
    conn = sqlite3.connect("IMS.db")
    cursor = conn.cursor()

    try:
        if var_search.get()=="":
            messagebox.showerror("Error","Search input should be required")
        else:
            cursor.execute("SELECT pid,name,price,qty,status FROM product WHERE name LIKE ?", ('%' + var_search.get() + '%',))
            rows = cursor.fetchall()
            if len(rows)!=0:
                product_Table.delete(*product_Table.get_children())
                for row in rows:
                    product_Table.insert('', 'end', values=row)
            else:
                messagebox.showerror("Error","No Record found")

    except Exception as ex:
        messagebox.showerror("Error", f"Error due to: {str(ex)}")
    finally:
        conn.close()

# ===============================================
def get_tabledata(ev):
    f=product_Table.focus()
    content=(product_Table.item(f))
    row=content['values']
    #    print(row)

    var_pid.set(row[0])
    var_pname.set(row[1])
    #    var_qty.set(rows[2])
    var_price.set(row[2])
    lbl_instock.config(text=f"In Stock[{str(row[3])}]")
    var_stock.set(row[3])
    # var_qty.set('1')

# ==========================================================
    
def get_cart_data(ev):
    f=cart_table.focus()
    content=(cart_table.item(f))
    row=content['values']
    #    print(row)

    var_pid.set(row[0])
    var_pname.set(row[1])
    #    var_qty.set(rows[2])
    var_price.set(row[2])
    var_qty.set(row[3])
    lbl_instock.config(text=f"In Stock[{str(row[4])}]")
    var_stock.set(row[4])
   

# =========================================================== 
def add_update_cart():
    if var_pid.get()=='':
        messagebox.showerror("Error","Please select from the list")
    elif var_qty.get()=='':
        messagebox.showerror("Error","Qantity is required")
    elif int(var_qty.get())>int(var_stock.get()):
        messagebox.showerror("Error","Invalid Quantity")
    else:
        # price_cal=int(var_qty.get())*float(var_price.get())
        # price_cal=float(price_cal)
        # print(price_cal)
        price_cal=var_price.get()
        cart_data=[var_pid.get(),var_pname.get(),price_cal,var_qty.get(),var_stock.get()]
        cart_list.append(cart_data)
        # print(cart_list)
        show_cart()
        bill_update()

# ===========================================================
def bill_update():
    bill_amt=0
    net_pay=0
    discount=0
    for row in cart_list:
        # pid,name,price,qty,status
        bill_amt=bill_amt+(float(row[2])*int(row[3]))
    discount=(bill_amt*5)/100
    net_pay=bill_amt-discount
    lbl_amount.config(text=f"Bill Amnt \n{str(bill_amt)}")
    lbl_net_pay.config(text=f"Net Pay \n{str(net_pay)}")

    cart_Title.config(text=f'Cart \t Total Product : [{str(len(cart_list))}]')


# ========================================================================
        
def show_cart():
    try:
        cart_table.delete(*cart_table.get_children())
        for row in cart_list:
            cart_table.insert('', 'end', values=row)

    except Exception as ex:
           messagebox.showerror("Error", f"Error due to: {str(ex)}")


# ===================================================================================
      
def generate_bill():
    if var_name.get()=='' or var_contact.get()=='':
        messagebox.showerror("Error","Customer detail are required") 
    elif len(cart_list)==0:
        messagebox.showerror("Error","Please Add Product to the Cart")
    else:
        bill_top()

        bill_amt=0
        net_pay=0
        discount=0

        for row in cart_list:
            bill_amt=bill_amt+(float(row[2])*int(row[3]))

        discount=(bill_amt*5)/100
        net_pay=bill_amt-discount

        bill_middle()
        bill_botttom(bill_amt, discount, net_pay)

        # Save bill
        invoice = int(time.strftime("%H%M%S")) + int(time.strftime("%d%m%Y"))
        with open(f'bill/{invoice}.txt', 'w') as fp:
            fp.write(txt_bill_area.get('1.0', END))
        messagebox.showinfo("Saved", "Bill has been generated/saved")

        


def bill_top():
    invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y"))
    bill_top_temp=f'''
            XYZ-Inventory

 Phone No. 12345*****, Sonai-414605
{str("="*36)}
 Customer Name : {var_name.get()}
 Ph no. : {var_contact.get()}
 Bill No. {str(invoice)}\t\tDate: {str(time.strftime("%d/%m/%Y"))}
{str("="*36)}
 Product Name\t\tQTY\tPrice
{str("="*36)}'''
    txt_bill_area.delete('1.0',END)
    txt_bill_area.insert("1.0",bill_top_temp)


def bill_middle():
    conn=sqlite3.connect("IMS.db")
    cur=conn.cursor()
    try:
        for row in cart_list:
            pid=row[0]
            name=row[1]
            qty=int(row[4])-int(row[3])
            if int(row[3])==int(row[4]):
                status='Inactive'
            if int(row[3])!=int(row[4]):
                status='Active'

            price=float(row[2])*int(row[3])
            price=str(price)
            txt_bill_area.insert(END,"\n"+name+"\t\t"+row[3]+"\tRs."+price)
# =============update qty in product table==========
            cur.execute("Update product set qty=?,status=? where pid=?",(
                qty,
                status,
                pid
            ))
            conn.commit()

    except Exception as ex:
        conn.close()
        prod_show()



def bill_botttom(bill_amt, discount, net_pay):
    bill_bottom_temp=f'''
{str("="*36)}
 Bill Amount\t\t\tRs.{bill_amt}
 Discount\t\t\tRs.{discount}
 Net Pay\t\t\tRs.{net_pay}
{str("="*36)}\n
    '''
    txt_bill_area.insert("end",bill_bottom_temp)

# =======================================================================================   

def clear_cart():
    var_pid.set('')    
    var_pname.set('')   
    var_price.set('')   
    var_qty.set('')   
    lbl_instock.config(text=f"In stock")   
    var_stock.set('')   
# ======================================================================================
def clear_all():
    del cart_list[:]
    var_name.set('')
    var_contact.set('')
    txt_bill_area.delete('1.0',END)
    cart_Title.config(text=f'Cart \t Total Product : [0]')
    var_search.set('')
    clear_cart()
    prod_show()
    show_cart()
 # ================================================

def update_date_time():
    time_=time.strftime("%I:%M:%S")
    date_=time.strftime("%d-%m-%Y")
    clock.config(text=f"Welcome to Warehouse Stock Management System\t\t Date:{str(date_)}\t\t Time:{str(time_)}")

    clock.after(200,update_date_time)

# ======================================================

def print_bill():
    chk_print=1
    if chk_print==1:
        messagebox.showinfo("Print","Please wait while printing")
        new_file=tempfile.mktemp('.txt')
        open(new_file,'w').write(txt_bill_area.get('1.0',END))
        os.startfile(new_file,"print")
    else:
        messagebox.showerror("Print","Please generate bill, to print the receipt")

       

# =======================================================================================
# ====Product Search Frame======
productframe2=Frame(productframe1,bd=2,relief=RIDGE,bg="white")
productframe2.place(x=2,y=42,width=398,height=90)

lbl_search=Label(productframe2,text="Search Product",font=("Arial",15,"bold"),bg="white",
                 fg="green")
lbl_search.place(x=2,y=5)

lbl_name=Label(productframe2,text="Product Name",font=("Arial",13,"bold"),bg="white")
lbl_name.place(x=2,y=45)

txt_search=Entry(productframe2,textvariable=var_search,font=("Arial",15),bg="lightyellow")
txt_search.place(x=128,y=47,width=150,height=22)

btn_search=Button(productframe2,text="Search",command=search,font=("Arial",14),bg="Lightgreen",cursor="hand2")
btn_search.place(x=285,y=45,width=100,height=25)

btn_show_all=Button(productframe2,text="Show All",command=prod_show,font=("Arial",14),bg="Lightgreen",cursor="hand2")
btn_show_all.place(x=285,y=10,width=100,height=25)
 
           
# =========Product Details============
productframe3 = Frame(productframe1,bd=3,relief=RIDGE,bg="white")
productframe3.place(x=2,y=140,width=398,height=350)

scrolly=Scrollbar(productframe3,orient=VERTICAL)
scrollx= Scrollbar(productframe3,orient=HORIZONTAL)

product_Table=ttk.Treeview(productframe3,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,
                           xscrollcommand=scrollx.set)


scrollx.pack(side=BOTTOM,fill=X)
scrolly.pack(side=RIGHT,fill=Y)
scrollx.config(command=product_Table.xview)
scrolly.config(command=product_Table.yview)

product_Table.heading("pid",text="pid")
product_Table.heading("name", text="Name")
product_Table.heading("price",text="price")
product_Table.heading("qty", text="qty")
product_Table.heading("status", text="status")

product_Table["show"]="headings"

product_Table.column("pid",width=10)
product_Table.column("name",width=40)
product_Table.column("price",width=40)
product_Table.column("qty",width=20)
product_Table.column("status",width=20)
    
product_Table.pack(fill=BOTH,expand=1)
product_Table.bind("<ButtonRelease-1>",get_tabledata)



# =============Customer frame==================

customer_frame=Frame(root,bd=4,relief=RIDGE,bg="white")
customer_frame.place(x=420,y=110,width=530,height=70)

customer_Title=Label(customer_frame,text="Customer Detail",font=("times new roman",15,"bold"),bg="lightgray")
customer_Title.pack(side=TOP,fill=X)

lbl_name=Label(customer_frame,text="Name",font=("Arial",15,),bg="white")
lbl_name.place(x=5,y=35)

txt_name=Entry(customer_frame,textvariable=var_name,font=("Arial",15),bg="lightyellow")
txt_name.place(x=80,y=35,width=180,height=24)

lbl_contact=Label(customer_frame,text="Contact No.",font=("Arial",15,),bg="white")
lbl_contact.place(x=270,y=35)

txt_contact=Entry(customer_frame,textvariable=var_contact,font=("Arial",15),bg="lightyellow")
txt_contact.place(x=380,y=35,width=140,height=24)


# ================= Calculator cart frame ===============
cal_cart_frame=Frame(root,bd=2,relief=RIDGE,bg="white")
cal_cart_frame.place(x=420,y=190,width=530,height=360)
# ==========================================================

# =========All Functions=====================================

def get_input(num):
    xnum=var_cal_input.get()+str(num)
    var_cal_input.set(xnum)

def clear_cal():
    var_cal_input.set('')

def perform_cal():
    result=var_cal_input.get()
    var_cal_input.set(eval(result))


# =============================================================

# ====Cal Frame=========
var_cal_input=StringVar()


cal_frame=Frame(cal_cart_frame,bd=9,relief=RIDGE,bg="white")
cal_frame.place(x=5,y=10,width=268,height=340)

txt_cal_input=Entry(cal_frame,textvariable=var_cal_input,font=("Arial",15,"bold"),width=21,bd=10,
                    relief=GROOVE,state="readonly",justify=RIGHT)
txt_cal_input.grid(row=0,columnspan=4)

# ==========Button=======================================
# first row
btn_7=Button(cal_frame,text='7',font=("Arial",15,"bold"),bd=5,width=4,pady=10,cursor="hand2",
             command=lambda:get_input(7))
btn_7.grid(row=1,column=0)

btn_8=Button(cal_frame,text='8',font=("Arial",15,"bold"),bd=5,width=4,pady=10,cursor="hand2",
             command=lambda:get_input(8))
btn_8.grid(row=1,column=1)

btn_9=Button(cal_frame,text='9',font=("Arial",15,"bold"),bd=5,width=4,pady=10,cursor="hand2",
             command=lambda:get_input(9))
btn_9.grid(row=1,column=2)

btn_sum=Button(cal_frame,text="+",font=("Arial",15,"bold"),bd=5,width=4,pady=10,cursor="hand2",
               command=lambda:get_input('+'))
btn_sum.grid(row=1,column=3)

# second row
btn_4=Button(cal_frame,text='4',font=("Arial",15,"bold"),bd=5,width=4,pady=10,cursor="hand2",
             command=lambda:get_input(4))
btn_4.grid(row=2,column=0)

btn_5=Button(cal_frame,text='5',font=("Arial",15,"bold"),bd=5,width=4,pady=10,cursor="hand2",
             command=lambda:get_input(5))
btn_5.grid(row=2,column=1)

btn_6=Button(cal_frame,text='6',font=("Arial",15,"bold"),bd=5,width=4,pady=10,cursor="hand2",
             command=lambda:get_input(6))
btn_6.grid(row=2,column=2)

btn_sub=Button(cal_frame,text="-",font=("Arial",15,"bold"),bd=5,width=4,pady=10,cursor="hand2",
               command=lambda:get_input('-'))
btn_sub.grid(row=2,column=3)

# third row
btn_1=Button(cal_frame,text='1',font=("Arial",15,"bold"),bd=5,width=4,pady=10,cursor="hand2",
             command=lambda:get_input(1))
btn_1.grid(row=3,column=0)

btn_2=Button(cal_frame,text='2',font=("Arial",15,"bold"),bd=5,width=4,pady=10,cursor="hand2",
             command=lambda:get_input(2))
btn_2.grid(row=3,column=1)

btn_3=Button(cal_frame,text='3',font=("Arial",15,"bold"),bd=5,width=4,pady=10,cursor="hand2",
             command=lambda:get_input(3))
btn_3.grid(row=3,column=2)

btn_mul=Button(cal_frame,text="*",font=("Arial",15,"bold"),bd=5,width=4,pady=10,cursor="hand2",
               command=lambda:get_input('*'))
btn_mul.grid(row=3,column=3)

# fourth row
btn_0=Button(cal_frame,text='0',font=("Arial",15,"bold"),bd=5,width=4,pady=15,cursor="hand2",
             command=lambda:get_input(0))
btn_0.grid(row=4,column=0)

btn_c=Button(cal_frame,text='c',font=("Arial",15,"bold"),bd=5,width=4,pady=15,cursor="hand2",
             command=clear_cal)
btn_c.grid(row=4,column=1)

btn_equal=Button(cal_frame,text='=',font=("Arial",15,"bold"),bd=5,width=4,pady=15,cursor="hand2",
                 command=perform_cal)
btn_equal.grid(row=4,column=2)

btn_div=Button(cal_frame,text="/",font=("Arial",15,"bold"),bd=5,width=4,pady=15,cursor="hand2",
               command=lambda:get_input('/'))
btn_div.grid(row=4,column=3)

# ===Cart Frame==========
cart_frame = Frame(cal_cart_frame,bd=3,relief=RIDGE,bg="white")
cart_frame.place(x=280,y=8,width=245,height=342)

cart_Title=Label(cart_frame,text="Cart \t Total Product:[0]",font=("times new roman",15,),bg="lightgray")
cart_Title.pack(side=TOP,fill=X)

scrolly=Scrollbar(cart_frame,orient=VERTICAL)
scrollx= Scrollbar(cart_frame,orient=HORIZONTAL)

cart_table=ttk.Treeview(cart_frame,columns=("pid","name","price","qty"),yscrollcommand=scrolly.set,
                           xscrollcommand=scrollx.set)


scrollx.pack(side=BOTTOM,fill=X)
scrolly.pack(side=RIGHT,fill=Y)
scrollx.config(command=cart_table.xview)
scrolly.config(command=cart_table.yview)

cart_table.heading("pid",text="pid")
cart_table.heading("name", text="Name")
cart_table.heading("price",text="price")
cart_table.heading("qty", text="qty")

cart_table["show"]="headings"

cart_table.column("pid",width=50)
cart_table.column("name",width=100)
cart_table.column("price",width=90)
cart_table.column("qty",width=50)

    
cart_table.pack(fill=BOTH,expand=1)
cart_table.bind("<ButtonRelease-1>",get_cart_data)

# ===================Add cart Frame===========
cart_button_frame=Frame(root,bd=2,relief=RIDGE,bg="white")
cart_button_frame.place(x=420,y=550,width=530,height=90)

lbl_p_name=Label(cart_button_frame,text="Product Name",font=("times new roman",15),bg="white")
lbl_p_name.place(x=5,y=5)

txt_p_name=Entry(cart_button_frame,textvariable=var_pname,font=("times new roman",15),
                 state="readonly",bg="lightyellow")
txt_p_name.place(x=5,y=35,width=190,height=22)


lbl_p_price=Label(cart_button_frame,text="Price Per Qty",font=("times new roman",15),bg="white")
lbl_p_price.place(x=230,y=5)

txt_p_price=Entry(cart_button_frame,textvariable=var_price,font=("times new roman",15),
                 state="readonly",bg="lightyellow")
txt_p_price.place(x=230,y=35,width=150,height=22)


lbl_p_qty=Label(cart_button_frame,text="Qty",font=("times new roman",15),bg="white")
lbl_p_qty.place(x=390,y=5)

txt_p_qty=Entry(cart_button_frame,textvariable=var_qty,font=("times new roman",15),
                 bg="lightyellow")
txt_p_qty.place(x=390,y=35,width=120,height=22)


lbl_instock=Label(cart_button_frame,text="In Stock",font=("times new roman",14),bg="white")
lbl_instock.place(x=5,y=60)

# ========= Buttton================================================
btn_clear=Button(cart_button_frame,text="Clear",command=clear_cart,font=("Arial",14),bg="Lightgreen",cursor="hand2")
btn_clear.place(x=180,y=60,width=120,height=22)

btn_add=Button(cart_button_frame,text="Add",command=add_update_cart,font=("Arial",14),bg="Lightgreen",cursor="hand2")
btn_add.place(x=340,y=60,width=160,height=22)

# ========================billing area====================================
billframe=Frame(root,bd=2,relief=RAISED,bg="white")
billframe.place(x=953,y=110,width=320,height=410)

bTitle=Label(billframe,text="Customer Bill Area",font=("times new roman",20,"bold"),bg="black",fg="white")
bTitle.pack(side=TOP,fill=X)

scrolly=Scrollbar(billframe,orient=VERTICAL)
scrolly.pack(side=RIGHT,fill=Y)

txt_bill_area=Text(billframe,yscrollcommand=scrolly.set)
txt_bill_area.pack(fill=BOTH,expand=1)

scrolly.config(command=txt_bill_area.yview)

# ==========Billing Button=================================
bill_menu_frame=Frame(root,bd=2,relief=RAISED,bg="white")
bill_menu_frame.place(x=953,y=520,width=320,height=118)

lbl_amount=Label(bill_menu_frame,text="Bill Amount\n[0]",font=("Arial",13,"bold"),bg="Blue",
                 fg="white")
lbl_amount.place(x=2,y=2,width=100,height=60)

lbl_discount=Label(bill_menu_frame,text="Discount\n[5%]",font=("Arial",13,"bold"),bg="Blue",
                 fg="white")
lbl_discount.place(x=110,y=2,width=100,height=60)

lbl_net_pay=Label(bill_menu_frame,text="Net Pay\n[0]",font=("Arial",13,"bold"),bg="Blue",
                 fg="white")
lbl_net_pay.place(x=215,y=2,width=100,height=60)

# button

btn_print=Button(bill_menu_frame,text="Print",command=print_bill,font=("Arial",13,"bold"),bg="lightgreen",
                 fg="black",cursor="hand2")
btn_print.place(x=2,y=70,width=100,height=40)

btn_clear=Button(bill_menu_frame,text="Clear All",command=clear_all,font=("Arial",13,"bold"),bg="lightgreen",
                 fg="black",cursor="hand2")
btn_clear.place(x=110,y=70,width=100,height=40)

btn_generate=Button(bill_menu_frame,text="Save\ \nGenerate Bill",command=generate_bill,font=("Arial",13,"bold"),bg="lightgreen",
                 fg="black",cursor="hand2")
btn_generate.place(x=215,y=70,width=100,height=40)


prod_show()
update_date_time()


root.mainloop()