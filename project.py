from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import os
import time
# from listlib import clear


# employee page
def show_employee_page():
    # # Create a new frame for the employee page
    # emp_root=Tk()
    # emp_root.title("Employee")
    # emp_root.geometry("1090x490+200+130")
    employee_frame = Frame(root, border=2, relief=RIDGE, bg="white")
    employee_frame.place(x=200, y=102, width=1150, height=520)
    #
    # Add content to the employee page
    # label_employee = Label(employee_frame, text="Employee Page", font=("times new roman", 20, "bold"),
    #                        bg="skyblue", fg="black", bd=5, relief=RIDGE)
    # label_employee.pack(side=TOP, fill=X)
    
    # # For example:
    # btn_back = Button(employee_frame, text="Back", font=("times new roman", 17, "bold"), bg="red",
    #                   bd=3, cursor="hand2", command=employee_frame.destroy)
    # btn_back.pack(side=TOP, fill=X)

    # All variable
    var_serachby = StringVar()
    var_searchtxt = StringVar()

    var_emp_id = StringVar()
    var_emp_gender = StringVar()
    var_emp_contact = StringVar()
    var_emp_name = StringVar()
    var_emp_dob = StringVar()
    var_emp_doj = StringVar()
    var_emp_email = StringVar()
    var_emp_pass = StringVar()
    var_emp_utype = StringVar()
    var_emp_salary = StringVar()
# =======================================================

    def search_emp():
      conn = sqlite3.connect("IMS.db")
      cursor = conn.cursor()

      try:
        search_field = var_serachby.get()
        search_text = var_searchtxt.get()

        if search_field == "select":
            messagebox.showerror("Error", "Select Search By Option")
            return

        if not search_text:
            messagebox.showerror("Error", "Search input should be required")
            return

        if search_field not in ["Email", "Name","Contact"]:
            messagebox.showerror("Error", f"Invalid search field '{search_field}'")
            return
        query = "SELECT * FROM employee WHERE {} LIKE ?".format(search_field)
        cursor.execute(query, ('%' + search_text + '%',))
        rows = cursor.fetchall()

        if len(rows) != 0:
               emp_table.delete(*emp_table.get_children())
        for row in rows:
                emp_table.insert('', 'end', values=row)
        
            

      except Exception as ex:
        messagebox.showerror("Error", f"Error due to: {str(ex)}")
      finally:
        conn.close()
# =======================================================

    # SEARCH FREAME
    searchframe=LabelFrame(root,text="Search Employee",font=("Times new Roman",14,"bold"),
                          bg="white",bd=3,relief=RIDGE, )
    searchframe.place(x=300,y=120,width=600,height=70)

#     Options
    search=ttk.Combobox(searchframe,textvariable=var_serachby,values=("Select","Email","Name","Contact"),
                        state="readonly",justify=CENTER,font=("Arial",14))
    search.place(x=10,y=10,width=200)
    search.current(0)

    txt_search=Entry(searchframe,textvariable=var_searchtxt,font=("Arial",14),bg="lightyellow")
    txt_search.place(x=220,y=10,width=200)

    btn_search=Button(searchframe,text="Search",font=("Arial",14),bg="lightgreen",fg="black",
                      cursor="hand2",command=search_emp)
    btn_search.place(x=435,y=9,width=150,height=25)

# title
    title =Label(root,text="Employee Details",font=("Times new roman",15),bg="skyblue",
                 fg="Black")
    title.place(x=240,y=200,width=1000)

#    ===== content
#     row1
    label_id = Label(root, text="Emp ID", font=("Times new roman", 15), bg="white")
    label_id.place(x=240, y=250)

    label_gender = Label(root, text="Gender", font=("Times new roman", 15), bg="white")
    label_gender.place(x=540, y=250)

    label_contact = Label(root, text="Contact", font=("Times new roman", 15), bg="white")
    label_contact.place(x=860, y=250)



    txt_id = Entry(root, textvariable=var_emp_id, font=("Times new roman", 15),bg="white")
    txt_id.place(x=330, y=250,width=180)

    txt_gender = Entry(root, textvariable=var_emp_gender, font=("Times new roman", 15),
                          bg="white")
    txt_gender.place(x=650, y=250,width=180)

    gender = ttk.Combobox(root, textvariable=var_emp_gender, values=("Select", "Male", "Female", "Other"),
                      state="readonly", justify=CENTER, font=("Arial", 14))

    gender.place(x=650, y=250,width=180)
    gender.current(0)

    txt_contact = Entry(root, textvariable=var_emp_contact, font=("Times new roman", 15),
                           bg="white")
    txt_contact.place(x=950, y=250,width=180)

#     row2
    label_name = Label(root, text="Name", font=("Times new roman", 15), bg="white")
    label_name.place(x=240, y=290)

    label_dob = Label(root, text="D.O.B", font=("Times new roman", 15), bg="white")
    label_dob.place(x=540, y=290)

    label_doj = Label(root, text="D.O.J", font=("Times new roman", 15), bg="white")
    label_doj.place(x=860, y=290)


    txt_name = Entry(root, textvariable=var_emp_name, font=("Times new roman", 15),bg="white")
    txt_name.place(x=330, y=290,width=180)

    txt_dob = Entry(root, textvariable=var_emp_dob, font=("Times new roman", 15),
                          bg="white")
    txt_dob.place(x=650, y=290,width=180)

    txt_doj = Entry(root, textvariable=var_emp_doj, font=("Times new roman", 15),
                        bg="white")
    txt_doj.place(x=950, y=290, width=180)

#     row3
    label_email = Label(root, text="Email", font=("Times new roman", 15), bg="white")
    label_email.place(x=240, y=330)

    label_pass = Label(root, text="Password", font=("Times new roman", 15), bg="white")
    label_pass.place(x=540, y=330)

    label_utype = Label(root, text="UType", font=("Times new roman", 15), bg="white")
    label_utype.place(x=860, y=330)

    txt_email = Entry(root, textvariable=var_emp_email, font=("Times new roman", 15), bg="white")
    txt_email.place(x=330, y=330, width=180)

    txt_pass = Entry(root, textvariable=var_emp_pass, font=("Times new roman", 15),
                    bg="white")
    txt_pass.place(x=650, y=330, width=180)

    txt_utype = Entry(root, textvariable=var_emp_utype, font=("Times new roman", 15),
                    bg="white")
    txt_utype.place(x=950, y=330, width=180)

    utype = ttk.Combobox(root, textvariable=var_emp_utype, values=("Admin", "Employee"),
                          state="readonly", justify=CENTER, font=("Arial", 14))
    utype.place(x=950, y=330, width=180)
    utype.current(0)


#     row4
    label_address = Label(root, text="Address", font=("Times new roman", 15), bg="white")
    label_address.place(x=240, y=370)

    label_salary = Label(root, text="Salary", font=("Times new roman", 15), bg="white")
    label_salary.place(x=650, y=370)

    txt_address = Text(root, font=("Times new roman", 15), bg="white")
    txt_address.place(x=330, y=370, width=300,height=60)

    txt_salary = Entry(root, textvariable=var_emp_salary, font=("Times new roman", 15),
                     bg="white")
    txt_salary.place(x=730, y=370, width=180)
