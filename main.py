from tkinter import *
from tkinter import messagebox
import qrcode

windowBg = "#441014"
titleColor = "#F8F0C0"
fieldsBg = "#F8F8F0"
fieldsColor = "#400011"


def generateCode():
    qr = qrcode.QRCode(version=size_input.get(),
                       box_size=10,
                       border=5)
    qr.add_data(text_input.get())
    qr.make(fit=True)
    img = qr.make_image()
    file_directory = location_input.get() + "\\" + name_input.get()
    img.save(f'{file_directory}.png')
    messagebox.showinfo("Nice", "Saved!")


# create window
window = Tk(className="QR Generator")
window.geometry("600x600")
window.config(bg=windowBg)  # pale warm yellow
frame = LabelFrame(window,
                   text="Generate QR Code",
                   bg=windowBg,
                   fg=titleColor,
                   font=('Times', 40))
frame.pack(fill="both", expand='yes')
# text/url
text_label = Label(frame,
                   text="Enter the text/URL: ",
                   bg=windowBg,
                   fg=fieldsBg,
                   font=('Century 12'))
text_label.pack(anchor='nw', padx=10, pady=5)
text_input = Entry(frame,
                   bg=fieldsBg,
                   fg=fieldsColor)
text_input.pack(anchor='nw', fill="x", padx=10)
# location
location_label = Label(frame,
                       text="Enter the location to save the QR Code: ",
                       bg=windowBg,
                       fg=fieldsBg,
                       font=('Century 12'))
location_label.pack(anchor='nw', padx=10, pady=5)
location_input = Entry(frame,
                       bg=fieldsBg,
                       fg=fieldsColor,)
location_input.pack(anchor='nw', fill="x", padx=10)
# image name
name_label = Label(frame,
                   text="Enter the file name: ",
                   bg=windowBg,
                   fg=fieldsBg,
                   font=('Century 12'))
name_label.pack(anchor='nw', padx=10, pady=5)
name_input = Entry(frame,
                   bg=fieldsBg,
                   fg=fieldsColor)
name_input.pack(anchor='nw', fill="x", padx=10)
# size
size_label = Label(frame,
                   text="Enter the size from 1 to 40 with 1 being 21x21:",
                   bg=windowBg,
                   fg=fieldsBg,
                   font=('Century 12'))
size_label.pack(anchor='nw', padx=10, pady=5)
size_input = Entry(frame,
                   bg=fieldsBg,
                   fg=fieldsColor)
size_input.pack(anchor='nw', fill="x", padx=10)
# submit button
button = Button(window,
                text="Give me QR",
                command=generateCode
                )
button.pack()

window.mainloop()
