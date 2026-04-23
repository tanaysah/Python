import tkinter as tk
import sqlite3

conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT
)
""")
conn.commit()

def load_tasks():
    listbox.delete(0, tk.END)
    for row in cursor.execute("SELECT * FROM tasks"):
        listbox.insert(tk.END, row[1])

def add_task():
    task = entry.get()
    cursor.execute("INSERT INTO tasks(task) VALUES(?)", (task,))
    conn.commit()
    load_tasks()

def delete_task():
    selected = listbox.curselection()
    if selected:
        task = listbox.get(selected)
        cursor.execute("DELETE FROM tasks WHERE task=?", (task,))
        conn.commit()
        load_tasks()

root = tk.Tk()
root.title("Task Manager")
root.geometry("400x400")

entry = tk.Entry(root)
entry.pack(fill='x')

tk.Button(root, text="Add Task", command=add_task).pack()

listbox = tk.Listbox(root)
listbox.pack(fill='both', expand=True)

tk.Button(root, text="Delete Task", command=delete_task).pack()

load_tasks()
root.mainloop()