# =================================================================
    # ==============================================================
# data add in table
    def add():
       conn = sqlite3.connect("IMS.db")
    #    conn.execute('''
    #                   Create table employee(
    #                   eid INT AUTO INCREMENT PRIMARY KEY,
    #                   name VARCHAR(30),
    #                   email VARCHAR(30),
    #                   gender VARCHAR(10),
    #                   contact VARCHAR(15),
    #                   dob VARCHAR(10),
    #                   doj VARCHAR(10),
    #                   pass VARCHAR(10),
    #                   utype VARCHAR(10),
    #                   address VARCHAR(30),
    #                   salary VARCHAR(10))
    #                ''')
       if var_emp_id.get() == "":
          messagebox.showerror("Error", "Employee ID must be required")
       else:
        try:
           conn.execute("Select * from employee where eid=?", (var_emp_id.get(),))
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")


    #    empid = var_emp_id.get()
    #    if not empid:
    #        # Show an error message or handle it as needed
    #        messagebox.showerror("Error", "Employee ID is required.")
    #        return

       # Connect to SQLite database (replace 'your_database.db' with your actual database name)
      #  conn = sqlite3.connect('data.db')

       try:
           conn.execute('''
               INSERT INTO employee (eid, name, email, gender, contact, dob, doj, pass,
                                     utype, address, salary)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
           ''', (
               var_emp_id.get(),
               var_emp_name.get(),
               var_emp_email.get(),
               var_emp_gender.get(),
               var_emp_contact.get(),
               var_emp_dob.get(),
               var_emp_doj.get(),
               var_emp_pass.get(),
               var_emp_utype.get(),
               txt_address.get('1.0', 'end-1c'),  # fix: use 'end-1c' to remove trailing newline
               var_emp_salary.get()
           ))

           conn.commit()
           messagebox.showinfo("Success", "Employee data added successfully.")
           show()
       except Exception as e:
           messagebox.showerror("Error", f"An error occurred: {str(e)}")
       finally:
           # Close the connection
           conn.close()

#    ===========================================
# data show in table
    def show():
        conn = sqlite3.connect("IMS.db")
        # cur=conn.cursor()
        cursor = conn.cursor()

        try:
           cursor.execute("SELECT * FROM employee")
           rows = cursor.fetchall()
        
        # Assuming Emp1 is a ttk.Treeview widget, you need to replace Emp1 with your actual Treeview widget instance
           emp_table.delete(*emp_table.get_children())

           for row in rows:
            emp_table.insert('', 'end', values=row)

        except Exception as ex:
        #    messagebox.showerror("Error", f"Error due to: {str(ex)}")
        # finally:
           conn.close()    

# =============================================
       # data show in forms rows   
    def get_tabledata(ev):
       f=emp_table.focus()
       content=(emp_table.item(f))
       row=content['values']
    #    print(row)

       var_emp_id.set(row[0]),
       var_emp_name.set(row[1]),
       var_emp_email.set(row[2]),
       var_emp_gender.set(row[3]),
       var_emp_contact.set(row[4]),
       var_emp_dob.set(row[5]),
       var_emp_doj.set(row[6]),
       var_emp_pass.set(row[7]),
       var_emp_utype.set(row[8]),
       txt_address.delete('1.0', 'end'), 
       txt_address.insert(END,row[9]), 
       var_emp_salary.set(row[10])

# ==================================================
#  update data    
    def update():
            conn = sqlite3.connect("IMS.db")
            try:
               if var_emp_id.get() == "":
                  messagebox.showerror("Error", "Employee ID must be required")
               else:
            # Fetch the row
                  cursor = conn.execute("SELECT * FROM employee WHERE eid=?", (var_emp_id.get(),))
                  row = cursor.fetchone()

                  if row is None:
                    messagebox.showerror("Error", "Invalid Employee ID")
                  else:
                # Update the row
                      conn.execute('''
                      UPDATE employee SET name=?, email=?, gender=?, contact=?, dob=?, doj=?, pass=?,
                      utype=?, address=?, salary=? WHERE eid=? ''', (
                      var_emp_name.get(),
                      var_emp_email.get(),
                      var_emp_gender.get(),
                      var_emp_contact.get(),
                      var_emp_dob.get(),
                      var_emp_doj.get(),
                      var_emp_pass.get(),
                      var_emp_utype.get(),
                      txt_address.get('1.0', 'end-1c'),
                      var_emp_salary.get(),
                      var_emp_id.get(),
                ))

                      conn.commit()
                      messagebox.showinfo("Success", "Employee data updated successfully.")
                      show()
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
            

# =====================================================
# delete data from table
    def delete():
       conn = sqlite3.connect("IMS.db")
       try:
          if var_emp_id.get() == "":
                  messagebox.showerror("Error", "Employee ID must be required")
          else:
            # Fetch the row
                  cursor = conn.execute("SELECT * FROM employee WHERE eid=?", (var_emp_id.get(),))
                  row = cursor.fetchone()

                  if row is None:
                    messagebox.showerror("Error", "Invalid Employee ID")
                  else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?")
                    if op==True:
                      cursor.execute("delete from employee where eid=?",(var_emp_id.get(),))
                      conn.commit()
                      messagebox.showinfo("Delete","Employee Deleted Successfully")
                      
                      clear()
       except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")            

# =================================================================
            
    def clear():
       var_emp_id.set(""),
       var_emp_name.set(""),
       var_emp_email.set(""),
       var_emp_gender.set("Select"),
       var_emp_contact.set(""),

       var_emp_dob.set(""),
       var_emp_doj.set(""),

       var_emp_pass.set(""),
       var_emp_utype.set("Admin"),
       txt_address.delete('1.0', 'end'), 
       var_emp_salary.set("")
       var_searchtxt.set("")
       var_serachby.set("")
       
       show()

# ====================================================
# ========================================

    #button
#     Save button
    btn_add = Button(root, text="Save", font=("Arial", 14), bg="lightgreen", fg="black",
                        cursor="hand2",command=add)
    btn_add.place(x=650, y=410, width=110, height=28)

# Update Button
    btn_update = Button(root, text="Update", font=("Arial", 14), bg="lightgreen", fg="black",
                     cursor="hand2",command=update)
    btn_update.place(x=770, y=410, width=110, height=28)


#   Delete Button
    btn_delete = Button(root, text="Delete", font=("Arial", 14), bg="lightgreen", fg="black",
                     cursor="hand2",command=delete)
    btn_delete.place(x=890, y=410, width=110, height=28)

#     Clear Button
    btn_clear = Button(root, text="Clear", font=("Arial", 14), bg="lightgreen", fg="black",
                     cursor="hand2",command=clear)
    btn_clear.place(x=1010, y=410, width=110, height=28)

