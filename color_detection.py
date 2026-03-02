# -------------------- IMPORT LIBRARIES --------------------
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from colorthief import ColorThief
import os

# -------------------- MAIN WINDOW --------------------
root = Tk()
root.title("Color Picker from Image")
root.geometry("800x470+100+100")
root.configure(bg="#bec3c7")
root.resizable(False, False)

# -------------------- GLOBAL VARIABLE --------------------
filename = ""   # Stores selected image path

# -------------------- FUNCTION: SHOW IMAGE --------------------
def showimage():
    global filename

    # Open file dialog to select image
    filename = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title="Select Image File",
        filetype=(("PNG File", "*.png"),
                  ("JPG File", "*.jpg"),
                  ("All Files", "*.*"))
    )

    if filename:
        # Open image
        img = Image.open(filename)

        # Resize image to fit frame (320x280)
        img = img.resize((320, 280), Image.LANCZOS)

        # Convert image for Tkinter
        img = ImageTk.PhotoImage(img)

        # Display image
        lbl.configure(image=img)
        lbl.image = img   # Prevent garbage collection

# -------------------- FUNCTION: FIND COLORS --------------------
def FindColor():
    if not filename:
        return

    # Extract colors from image
    ct = ColorThief(filename)
    palette = ct.get_palette(color_count=11)

    # Convert RGB to HEX
    hex_colors = []
    for i in range(10):
        r, g, b = palette[i]
        hex_colors.append(f"#{r:02x}{g:02x}{b:02x}")

    # Update first column
    colors.itemconfig(id1, fill=hex_colors[0])
    colors.itemconfig(id2, fill=hex_colors[1])
    colors.itemconfig(id3, fill=hex_colors[2])
    colors.itemconfig(id4, fill=hex_colors[3])
    colors.itemconfig(id5, fill=hex_colors[4])

    # Update second column
    colors2.itemconfig(id6, fill=hex_colors[5])
    colors2.itemconfig(id7, fill=hex_colors[6])
    colors2.itemconfig(id8, fill=hex_colors[7])
    colors2.itemconfig(id9, fill=hex_colors[8])
    colors2.itemconfig(id10, fill=hex_colors[9])

    # Update HEX labels
    hex1.config(text=hex_colors[0])
    hex2.config(text=hex_colors[1])
    hex3.config(text=hex_colors[2])
    hex4.config(text=hex_colors[3])
    hex5.config(text=hex_colors[4])
    hex6.config(text=hex_colors[5])
    hex7.config(text=hex_colors[6])
    hex8.config(text=hex_colors[7])
    hex9.config(text=hex_colors[8])
    hex10.config(text=hex_colors[9])

# -------------------- APP ICON --------------------
image_icon = PhotoImage(file="c:\\Users\\Affan laptop\\Downloads\\icon.png")
root.iconphoto(False, image_icon)

# -------------------- TOP HEADER --------------------
Label(root, width=120, height=10, bg="#4272f9").pack()

# -------------------- MAIN FRAME --------------------
frame = Frame(root, width=700, height=370, bg="#ffffff")
frame.place(x=50, y=50)

# -------------------- LOGO --------------------
logo_image = Image.open("c:\\Users\\Affan laptop\\Downloads\\palette.png")
logo_image = logo_image.resize((80, 80))
logo = ImageTk.PhotoImage(logo_image)

Label(frame, image=logo, bg="white").place(x=10, y=10)
Label(frame, text="Color Finder",
      font=("arial", 25, "bold"),
      bg="white").place(x=100, y=30)

# -------------------- FIRST COLOR COLUMN --------------------
colors = Canvas(frame, bg="white", width=150, height=265, bd=0)
colors.place(x=20, y=90)

id1 = colors.create_rectangle(10, 10, 50, 50, fill="#b8255f")
id2 = colors.create_rectangle(10, 50, 50, 100, fill="#db4035")
id3 = colors.create_rectangle(10, 100, 50, 150, fill="#ff9933")
id4 = colors.create_rectangle(10, 150, 50, 200, fill="#fad000")
id5 = colors.create_rectangle(10, 200, 50, 250, fill="#afb83b")

hex1 = Label(colors, text="#b8255f", font="arial 12 bold", bg="white")
hex1.place(x=60, y=10)
hex2 = Label(colors, text="#db4035", font="arial 12 bold", bg="white")
hex2.place(x=60, y=70)
hex3 = Label(colors, text="#ff9933", font="arial 12 bold", bg="white")
hex3.place(x=60, y=120)
hex4 = Label(colors, text="#fad000", font="arial 12 bold", bg="white")
hex4.place(x=60, y=170)
hex5 = Label(colors, text="#afb83b", font="arial 12 bold", bg="white")
hex5.place(x=60, y=220)

# -------------------- SECOND COLOR COLUMN --------------------
colors2 = Canvas(frame, bg="white", width=150, height=265, bd=0)
colors2.place(x=180, y=90)

id6 = colors2.create_rectangle(10, 10, 50, 50, fill="#7ecc49")
id7 = colors2.create_rectangle(10, 50, 50, 100, fill="#299438")
id8 = colors2.create_rectangle(10, 100, 50, 150, fill="#6accbc")
id9 = colors2.create_rectangle(10, 150, 50, 200, fill="#158fad")
id10 = colors2.create_rectangle(10, 200, 50, 250, fill="#14aaf5")

hex6 = Label(colors2, text="#7ecc49", font="arial 12 bold", bg="white")
hex6.place(x=60, y=10)
hex7 = Label(colors2, text="#299438", font="arial 12 bold", bg="white")
hex7.place(x=60, y=70)
hex8 = Label(colors2, text="#6accbc", font="arial 12 bold", bg="white")
hex8.place(x=60, y=120)
hex9 = Label(colors2, text="#158fad", font="arial 12 bold", bg="white")
hex9.place(x=60, y=170)
hex10 = Label(colors2, text="#14aaf5", font="arial 12 bold", bg="white")
hex10.place(x=60, y=220)

# -------------------- IMAGE DISPLAY AREA --------------------
image_frame = Frame(frame, width=340, height=350, bg="#d6dee5")
image_frame.place(x=350, y=10)

image_border = Frame(image_frame, bd=3, bg="black",
                     width=320, height=280, relief=GROOVE)
image_border.place(x=10, y=10)

lbl = Label(image_border, bg="black")
lbl.place(x=0, y=0)

# -------------------- BUTTONS --------------------
Button(image_frame, text="Select Image",
       font="arial 14 bold",
       command=showimage).place(x=10, y=300)

Button(image_frame, text="Find Colors",
       font="arial 14 bold",
       command=FindColor).place(x=176, y=300)

# -------------------- RUN APP --------------------
root.mainloop()

# 🎨 Color Picker from Image

# A simple Python GUI application built with Tkinter that allows users to select an image and automatically extract its dominant colors. The app displays the image and shows the top color palette along with their HEX color codes, making it useful for designers and developers.

# 🛠 Technologies Used

# Python

# Tkinter

# PIL (Pillow)

# ColorThief

# This project demonstrates GUI development, image processing, and color extraction in Python.