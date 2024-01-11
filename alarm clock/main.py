import tkinter as tk
from tkinter import Entry, Label, Button, messagebox
import os
import time
import winsound

def create_widgets():
    """
    Create and configure the GUI widgets.
    """
    label1 = Label(root, text="Enter the time in hh:mm: ")
    label1.grid(row=0, column=0, padx=5, pady=5)

    global entry1
    entry1 = Entry(root, width=15)
    entry1.grid(row=0, column=1)

    label2 = Label(root, text="Enter the message of alarm:")
    label2.grid(row=1, column=0, padx=5, pady=5)

    global entry2
    entry2 = Entry(root, width=15)
    entry2.grid(row=1, column=1)

    but = Button(root, text="submit", width=10, command=submit)
    but.grid(row=2, column=1)

    global label3
    label3 = Label(root, text="")
    label3.grid(row=3, column=0)

def message1():
    """
    Display a message box indicating that the alarm is counting.
    """
    global entry1, label3
    alarm_time_label = entry1.get()
    label3.config(text="The alarm is counting...")
    messagebox.showinfo("Alarm clock", f"the alarm time is: {alarm_time_label}")

def submit():
    """
    Set the alarm time and message, then initiate the alarm countdown.
    """
    global entry1, entry2, label3
    alarm_time = entry1.get()
    message1()
    current_time = time.strftime("%H:%M")
    alarm_message = entry2.get()
    print(F"The alarm time is : {alarm_time}")

    while alarm_time != current_time:
        current_time = time.strftime("%H:%M")
        time.sleep(1)
    
    if alarm_time == current_time:
        print("Playing alarm sound...")
        winsound.PlaySound('*', winsound.SND_ASYNC)
        label3.config(text="Alarm sound playing")
        messagebox.showinfo("Alarm message", f"Message: {alarm_message}")

# Create and configure the main Tkinter window
root = tk.Tk()
root.title("Alarm Clock")
root.geometry("400x150")

# Initialize and run the GUI
create_widgets()
root.mainloop()