#     Employee details
    emp_frame = Frame(root,bd=3,relief=RIDGE,bg="white")
    emp_frame.place(x=202,y=450,width=1075,height=170)

    # scrolly=Scrollbar(emp_frame,orient=VERTICAL)
    # scrollx= Scrollbar(emp_frame,orient=HORIZONTAL)

    emp_table=ttk.Treeview(emp_frame,columns=("eid","name","email","gender","contact","dob","doj",
                                              "pass","utype","address","salary"))
                           # ,yscrollcommand=scrolly.set,
                           # xscrollcommand=scrollx.set)


    # scrollx.pack(side=BOTTOM,fill=X)
    # scrolly.pack(side=RIGHT,fill=Y)
    # scrollx.config(command=emp_table.xview)
    # scrolly.config(command=emp_table.yview)

    emp_table.heading("eid",text="EMP ID")
    emp_table.heading("name", text="Name")
    emp_table.heading("email",text="Email")
    emp_table.heading("gender", text="Gender")
    emp_table.heading("contact", text="Contact")
    emp_table.heading("dob", text="DOB")
    emp_table.heading("doj", text="DOJ")
    emp_table.heading("pass", text="Password")
    emp_table.heading("utype", text="Utype")
    emp_table.heading("address", text="Address")
    emp_table.heading("salary", text="Salary")

    emp_table["show"]="headings"

    emp_table.column("eid",width=10)
    emp_table.column("name",width=20)
    emp_table.column("email",width=50)
    emp_table.column("gender",width=20)
    emp_table.column("contact",width=40)
    emp_table.column("dob",width=20)
    emp_table.column("doj",width=20)
    emp_table.column("pass",width=40)
    emp_table.column("utype",width=30)
    emp_table.column("address",width=40)
    emp_table.column("salary",width=30)
    emp_table.pack(fill=BOTH)
    emp_table.bind("<ButtonRelease-1>",get_tabledata)
    show()
    

# ==============================================================
#  Supplier page    
def show_supplier_page():
    # # Create a new frame for the employee page

    
    supplier_frame = Frame(root, border=2, relief=RIDGE, bg="white")
    supplier_frame.place(x=200, y=102, width=1150, height=520)
    

    # All variable
    # var_sup_serachby = StringVar()
    var_sup_searchby = StringVar()
    var_sup_searchtxt =StringVar()

    var_suppiler_invoice = StringVar()
    var_supplier_name = StringVar()
    var_supplier_contact = StringVar()

    cat_list=[]
    sup_list=[]
    

    # SEARCH FREAME
    # ===============================================================
    def search_sup():
      conn = sqlite3.connect("IMS.db")
      cursor = conn.cursor()

      try:
       if var_sup_searchtxt.get() == "":
            messagebox.showerror("Error","Invoice No should be required")
       else:
           cursor.execute("select * from supplier where invoice = ?",( var_sup_searchtxt.get(),))
           row = cursor.fetchone()
           if row != None:
                sup_table.delete(*sup_table.get_children())
                sup_table.insert('',END,values=row)
           else:
               messagebox.showerror("Error","No record found")
      except Exception as e:
          messagebox.showerror("Error",f"Error due to : {str(e)}")      
          conn.close()

# 
    # ==============================================================
    

#     Options
    sup_search=Label(root,text="Invoice No",bg="white",font=("Arial",14))
    sup_search.place(x=750,y=200)
    
    txt_search=Entry(root,textvariable=var_sup_searchtxt,font=("Arial",14),bg="lightyellow")
    txt_search.place(x=870,y=200,width=220)

    btn_search=Button(root,text="Search",font=("Arial",14),bg="lightgreen",fg="black",
                      cursor="hand2",command=search_sup)
    btn_search.place(x=1100,y=200,width=140,height=25)

# title
    title =Label(root,text="Supplier Details",font=("Times new roman",20,"bold"),bg="skyblue",
                 fg="Black")
    title.place(x=240,y=120,width=1000,height=40)

#    ===== content
#     row1
    label_sup_invoice = Label(root, text="Invoice No", font=("Times new roman", 15), bg="white")
    label_sup_invoice.place(x=240, y=200)

    txt_sup_invoice = Entry(root, textvariable=var_suppiler_invoice, font=("Times new roman", 15),bg="lightyellow")
    txt_sup_invoice.place(x=350, y=200,width=180)

    #     row2
    label_sup_name = Label(root, text="Name", font=("Times new roman", 15), bg="white")
    label_sup_name.place(x=240, y=240)

    txt_sup_name = Entry(root, textvariable=var_supplier_name, font=("Times new roman", 15),bg="lightyellow")
    txt_sup_name.place(x=350, y=240,width=180)

    #     row3
    label_sup_contact = Label(root, text="Contact", font=("Times new roman", 15), bg="white")
    label_sup_contact.place(x=240, y=280)


    txt_sup_contact = Entry(root, textvariable=var_supplier_contact, font=("Times new roman", 15), bg="lightyellow")
    txt_sup_contact.place(x=350, y=280, width=180)

    #     row4
    label_sup_desc = Label(root, text="Description", font=("Times new roman", 15), bg="white")
    label_sup_desc.place(x=240, y=320)

    txt_sup_desc = Text(root, font=("Times new roman", 15), bg="lightyellow")
    txt_sup_desc.place(x=350, y=320, width=450,height=110)

# ======================================================

    def sup_add():
       conn = sqlite3.connect("IMS.db")
    #    conn.execute('''
    #                   Create table supplier(
    #                   invoice INTEGER  PRIMARY KEY AUTOINCREMENT,
    #                   name VARCHAR(30),
    #                   contact VARCHAR(15),
    #                   desc VARCHAR(30)
    #                 ) 
    #                ''')
       if var_suppiler_invoice.get() == "":
          messagebox.showerror("Error", "Invoice must be required")
       else:
        try:
           conn.execute("Select * from supplier where invoice=?",(var_suppiler_invoice.get(),))
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")


    #    empid = var_emp_id.get()
    #    if not empid:
    #        # Show an error message or handle it as needed
    #        messagebox.showerror("Error", "Employee ID is required.")
    #        return

       # Connect to SQLite database (replace 'your_database.db' with your actual database name)
      #  conn = sqlite3.connect('data.db')

       try:
           conn.execute('''
               INSERT INTO supplier (invoice, name, contact, desc)
               VALUES (?, ?, ?, ?)
           ''', (
               var_suppiler_invoice.get(),
               var_supplier_name.get(),
               var_supplier_contact.get(),
               
               txt_sup_desc.get('1.0', 'end-1c'),  # fix: use 'end-1c' to remove trailing newline
               
           ))

           conn.commit()
           messagebox.showinfo("Success", "supplier data added successfully.")
           sup_show()
       except Exception as e:
           messagebox.showerror("Error", f"An error occurred: {str(e)}")
       finally:
           # Close the connection
           conn.close()

# =====================================
    def sup_show():
        conn = sqlite3.connect("IMS.db")
        # cur=conn.cursor()
        cursor = conn.cursor()

        try:
           cursor.execute("SELECT * FROM supplier")
           rows = cursor.fetchall()
        
        # Assuming Emp1 is a ttk.Treeview widget, you need to replace Emp1 with your actual Treeview widget instance
           sup_table.delete(*sup_table.get_children())

           for row in rows:
             sup_table.insert('', 'end', values=row)

        except Exception as ex:
           messagebox.showerror("Error", f"Error due to: {str(ex)}")
        finally:
           conn.close()  

