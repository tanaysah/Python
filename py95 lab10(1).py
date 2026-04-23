#lab 10
import tkinter as tk

root = tk.Tk()
root.title("Simple Window")
root.geometry("400x300")
root.resizable(False, False)

label = tk.Label(root, text="Welcome to Tkinter GUI", font=("Arial", 14))
label.pack(pady=100)

root.mainloop()