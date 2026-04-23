import tkinter as tk
import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    username TEXT,
    password TEXT
)
""")
conn.commit()

def signup():
    u = user_entry.get()
    p = pass_entry.get()

    cursor.execute("INSERT INTO users VALUES(?,?)", (u,p))
    conn.commit()
    status.config(text="Signup Successful")
def login():
    u = user_entry.get()
    p = pass_entry.get()

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (u,p))
    result = cursor.fetchone()

    if result:
        status.config(text="Login Successful")
    else:
        status.config(text="Invalid Credentials")

root = tk.Tk()
root.title("Login System")
root.geometry("300x200")

tk.Label(root, text="Username").pack()
user_entry = tk.Entry(root)
user_entry.pack()

tk.Label(root, text="Password").pack()
pass_entry = tk.Entry(root, show="*")
pass_entry.pack()

tk.Button(root, text="Login", command=login).pack(pady=5)
tk.Button(root, text="Signup", command=signup).pack()

status = tk.Label(root, text="")
status.pack()

root.mainloop()