# ====================================================
           
    def get_tabledata(ev):
       f=sup_table.focus()
       content=(sup_table.item(f))
       row=content['values']
    #    print(row)

       var_suppiler_invoice.set(row[0]),
       var_supplier_name.set(row[1]),
       var_supplier_contact.set(row[2]),
       
       txt_sup_desc.delete('1.0', 'end'), 
       txt_sup_desc.insert(END,row[3])

       sup_show()
       

# ================================================
    def sup_update():
            conn = sqlite3.connect("IMS.db")
            try:
               if var_suppiler_invoice.get() == "":
                  messagebox.showerror("Error", "Invoice must be required")
               else:
            # Fetch the row
                  cursor = conn.execute("SELECT * FROM supplier WHERE invoice=?", (var_suppiler_invoice.get(),))
                  row = cursor.fetchone()

                  if row is None:
                    messagebox.showerror("Error", "Invalid invoice No")
                  else:
                # Update the row
                      conn.execute('''
                      UPDATE supplier SET name=?,contact=?,desc=? WHERE invoice=? ''', (
                      var_supplier_name.get(),
                      var_supplier_contact.get(),
                      txt_sup_desc.get('1.0', 'end-1c'),
                      var_suppiler_invoice.get(),
                ))

                      conn.commit()
                      messagebox.showinfo("Success", "Supplier data updated successfully.")
                      sup_show()
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")

# =================================================================
    def sup_delete():
       conn = sqlite3.connect("IMS.db")
       try:
          if var_suppiler_invoice.get() == "":
                  messagebox.showerror("Error", "Invoice No must be required")
          else:
            # Fetch the row
                  cursor = conn.execute("SELECT * FROM supplier WHERE invoice=?", (var_suppiler_invoice.get(),))
                  row = cursor.fetchone()

                  if row is None:
                    messagebox.showerror("Error", "Invalid Invoice No")
                  else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?")
                    if op==True:
                      cursor.execute("DELETE FROM supplier WHERE invoice=?", (var_suppiler_invoice.get(),))

                      conn.commit()
                      messagebox.showinfo("Delete","Supplier Deleted Successfully")
                      
                      sup_clear()
       except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")            

# =================================================================
            
    def sup_clear():
        conn = sqlite3.connect("IMS.db")
        var_suppiler_invoice.set(""),
        var_supplier_name.set(""),
        var_supplier_contact.set(""),

        txt_sup_desc.delete('1.0', 'end'), 
        var_sup_searchtxt.set("")
        
# ==================================

#button
#     Save button
    btn_add = Button(root, text="Save", font=("Arial", 14), bg="lightgreen", fg="black",
                        cursor="hand2",command=sup_add)
    btn_add.place(x=350, y=455, width=110, height=35)

# Update Button
    btn_update = Button(root, text="Update", font=("Arial", 14), bg="lightgreen", fg="black",
                     cursor="hand2",command=sup_update)
    btn_update.place(x=470, y=455, width=110, height=35)


#   Delete Button
    btn_delete = Button(root, text="Delete", font=("Arial", 14), bg="lightgreen", fg="black",
                     cursor="hand2",command=sup_delete)
    btn_delete.place(x=590, y=455, width=110, height=35)

#     Clear Button
    btn_clear = Button(root, text="Clear", font=("Arial", 14), bg="lightgreen", fg="black",
                     cursor="hand2",command=sup_clear)
    btn_clear.place(x=710, y=455, width=110, height=35)

#     Employee details
    sup_frame = Frame(root,bd=3,relief=RIDGE,bg="white")
    sup_frame.place(x=850,y=240,width=400,height=375)

    # #     Employee details
    # sup_frame = Frame(root,bd=3,relief=RIDGE,bg="white")
    # sup_frame.place(x=202,y=450,width=1075,height=170)

    # scrolly=Scrollbar(emp_frame,orient=VERTICAL)
    # scrollx= Scrollbar(emp_frame,orient=HORIZONTAL)

    sup_table=ttk.Treeview(sup_frame,columns=("invoice","name","contact","description"))
                           # ,yscrollcommand=scrolly.set,
                           # xscrollcommand=scrollx.set)


    # scrollx.pack(side=BOTTOM,fill=X)
    # scrolly.pack(side=RIGHT,fill=Y)
    # scrollx.config(command=emp_table.xview)
    # scrolly.config(command=emp_table.yview)

    sup_table.heading("invoice",text="Invoice")
    sup_table.heading("name", text="Name")
    sup_table.heading("contact",text="Contact")
    sup_table.heading("description", text="Description")
    
    sup_table["show"]="headings"

    sup_table.column("invoice",width=10)
    sup_table.column("name",width=20)
    sup_table.column("contact",width=50)
    sup_table.column("description",width=20)
    
    sup_table.pack(fill=BOTH,expand=1)
    sup_table.bind("<ButtonRelease-1>",get_tabledata)

    sup_show()
    
# ========================================================
    
# category page

def show_category_page():
    # # Create a new frame for the employee page
    supplier_frame = Frame(root, border=2, relief=RIDGE, bg="white")
    supplier_frame.place(x=200, y=102, width=1150, height=520)

    # ===================variables================

    var_cat_id = StringVar()
    var_cat_name = StringVar()

    # =============title=====================
    
    cat_title =Label(root,text="Manage Product Category",font=("Times new roman",20,"bold"),bg="skyblue",
                 fg="Black")
    cat_title.place(x=240,y=120,width=1000,height=40)

    cat_name =Label(root,text="Enter Category Name",font=("Times new roman",20),bg="White",
                 fg="Black")
    cat_name.place(x=210,y=180,width=400,height=40)

    txt_name=Entry(root,textvariable=var_cat_name,font=("Times new roman",18),bg="lightyellow",
                 fg="Black")
    txt_name.place(x=290,y=230,width=300)

# ======================================================================
    def cat_add():
       conn = sqlite3.connect("IMS.db")
       cursor = conn.cursor()
    #    cursor.execute('''
    #                   Create table category1(
    #                   cid INTEGER PRIMARY KEY AUTOINCREMENT,
    #                   name VARCHAR(30)
    #                 ) 
    #                ''')
       
       if var_cat_name.get() == "":
          messagebox.showerror("Error", "Category should be required")
       else:
        try:
           conn.execute("Select * from category1 where name=?", (var_cat_name.get(),))
           rows=cursor.fetchone()
           if rows!=None:
               messagebox.showerror("Error","Category already present, try different")
           else:
               conn.execute('''
               INSERT INTO category1 (name)
               VALUES (?)
           ''', (
               var_cat_name.get(),
            #    var_cat_id.get()
           ))
               conn.commit()
               messagebox.showinfo("Success", "Category added successfully.")
               cat_show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")


    #    empid = var_emp_id.get()
    #    if not empid:
    #        # Show an error message or handle it as needed
    #        messagebox.showerror("Error", "Employee ID is required.")
    #        return

       # Connect to SQLite database (replace 'your_database.db' with your actual database name)
      #  conn = sqlite3.connect('data.db')

    #    try:
    #        conn.execute('''
    #            INSERT INTO cate (name)
    #            VALUES (?)
    #        ''', (
    #            var_cat_name.get(),
    #        ))

    #        conn.commit()
    #        messagebox.showinfo("Success", "Category added successfully.")
    #        cat_show()
    #    except Exception as e:
    #        messagebox.showerror("Error", f"An error occurred: {str(e)}")
    #    finally:
    #        # Close the connection
    #        conn.close()
