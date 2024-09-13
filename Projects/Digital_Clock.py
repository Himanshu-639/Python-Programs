import tkinter as tk
import datetime as dt
import pytz
from tkinter import ttk

root = tk.Tk()
root.title("Digital Clock")
root.configure(bg = "light yellow")
root.minsize(400, 200)
root.geometry("400x200")

time_frame = tk.Frame(root, bg="light yellow")
date_frame = tk.Frame(root, bg="light yellow")
timezone_frame = tk.Frame(root, bg="light yellow")

label0 = tk.Label(time_frame, bg="light yellow", font=("Fixedsys", 60))
label1 = tk.Label(date_frame, bg="light yellow", font=("Fixedsys", 30))

def update_time():
    tz = pytz.timezone(selected_timezone.get())
    now = dt.datetime.now(tz).strftime("%H:%M:%S")
    label0.config(text=now)
    root.after(1000, update_time)

def update_date():
    today = dt.datetime.now().strftime("%Y-%m-%d")
    label1.config(text=today)

def update_timezone_options(*args):
    timezone_options = pytz.all_timezones
    timezone_menu['values'] = timezone_options
    timezone_menu.set('Asia/Kolkata')
    timezone_menu.bind("<<ComboboxSelected>>", lambda event: update_time())

selected_timezone = tk.StringVar(root)
timezone_label = tk.Label(timezone_frame, text="Timezone : ", bg="light yellow", font=("Helvetica", 12))
timezone_menu = ttk.Combobox(timezone_frame, textvariable = selected_timezone)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)

for frame in [time_frame, date_frame, timezone_frame]:
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_rowconfigure(0,weight=1)

timezone_frame.grid(row=0, column=0, sticky="nsew")
time_frame.grid(row=1, column=0, sticky="nsew")
date_frame.grid(row=2, column=0, sticky="nsew")

timezone_label.grid(row=0, column=0, sticky="e", padx=5, pady=5)
timezone_menu.grid(row=0, column=1, sticky="w", padx=5, pady=5)

timezone_frame.grid_rowconfigure(0, weight=1)
timezone_frame.grid_columnconfigure(0, weight=1)
timezone_frame.grid_columnconfigure(1, weight=1)

label0.grid(row=0, column=0, sticky="nsew")
label1.grid(row=0, column=0, sticky="nsew")

update_timezone_options()
update_time()
update_date()

root.mainloop()