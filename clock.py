import time
import tkinter as tk

def update_clock():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    root.after(1000, update_clock)

root = tk.Tk()
root.title("Digital Clock")
root.geometry("300x120")
root.configure(bg="black")

clock_label = tk.Label(
    root,
    text="",
    font=("Arial", 40, "bold"),
    fg="lime",
    bg="black"
)
clock_label.pack(expand=True)

update_clock()
root.mainloop()