# =============================================================
    def cat_show():
        conn = sqlite3.connect("IMS.db")
        # cur=conn.cursor()
        cursor = conn.cursor()

        try:
           cursor.execute("SELECT * FROM category1")
           rows = cursor.fetchall()
        
        # Assuming Emp1 is a ttk.Treeview widget, you need to replace Emp1 with your actual Treeview widget instance
           cat_table.delete(*cat_table.get_children())

           for row in rows:
             cat_table.insert('', 'end', values=row)

        except Exception as ex:
           messagebox.showerror("Error", f"Error due to: {str(ex)}")
        finally:
           conn.close()

# =================================================
    def get_tabledata(ev):
       f=cat_table.focus()
       content=(cat_table.item(f))
       row=content['values']
    #    print(row)

       var_cat_id.set(row[0]),
       var_cat_name.set(row[1])   

# ===========================================
    def cat_delete():
       conn = sqlite3.connect("IMS.db")
       try:
          if var_cat_name.get() == "":
                  messagebox.showerror("Error", "Please select the category form the list")
          else:
            # Fetch the row
                  cursor = conn.execute("SELECT * FROM category1 WHERE name=?", (var_cat_name.get(),))
                  row = cursor.fetchone()

                  if row is None:
                    messagebox.showerror("Error", "Please try again")
                  else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?")
                    if op==True:
                      cursor.execute("DELETE FROM category1 WHERE name=?", (var_cat_name.get(),))

                      conn.commit()
                      messagebox.showinfo("Delete","Category Deleted Successfully")
                      
                      cat_show()
                      var_cat_id.set("")
                      var_cat_name.set("")
       except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


    # ===========Button======================
    #   Add Button
    btn_add=Button(root,text="ADD",font=("Times new roman",15),bg="lightgreen",
                 fg="Black",cursor="hand2",command=cat_add)
    btn_add.place(x=600,y=230,width=120,height=30)
    

    # Delete Button
    btn_delete=Button(root,text="Delete",font=("Times new roman",15),bg="lightgreen",
                 fg="Black",cursor="hand2",command=cat_delete)
    btn_delete.place(x=740,y=230,width=120,height=30)

# =================Category Detail ==================
    cat_frame = Frame(root,bd=3,relief=RIDGE,bg="white")
    cat_frame.place(x=870,y=220,width=400,height=100)

    scrolly=Scrollbar(cat_frame,orient=VERTICAL)
    scrollx= Scrollbar(cat_frame,orient=HORIZONTAL)

    cat_table=ttk.Treeview(cat_frame,columns=("cid","name"),yscrollcommand=scrolly.set,
                           xscrollcommand=scrollx.set)


    scrollx.pack(side=BOTTOM,fill=X)
    scrolly.pack(side=RIGHT,fill=Y)
    scrollx.config(command=cat_table.xview)
    scrolly.config(command=cat_table.yview)

    cat_table.heading("cid",text="Category ID")
    cat_table.heading("name", text="Name")
    

    cat_table["show"]="headings"

    cat_table.column("cid",width=10)
    cat_table.column("name",width=20)
   
    cat_table.pack(fill=BOTH)
    cat_table.bind("<ButtonRelease-1>",get_tabledata)

    # ===========images=============
    img1=Image.open("C:\\Users\\sai\\Desktop\\IMS\\inventory-management-icon-15.jpg")
    img1=img1.resize((500,200),Image.ADAPTIVE)
    img1=ImageTk.PhotoImage(img1)

    lable_img1=Label(root,image=img1,bd=2,relief=RAISED)
    lable_img1.place(x=250,y=400)



    img2=Image.open("C:\\Users\\sai\\Desktop\\Project\\inventory-management-icon-15.jpg")
    img2=img2.resize((500,200),Image.ADAPTIVE)
    img2=ImageTk.PhotoImage(img2)

    lable_img2=Label(root,image=img2,bd=2,relief=RAISED)
    lable_img2.place(x=760,y=400)

    cat_show()

    
    
# =============================================================
    # Product page

def show_product_page():
    # Create a new frame for the product page
    product_frame = Frame(root, border=2, relief=RIDGE, bg="white")
    product_frame.place(x=200, y=102, width=1150, height=520)

    s_frame=Frame(product_frame,border=3, relief=RIDGE, bg="white")
    s_frame.place(x=20,y=20,width=450,height=480)

    # root.focus_force()

    # ==============Variables=============
     
    var_searchtxt=StringVar()
    var_serachby=StringVar()

    var_prod_pid=StringVar()

    cat_list=[]
    sup_list=[]
    
    var_prod_category=StringVar()
    var_prod_supplier=StringVar()
    var_prod_name=StringVar()
    var_prod_price=StringVar()
    var_prod_quantity=StringVar()
    var_prod_status=StringVar()

    # ================title===================

    product_title =Label(s_frame,text=" Manage Product Details",font=("Times new roman",20,"bold"),
                         bg="skyblue",fg="Black")
    product_title.pack(side=TOP,fill=X)

    # ==============label====================
    #  column 1
    label_category =Label(s_frame,text="Category",font=("Times new roman",20),bg="white")
    label_category.place(x=30,y=60)

    label_Supplier =Label(s_frame,text="Supplier",font=("Times new roman",20),bg="white")
    label_Supplier.place(x=30,y=110)

    label_product =Label(s_frame,text="Name",font=("Times new roman",20),bg="white")
    label_product.place(x=30,y=160)

    label_price =Label(s_frame,text="Price",font=("Times new roman",20),bg="white")
    label_price.place(x=30,y=210)

    label_quantity =Label(s_frame,text="Quantity",font=("Times new roman",20),bg="white")
    label_quantity.place(x=30,y=260)

    label_status =Label(s_frame,text="Status",font=("Times new roman",20),bg="white")
    label_status.place(x=30,y=310)

# ========Entry===============     
#    column 2
    cmb_product_cat=ttk.Combobox(s_frame,textvariable=var_prod_category,values=cat_list,
                        state="readonly",justify=CENTER,font=("Arial",14))
    cmb_product_cat.place(x=150,y=60,width=200)
    # cmb_product_cat.current(0)


    cmb_product_sup=ttk.Combobox(s_frame,textvariable=var_prod_supplier,values=sup_list,
                        state="readonly",justify=CENTER,font=("Arial",14))
    cmb_product_sup.place(x=150,y=100,width=200)
    # cmb_product_sup.current(0)


    txt_product_name=Entry(s_frame,textvariable=var_prod_name,font=("Arial",14),bg="lightyellow")
    txt_product_name.place(x=150,y=160,width=200)

    txt_product_price=Entry(s_frame,textvariable=var_prod_price,font=("Arial",14),bg="lightyellow")
    txt_product_price.place(x=150,y=210,width=200)

    txt_product_quantity=Entry(s_frame,textvariable=var_prod_quantity,font=("Arial",14),bg="lightyellow")
    txt_product_quantity.place(x=150,y=260,width=200)


    cmb_product_status=ttk.Combobox(s_frame,textvariable=var_prod_status,values=("Active","Inactive"),
                        state="readonly",justify=CENTER,font=("Arial",14))
    cmb_product_status.place(x=150,y=310,width=200)
    cmb_product_status.current(0)

    

