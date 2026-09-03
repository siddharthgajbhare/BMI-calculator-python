//aad cal new
import tkinter as tkinter
from tkinter import ttk
from PIL import Image, ImageTk


# Creating main window
root = tkinter.Tk()

# Setting title and geometry
root.title("BMI Calculator")
root.geometry("470x580+300+200")
root.resizable(False, False)

# Background color
root.config(bg="lightgrey")


# ---------------- BMI Calculation ----------------
def bmi():
    try:
        Height = float(h.get())
        Weight = float(w.get())

        if Height <= 0 or Weight <= 0:
            label.config(text="Invalid")
            label1.config(text="Please enter valid height and weight")
            return

        # Convert cm to meters
        m = Height / 100

        # Calculate BMI
        B = round(Weight / (m ** 2), 1)

        # Display BMI
        label.config(text=B)

        # BMI Conditions
        if B < 18.5:
            label1.config(text="Underweight")
        elif B < 25:
            label1.config(text="Normal")
        elif B < 30:
            label1.config(text="Overweight")
        else:
            label1.config(text="Health is at risk!\nNeed to lose weight")

    except ValueError:
        label.config(text="Error")
        label1.config(text="Please enter valid numbers")


# ---------------- Heading ----------------
top = tkinter.Label(
    root,
    text="BMI CALCULATOR",
    font=("Arial", 25, "bold"),
    width=25,
    bd=5,
    bg="white"
)
top.place(x=0, y=0)


# ---------------- Bottom Box ----------------
bottom = tkinter.Label(
    root,
    width=72,
    height=18,
    bg="lightcyan"
)
bottom.pack(side="bottom")


# ---------------- Images ----------------
try:
    box = tkinter.PhotoImage(file="bo.png")
    tkinter.Label(root, image=box).place(x=20, y=100)
    tkinter.Label(root, image=box).place(x=240, y=100)

    scale_img = tkinter.PhotoImage(file="scale.png")
    tkinter.Label(
        root,
        image=scale_img,
        bg="lightcyan"
    ).place(x=20, y=310)

except tkinter.TclError:
    print("Image files not found!")


# ---------------- Height Slider ----------------
current = tkinter.DoubleVar()


def slider_c(value):
    height.set("{:.0f}".format(current.get()))

    try:
        size = int(current.get())

        img = Image.open("man.png")

        # Resize image
        resized_img = img.resize((50, max(50, 10 + size)))

        p = ImageTk.PhotoImage(resized_img)

        man.config(image=p)
        man.image = p

        man.place(x=70, y=max(350, 550 - size))

    except FileNotFoundError:
        pass


style = ttk.Style()
style.configure("TScale", background="white")

slider_h = ttk.Scale(
    root,
    from_=50,
    to=220,
    orient="horizontal",
    style="TScale",
    command=slider_c,
    variable=current
)

slider_h.place(x=80, y=250)


# ---------------- Weight Slider ----------------
current2 = tkinter.DoubleVar()


def slider_c2(value):
    weight.set("{:.0f}".format(current2.get()))


slider_w = ttk.Scale(
    root,
    from_=20,
    to=200,
    orient="horizontal",
    style="TScale",
    command=slider_c2,
    variable=current2
)

slider_w.place(x=300, y=250)


# ---------------- Entry Variables ----------------
height = tkinter.StringVar()
weight = tkinter.StringVar()


# Height Entry
h = tkinter.Entry(
    root,
    textvariable=height,
    width=5,
    font=("Arial", 50),
    bg="white",
    fg="black",
    bd=0,
    justify="center"
)

h.place(x=35, y=160)


# Weight Entry
w = tkinter.Entry(
    root,
    textvariable=weight,
    width=5,
    font=("Arial", 50),
    bg="white",
    fg="black",
    bd=0,
    justify="center"
)

w.place(x=255, y=160)


# Default Values
current.set(170)
current2.set(65)

height.set("170")
weight.set("65")


# ---------------- Man Image ----------------
man = tkinter.Label(root, bg="lightcyan")
man.place(x=70, y=400)


# ---------------- Report Button ----------------
tkinter.Button(
    root,
    text="Report",
    width=15,
    height=2,
    font=("Arial", 10, "bold"),
    bg="#1f6e68",
    fg="white",
    command=bmi
).place(x=280, y=340)


# ---------------- BMI Result ----------------
label = tkinter.Label(
    root,
    font=("Arial", 30, "bold"),
    bg="lightcyan",
    fg="black"
)

label.place(x=350, y=450)


# BMI Status
label1 = tkinter.Label(
    root,
    font=("Arial", 10, "bold"),
    bg="lightcyan",
    fg="black",
    width=50
)

label1.place(x=200, y=500)


# Run application
root.mainloop()
