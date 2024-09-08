import tkinter as tk
import time as t
root = tk.Tk()
root.title("Digital Clock")
root.configure(bg = "light yellow")
root.minsize(400, 200)
root.geometry("400x200")

label0 = tk.Label(root, bg="light yellow", font=("Fixedsys", 60))
label1 = tk.Label(root, bg="light yellow", font=("Fixedsys", 30))
def update_time():
    now = t.strftime("%H:%M:%S")
    label0.config(text=now)
    root.after(1000, update_time)

def update_date():
    today = t.strftime("%Y-%m-%d")
    label1.config(text=today)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

label0.grid(row=0, column=0, sticky="nsew")
label1.grid(row=1, column=0, sticky="nsew")

update_time()
update_date()
root.mainloop()