# ==========================================================

    def fetch_cat_supp():
        nonlocal cat_list, sup_list  # Declare as nonlocal to modify outer variables
        conn = sqlite3.connect("IMS.db")
        cur = conn.cursor()

        try:
            cur.execute("Select name From category1")
            cat = cur.fetchall()

            if len(cat) > 0:
                cat_list = ["Select"] + [i[0] for i in cat]

            cur.execute("SELECT name FROM supplier")
            sup = cur.fetchall()

            if len(sup) > 0:
                sup_list = ["Select"] + [i[0] for i in sup]

            # Configuring combo boxes after populating lists
            cmb_product_cat.config(values=cat_list)
            cmb_product_sup.config(values=sup_list)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    # Call fetch_cat_supp to populate combo box values
    fetch_cat_supp()

# ====================================================================================

    def prod_add():
       conn = sqlite3.connect("IMS.db")
    #    conn.execute('''
    #                   Create table product(
    #                   pid INTEGER PRIMARY KEY AUTOINCREMENT,
    #                   Category VARCHAR(30),
    #                   Supplier VARCHAR(30),
    #                   name VARCHAR(10),
    #                   price INT(15),
    #                   qty VARCHAR(20),
    #                   status VARCHAR(10))
                  
    #                ''')
       
       if var_prod_category.get() == "Select"  or var_prod_supplier.get()=="Select" or var_prod_name.get()=="":
          messagebox.showerror("Error", "All fields are required")
       else:
        try:
           conn.execute("Select * from product where name=?", (var_prod_name.get(),))
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")


    #    empid = var_emp_id.get()
    #    if not empid:
    #        # Show an error message or handle it as needed
    #        messagebox.showerror("Error", "Employee ID is required.")
    #        return

       # Connect to SQLite database (replace 'your_database.db' with your actual database name)
      #  conn = sqlite3.connect('data.db')

       try:
           conn.execute('''
               INSERT INTO product (Category, Supplier, name, price, qty, status)
               VALUES (?, ?, ?, ?, ?, ?)
           ''', (
               
               var_prod_category.get(),
               var_prod_supplier.get(),
               var_prod_name.get(),
               var_prod_price.get(),
               var_prod_quantity.get(),
               var_prod_status.get(),
               
           ))

           conn.commit()
           messagebox.showinfo("Success", "Product added successfully.")
           prod_show()
       except Exception as e:
           messagebox.showerror("Error", f"An error occurred: {str(e)}")
       finally:
           # Close the connection
           conn.close()


#    ===========================================
# data show in table
    def prod_show():
        conn = sqlite3.connect("IMS.db")
        # cur=conn.cursor()
        cursor = conn.cursor()

        try:
           cursor.execute("SELECT * FROM product")
           rows = cursor.fetchall()
        
        # Assuming Emp1 is a ttk.Treeview widget, you need to replace Emp1 with your actual Treeview widget instance
           product_table.delete(*product_table.get_children())

           for row in rows:
            product_table.insert('', 'end', values=row)

        except Exception as ex:
        #    messagebox.showerror("Error", f"Error due to: {str(ex)}")
        # finally:
           conn.close()    

# =============================================
#        # data show in forms rows   
    def get_prod_data(ev):

        f=product_table.focus()
        content=(product_table.item(f))
        row=content['values']
    #    print(row)
       
        var_prod_pid.set(row[0]),
        var_prod_category.set(row[1]),
        var_prod_supplier.set(row[2]),
        var_prod_name.set(row[3]),
        var_prod_price.set(row[4]),
        var_prod_quantity.set(row[5]),
        var_prod_status.set(row[6])

        prod_show()

# # ==================================================
#  update data    
    def prod_update():
            conn = sqlite3.connect("IMS.db")
            try:
               if var_prod_pid.get() == "":
                  messagebox.showerror("Error", "please select product from list")
               else:
            # Fetch the row
                  cursor = conn.execute("SELECT * FROM product WHERE pid=?", (var_prod_pid.get(),))
                  row = cursor.fetchone()

                  if row is None:
                    messagebox.showerror("Error", "Invalid product")
                  else:
                # Update the row
                      conn.execute('''
                      UPDATE product SET Category=?, Supplier=?, name=?, price=?, qty=?, status=?
                                    WHERE pid=? ''', (
                                       var_prod_category.get(),
                                       var_prod_supplier.get(),
                                       var_prod_name.get(),
                                       var_prod_price.get(),
                                       var_prod_quantity.get(),
                                       var_prod_status.get(),
                                       var_prod_pid.get()
                                    ))

                      conn.commit()
                      messagebox.showinfo("Success", "Employee data updated successfully.")
                      prod_show()
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
            

# # =====================================================
# # delete data from table
    def prod_delete():
       conn = sqlite3.connect("IMS.db")
       try:
          if var_prod_pid.get() == "":
                  messagebox.showerror("Error", "Select product from the list")
          else:
            # Fetch the row
                  cursor = conn.execute("SELECT * FROM product WHERE pid=?", (var_prod_pid.get(),))
                  row = cursor.fetchone()

                  if row is None:
                    messagebox.showerror("Error", "Invalid product")
                  else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?")
                    if op==True:
                      cursor.execute("delete from product where pid=?",(var_prod_pid.get(),))
                      conn.commit()
                      messagebox.showinfo("Delete","Product Deleted Successfully")
                      
                      prod_clear()
       except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")            

# =================================================================
            
    def prod_clear():

        var_prod_category.set(""),
        var_prod_supplier.set(""),
        var_prod_name.set(""),
        var_prod_price.set(""),
        var_prod_quantity.set(""),
        var_prod_status.set(""),
        var_prod_pid.set(""),

        var_searchtxt.set(""),
        var_serachby.set("")
       
        prod_show()
# ====================================================
    def search_product():
      conn = sqlite3.connect("IMS.db")
      cursor = conn.cursor()

      try:
        search_field = var_serachby.get()
        search_text = var_searchtxt.get()

        if search_field == "select":
            messagebox.showerror("Error", "Select Search By Option")
            return

        if not search_text:
            messagebox.showerror("Error", "Search input should be required")
            return

        if search_field not in ["Name", "Category", "Supplier"]:
            messagebox.showerror("Error", f"Invalid search field '{search_field}'")
            return
        query = "SELECT * FROM product WHERE {} LIKE ?".format(search_field)
        cursor.execute(query, ('%' + search_text + '%',))
        rows = cursor.fetchall()

        if len(rows) != 0:
               product_table.delete(*product_table.get_children())
        for row in rows:
                product_table.insert('', 'end', values=row)
        
            

      except Exception as ex:
        messagebox.showerror("Error", f"Error due to: {str(ex)}")
      finally:
        conn.close()
 


# ==========Button=============
    
