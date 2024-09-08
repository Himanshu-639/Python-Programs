import tkinter as tk
import time as t
root = tk.Tk()
root.title("Time")
root.minsize(400, 200)

label = tk.Label(root, bg="light yellow", height=200, width=400, font=("Fixedsys", 40))
def update_time():
    now = t.strftime("%H:%M:%S")
    label.config(text=now)
    root.after(1000, update_time)

label.pack()
update_time()
root.mainloop()