import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}

def GetValue(event):
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    e3.delete(0, tk.END)
    e4.delete(0, tk.END)
    row_id = listBox.selection()[0]
    select = listBox.item(row_id, "values")
    e1.insert(0, select[0])
    e2.insert(0, select[1])
    e3.insert(0, select[2])
    e4.insert(0, select[3])

def Add():
    studid, studname, coursename, feee = e1.get(), e2.get(), e3.get(), e4.get()
    try:
        mysqldb = mysql.connector.connect(**DB_CONFIG)
        mycursor = mysqldb.cursor()
        sql = "INSERT INTO registration (id, empname, mobile, salary) VALUES (%s, %s, %s, %s)"
        mycursor.execute(sql, (studid, studname, coursename, feee))
        mysqldb.commit()
        messagebox.showinfo("Information", "Employee inserted successfully!")
        clear_entries()
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        mysqldb.close()

def update():
    studid, studname, coursename, feee = e1.get(), e2.get(), e3.get(), e4.get()
    try:
        mysqldb = mysql.connector.connect(**DB_CONFIG)
        mycursor = mysqldb.cursor()
        sql = "UPDATE registration SET empname=%s, mobile=%s, salary=%s WHERE id=%s"
        mycursor.execute(sql, (studname, coursename, feee, studid))
        mysqldb.commit()
        messagebox.showinfo("Information", "Record updated successfully!")
        clear_entries()
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        mysqldb.close()

def delete():
    studid = e1.get()
    try:
        mysqldb = mysql.connector.connect(**DB_CONFIG)
        mycursor = mysqldb.cursor()
        sql = "DELETE FROM registration WHERE id=%s"
        mycursor.execute(sql, (studid,))
        mysqldb.commit()
        messagebox.showinfo("Information", "Record deleted successfully!")
        clear_entries()
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        mysqldb.close()

def show():
    try:
        mysqldb = mysql.connector.connect(**DB_CONFIG)
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT id, empname, mobile, salary FROM registration")
        records = mycursor.fetchall()
        listBox.delete(*listBox.get_children())
        for (id, stname, course, fee) in records:
            listBox.insert("", "end", values=(id, stname, course, fee))
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        mysqldb.close()

def clear_entries():
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    e3.delete(0, tk.END)
    e4.delete(0, tk.END)
    e1.focus_set()

# GUI setup
root = tk.Tk()
root.geometry("800x500")
root.title("Employee Management System")

tk.Label(root, text="Employee Registration", fg="red", font=(None, 30)).place(x=250, y=5)
tk.Label(root, text="Employee ID").place(x=10, y=50)
tk.Label(root, text="Employee Name").place(x=10, y=80)
tk.Label(root, text="Mobile").place(x=10, y=110)
tk.Label(root, text="Salary").place(x=10, y=140)

e1, e2, e3, e4 = tk.Entry(root), tk.Entry(root), tk.Entry(root), tk.Entry(root)
e1.place(x=140, y=50)
e2.place(x=140, y=80)
e3.place(x=140, y=110)
e4.place(x=140, y=140)

tk.Button(root, text="Add", command=Add, height=2, width=13).place(x=30, y=180)
tk.Button(root, text="Update", command=update, height=2, width=13).place(x=140, y=180)
tk.Button(root, text="Delete", command=delete, height=2, width=13).place(x=250, y=180)
tk.Button(root, text="Refresh", command=show, height=2, width=13).place(x=360, y=180)

cols = ('id', 'empname', 'mobile', 'salary')
listBox = ttk.Treeview(root, columns=cols, show='headings')
for col in cols:
    listBox.heading(col, text=col)
listBox.place(x=10, y=230, width=780, height=250)

listBox.bind('<Double-Button-1>', GetValue)

show()
root.mainloop()