# Save button
    btn_add = Button(s_frame, text="Save", font=("Arial", 14), bg="lightgreen", fg="black",
                        cursor="hand2",command=prod_add)
    btn_add.place(x=20, y=400, width=90, height=35)

# Update Button
    btn_update = Button(s_frame, text="Update", font=("Arial", 14), bg="lightgreen", fg="black",
                     cursor="hand2",command=prod_update)
    btn_update.place(x=130, y=400, width=90, height=35)


#   Delete Button
    btn_delete = Button(s_frame, text="Delete", font=("Arial", 14), bg="lightgreen", fg="black",
                     cursor="hand2",command=prod_delete)
    btn_delete.place(x=240, y=400, width=90, height=35)

#     Clear Button
    btn_clear = Button(s_frame, text="Clear", font=("Arial", 14), bg="lightgreen", fg="black",
                     cursor="hand2",command=prod_clear)
    btn_clear.place(x=350, y=400, width=90, height=35)

# SEARCH FRaAME==========================
    searchframe=LabelFrame(root,text="Search Employee",font=("Times new Roman",14,"bold"),
                          bg="white",bd=3,relief=RIDGE, )
    searchframe.place(x=690,y=120,width=570,height=70)

#     Options
    search=ttk.Combobox(searchframe,textvariable=var_serachby,values=("Select","Category","Supplier","Name"),
                        state="readonly",justify=CENTER,font=("Arial",14))
    search.place(x=10,y=10,width=200)
    search.current(0)

    txt_search=Entry(searchframe,textvariable=var_searchtxt,font=("Arial",14),bg="lightyellow")
    txt_search.place(x=220,y=10,width=200)

    btn_search=Button(searchframe,text="Search",font=("Arial",14),bg="lightgreen",fg="black",
                      cursor="hand2",command=search_product)
    btn_search.place(x=435,y=9,width=120,height=29)

    # ===========================================
#     Product details
    
    product_frame = Frame(root,bd=3,relief=RIDGE,bg="white")
    product_frame.place(x=690,y=200,width=570,height=200)

    # scrolly=Scrollbar(emp_frame,orient=VERTICAL)
    # scrollx= Scrollbar(emp_frame,orient=HORIZONTAL)

    product_table=ttk.Treeview(product_frame,columns=("pid","Category","Supplier","name","price","qty","status"))
                           # ,yscrollcommand=scrolly.set,
                           # xscrollcommand=scrollx.set)


    # scrollx.pack(side=BOTTOM,fill=X)
    # scrolly.pack(side=RIGHT,fill=Y)
    # scrollx.config(command=emp_table.xview)
    # scrolly.config(command=emp_table.yview)

    product_table.heading("pid",text="P ID")
    product_table.heading("Category", text="Category")
    product_table.heading("Supplier",text="Supplier")
    product_table.heading("name", text="Name")
    product_table.heading("price", text="Price")
    product_table.heading("qty", text="qTY")
    product_table.heading("status", text="Status")
    

    product_table["show"]="headings"

    product_table.column("pid",width=10)
    product_table.column("Category",width=20)
    product_table.column("Supplier",width=50)
    product_table.column("name",width=20)
    product_table.column("price",width=40)
    product_table.column("qty",width=20)
    product_table.column("status",width=20)
    
    product_table.pack(fill=BOTH)
    product_table.bind("<ButtonRelease-1>",get_prod_data)

    prod_show()
    
    fetch_cat_supp()


# ===================================================================
def show_sales_page():

    # Create a new frame for the product page
    sales_frame = Frame(root, border=2, relief=RIDGE, bg="white")
    sales_frame.place(x=200, y=102, width=1150, height=520)

    # ============Variable==============

    var_invoice=StringVar()
    bill_list=[]

    # =====================================================
    # ======================================================

    sales_title =Label(sales_frame,text="View Customer Bill ",font=("Times new roman",20,"bold"),bg="skyblue",
                 fg="Black")
    sales_title.place(x=20,y=20,width=1000,height=40)

    invoice_label=Label(sales_frame,text="Invoice No",font=("Times new roman",20),bg="White")
    invoice_label.place(x=50,y=90)

    txt_invoice_label=Entry(sales_frame,textvariable=var_invoice,font=("Times new roman",15),bg="lightyellow")
    txt_invoice_label.place(x=190,y=90,height=30)


    # ===========Button===========


    btn_search=Button(sales_frame,text="Search",font=("Arial",14),bg="lightgreen",fg="black",
                      cursor="hand2")
    btn_search.place(x=410,y=90,width=90,height=31)

    
    btn_clear=Button(sales_frame,text="Clear",font=("Arial",14),bg="lightgreen",fg="black",
                      cursor="hand2")
    btn_clear.place(x=520,y=90,width=90,height=31)

    # ========Frame==================

    s_frame=Frame(sales_frame,border=3, relief=RIDGE, bg="white")
    s_frame.place(x=50,y=150,width=200,height=330)
    


    # ======================Bill List=============

    scrolly=Scrollbar(s_frame,orient=VERTICAL) 
    
    sales_list=Listbox(s_frame,font=("Times new roman",15),bg="white",yscrollcommand=scrolly.set)
    scrolly.pack(side=RIGHT,fill=Y)
    scrolly.config(command=sales_list.yview)
    sales_list.pack(fill=BOTH,expand=1)

    # ===============Bill Area===========

    bill_frame=Frame(sales_frame,border=3, relief=RIDGE, bg="white")
    bill_frame.place(x=280,y=150,width=410,height=330)

    bill_title=Label(bill_frame,text="Customer Bill Area",font=("Times new roman",20,"bold"),bg="skyblue",
                 fg="Black")
    bill_title.pack(side=TOP,fill=X)

    scrolly2=Scrollbar(bill_frame,orient=VERTICAL) 
    
    bill_area=Text(bill_frame,bg="lightyellow",yscrollcommand=scrolly2.set)
    scrolly2.pack(side=RIGHT,fill=Y)
    scrolly2.config(command=bill_area.yview)
    bill_area.pack(fill=BOTH,expand=1)
    


    # sales_list.bind("<ButtonRelease-1>", get_data_bill(sales_list,bill_area))
    # sales_list.bind("<ButtonRelease-1>", lambda ev: get_data_bill(sales_list, bill_area, bill_list,ev))

    # ==========Image===========
    # bill_photo = Image.open("C:\\Users\\sai\\Desktop\\IMS Website\\images.jpg")
    # bill_photo = menulogo.resize((450,300),Image.ADAPTIVE)
    # bill_photo = ImageTk.PhotoImage(bill_photo)

    # bill_image=Label(sales_frame,image=bill_photo)
    # bill_image.pack(side=RIGHT)

    bill_show(sales_list,bill_list)

    sales_list.bind("<ButtonRelease-1>", lambda ev: get_data_bill(sales_list, bill_area, bill_list, ev))   
    btn_search.bind("<ButtonRelease-1>", lambda ev: search_bill(var_invoice, bill_area, bill_list))
    btn_clear.bind("<ButtonRelease-1>", lambda ev: clear_bill(sales_list, bill_area, bill_list))
# =============================================
    
