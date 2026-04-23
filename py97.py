import tkinter as tk
import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    course TEXT
)
""")
conn.commit()

def register():
    name = name_entry.get()
    email = email_entry.get()
    course = course_entry.get()

    cursor.execute("INSERT INTO students(name,email,course) VALUES(?,?,?)",
                   (name, email, course))
    conn.commit()

    status.config(text="Registered Successfully")

root = tk.Tk()
root.title("Student Registration")
root.geometry("400x300")

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Course").pack()
course_entry = tk.Entry(root)
course_entry.pack()

tk.Button(root, text="Register", command=register).pack(pady=10)

status = tk.Label(root, text="")
status.pack()

root.mainloop()