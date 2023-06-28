import tkinter as tk
import calendar

def show_calendar(year, month):
    cal = calendar.month(year, month)
    label.config(text=cal)

root = tk.Tk()
root.title("달력")

year_label = tk.Label(root, text="년도")
year_label.pack()

year_entry = tk.Entry(root)
year_entry.pack()

month_label = tk.Label(root, text="월")
month_label.pack()

month_entry = tk.Entry(root)
month_entry.pack()

button = tk.Button(root, text="보기", command=lambda: show_calendar(int(year_entry.get()), int(month_entry.get())))
button.pack()

label = tk.Label(root)
label.pack()

root.mainloop()