def bill_show(sales_list,bill_list):
    del bill_list[:]
    sales_list.delete(0,END)
    for i in os.listdir('bill'):
        if i.split('.')[-1]=='txt':
            sales_list.insert(END,i)
            bill_list.append(i.split('.')[0])
    

def get_data_bill(sales_list, bill_area,bill_list,ev): # Pass bill_list as an argument
    index_=sales_list.curselection()
    file_name=sales_list.get(index_)
    # print(file_name)
    
    bill_area.delete('1.0', END)

    # if file_name+'.txt' in bill_list: # Check if the file name is in the bill_list
    fp=open(f'bill/{file_name}','r')
    for i in fp:
            bill_area.insert(END,i)
    fp.close()


def search_bill(var_invoice,bill_area,bill_list):
    if var_invoice.get()=="":
        messagebox.showerror("Error","Invoice no should be required")
    else:
        if var_invoice.get() in bill_list:
            # print("Yes find the invoice")
            p=open(f"bill/{var_invoice.get()}.txt",'r')
            bill_area.delete('1.0',END)
            for i in p:
                bill_area.insert(END,i)
            p.close()
        else:
            messagebox.showerror("Error","Invalid Invoice No")

# def clear_bill(bill_area,ev):
#     bill_show()
#     bill_area.delete('1.0',END)
            
def clear_bill(sales_list, bill_area, bill_list):
    bill_show(sales_list, bill_list)
    bill_area.delete('1.0', END)
# ====================================================================
   #Logout 
    
def logout():
    root.destroy()
    os.system("python Login.py")

def close_window():
    root.destroy()
    os.system("python project.py")
 
# ==============================================================
root = Tk()
root.geometry("1350x700+0+0")

# icon = Image.open("C:\\Users\\sai\\Downloads\\icon.png")
# icon_label = Label(image=icon,compound=LEFT)

root.title("Warehouse Stock Management System ")
root.config(bg="White")

title = Label(root,text="Warehouse Stock Management System",font=("times new roman",40,"bold"),
              bg="skyblue",fg="black",anchor="w",padx=20)
title.place(x=0,y=0,relwidth=1,height=70)
# icon_label.pack()

# Logout button

btn = Button(root,text="Logout",command=logout,font=("times new roman",15,"bold"),bg="yellow",cursor="hand2")
btn.place(x=1100,y=10,height=50,width=150)

# clock
clock = Label(root,text="Welcome to Warehouse Stock Management System\t\t Date:DD-MM-YYYY\t\t Time:HH:MM:SS",
              font=("times new roman",18), bg="grey",fg="white")
clock.place(x=0,y=70,relwidth=1,height=30)

# menu
menulogo = Image.open("C:\\Users\\sai\\Documents\\Downloads\\inventory-management-icon-15.jpg")
menulogo = menulogo.resize((200,200),Image.ADAPTIVE)
logo = ImageTk.PhotoImage(menulogo)

leftmenu= Frame(root,border=2,relief=RIDGE,bg="white")
leftmenu.place(x=0,y=102,width=200,height=520)

label_menulogo = Label(leftmenu,image=logo)
label_menulogo.pack(side=TOP,fill=X)

btnmenu = Label(leftmenu,text="Menu",font=("times new roman",18,),bg="Red")
btnmenu.pack(side=TOP,fill=X)

btn_emp = Button(leftmenu,text="Employee",font=("times new roman",17,"bold"),bg="White",
                 bd=3,cursor="hand2",command=show_employee_page)
btn_emp.pack(side=TOP,fill=X)

btn_supplier = Button(leftmenu,text="Supplier",font=("times new roman",17,"bold"),bg="White",
                 bd=3,cursor="hand2",command=show_supplier_page)
btn_supplier.pack(side=TOP,fill=X)

btn_category = Button(leftmenu,text="Category",font=("times new roman",17,"bold"),bg="White",
                 bd=3,cursor="hand2",command=show_category_page)
btn_category.pack(side=TOP,fill=X)

btn_product = Button(leftmenu,text="Product",font=("times new roman",17,"bold"),bg="White",
                 bd=3,cursor="hand2",command=show_product_page)
btn_product.pack(side=TOP,fill=X)

btn_sales = Button(leftmenu,text="Sales",font=("times new roman",17,"bold"),bg="White",
                 bd=3,cursor="hand2",command=show_sales_page)
btn_sales.pack(side=TOP,fill=X)

btn_exit = Button(leftmenu,text="Exit",command=close_window,font=("times new roman",17,"bold"),bg="White",
                 bd=3,cursor="hand2")
btn_exit.pack(side=TOP,fill=X)


# ==============================================================================

def update_content():
    conn=sqlite3.connect("IMS.db")
    cur=conn.cursor()
    try:
        cur.execute("select * from product")
        product=cur.fetchall()
        product_label.config(text=f"Total Product\n[ {str(len(product))} ]")

        cur.execute("select * from supplier")
        supplier=cur.fetchall()
        supplier_label.config(text=f"Total Supplier\n[ {str(len(supplier))} ]")

        cur.execute("select * from category1")
        category=cur.fetchall()
        category_label.config(text=f"Total Category\n[ {str(len(category))} ]")

        cur.execute("select * from employee")
        employee=cur.fetchall()
        emp_label.config(text=f"Total Employee\n[ {str(len(employee))} ]")

        bill=len(os.listdir('bill'))
        sales_label.config(text=f"Total Sales\n[ {str(bill)} ]")

        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d-%m-%Y")
        clock.config(text=f"Welcome to Warehouse Stock Management System\t\t Date:{str(date_)}\t\t Time:{str(time_)}")

        clock.after(200,update_content)

    except Exception as e:
        conn.close()

    

# ===============================================================================


# Content
emp_label = Label(root,text="Total Employee\n[ 0 ]",bg="skyblue",fg="black",font=("Times New Roman",20,"bold"),
                 bd=5,relief=RIDGE)
emp_label.place(x=250,y=120,height=120,width=250)

supplier_label = Label(root,text="Total Supplier\n[ 0 ]",bg="skyblue",fg="black",font=("Times New Roman",20,"bold"),
                 bd=5,relief=RIDGE)
supplier_label.place(x=550,y=120,height=120,width=250)

category_label = Label(root,text="Total Category\n[ 0 ]",bg="skyblue",fg="black",font=("Times New Roman",20,"bold"),
                 bd=5,relief=RIDGE)
category_label.place(x=850,y=120,height=120,width=250)

product_label = Label(root,text="Total Product\n[ 0 ]",bg="skyblue",fg="black",font=("Times New Roman",20,"bold"),
                 bd=5,relief=RIDGE)
product_label.place(x=250,y=300,height=120,width=250)

sales_label = Label(root,text="Total Sales\n[ 0 ]",bg="skyblue",fg="black",font=("Times New Roman",20,"bold"),
                 bd=5,relief=RIDGE)
sales_label.place(x=550,y=300,height=120,width=250)


# footer
footer = Label(root,text="Warehouse Stock Management System", font=("times new roman",14,),
              bg="grey",fg="white")
footer.place(x=0,y=618,relwidth=1,height=30)

update_content()

root.mainloop()