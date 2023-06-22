# monitor = tech with tim
# identify = missing object
# in out = facial recognition
# record = normal record
import tkinter as tk
import tkinter.font as font
from monitor import monitor
from record import record
from identify import identify
from face_rec import maincall
from PIL import Image, ImageTk
# from authorize import authorize
window = tk.Tk()
window.title("Smart CCTV")
window.iconphoto(False, tk.PhotoImage(file='mn.png'))
window.geometry('1080x700')


frame1 = tk.Frame(window)

label_title = tk.Label(frame1, text="SMART-CCTV")
label_font = font.Font(size=35, weight='bold', family='Helvetica')
label_title['font'] = label_font
label_title.grid(pady=(10, 10), column=2)


icon = Image.open('icons/spy.png')
icon = icon.resize((150, 150), Image.Resampling.LANCZOS)
icon = ImageTk.PhotoImage(icon)
label_icon = tk.Label(frame1, image=icon)
label_icon.grid(row=1, pady=(5, 10), column=2)

btn1_image = Image.open('icons/Monitor.png')
btn1_image = btn1_image.resize((50, 50), Image.Resampling.LANCZOS)
btn1_image = ImageTk.PhotoImage(btn1_image)

btn5_image = Image.open('icons/exit.png')
btn5_image = btn5_image.resize((50, 50), Image.Resampling.LANCZOS)
btn5_image = ImageTk.PhotoImage(btn5_image)

btn6_image = Image.open('icons/incognito.png')
btn6_image = btn6_image.resize((50, 50), Image.Resampling.LANCZOS)
btn6_image = ImageTk.PhotoImage(btn6_image)

btn4_image = Image.open('icons/rec.png')
btn4_image = btn4_image.resize((50, 50), Image.Resampling.LANCZOS)
btn4_image = ImageTk.PhotoImage(btn4_image)

btn7_image = Image.open('icons/main.png')
btn7_image = btn7_image.resize((50, 50), Image.Resampling.LANCZOS)
btn7_image = ImageTk.PhotoImage(btn7_image)


# Button
# Monito Button
btn_font = font.Font(size=25)
btn1 = tk.Button(frame1, text='Monitor', height=90, width=180, fg='white', command=monitor, image=btn1_image, compound='left')
btn1['font'] = btn_font
# btn1["border"] = "0"
btn1["bg"] = "orange"
btn1.grid(row=3, pady=(20, 10))
# Record Button
btn4 = tk.Button(frame1, text='Record', height=90, width=180, fg='white', command=record, image=btn4_image, compound='left')
btn4['font'] = btn_font
btn4["bg"] = "orange"
btn4.grid(row=5, pady=(20, 10), column=3)
# Authorization
btn6 = tk.Button(frame1, text='Authorize', height=90, width=180, fg='white', command=maincall, image=btn6_image, compound='left')
btn6['font'] = btn_font
btn6["bg"] = "orange"
btn6.grid(row=5, pady=(20, 10))
# Exit
btn5 = tk.Button(frame1, height=90, width=180, fg='red', command=window.quit, image=btn5_image)
btn5['font'] = btn_font
btn5["bg"] = "orange"
btn5.grid(row=6, pady=(20, 10), column=2)
# Identify Button
btn7 = tk.Button(frame1, text="Identify", fg="white", command=identify, compound='left', image=btn7_image, height=90, width=180)
btn7['font'] = btn_font
btn7["bg"] = "orange"
btn7.grid(row=3, column=3, pady=(20, 10))

frame1.pack()
window.mainloop()
