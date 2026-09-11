import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from datetime import datetime


# ==========================================================
# Main Window
# ==========================================================

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("470x650+300+150")
root.resizable(False, False)
root.configure(bg="#e9f5f4")


# ==========================================================
# Variables
# ==========================================================

height = tk.StringVar(value="170")
weight = tk.StringVar(value="65")
age = tk.StringVar(value="25")
gender = tk.StringVar(value="Male")
unit = tk.StringVar(value="Metric")

bmi_result = tk.StringVar(value="--")
status_result = tk.StringVar(value="Enter your details")
advice_result = tk.StringVar(value="")

history = []


# ==========================================================
# BMI Calculation
# ==========================================================

def calculate_bmi():
    try:
        h = float(height.get())
        w = float(weight.get())
        a = int(age.get())

        if h <= 0 or w <= 0 or a <= 0:
            raise ValueError

        # Metric calculation
        if unit.get() == "Metric":
            meters = h / 100
            bmi_value = w / (meters ** 2)

        # Imperial calculation
        else:
            bmi_value = (w / (h ** 2)) * 703

        bmi_value = round(bmi_value, 1)

        bmi_result.set(str(bmi_value))

        # BMI category
        if bmi_value < 18.5:
            category = "Underweight"
            color = "#3498db"
            advice = "Consider a balanced diet and healthy weight gain."
        elif bmi_value < 25:
            category = "Normal Weight"
            color = "#27ae60"
            advice = "Great! Maintain your healthy lifestyle."
        elif bmi_value < 30:
            category = "Overweight"
            color = "#f39c12"
            advice = "Regular exercise and a balanced diet may help."
        else:
            category = "Obesity"
            color = "#e74c3c"
            advice = "Consider discussing your health with a professional."

        status_result.set(category)
        status_label.config(fg=color)

        advice_result.set(advice)

        # Save calculation to history
        now = datetime.now().strftime("%H:%M:%S")

        history.append({
            "time": now,
            "age": a,
            "gender": gender.get(),
            "height": h,
            "weight": w,
            "bmi": bmi_value,
            "category": category
        })

        update_history()

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter valid positive numbers."
        )


# ==========================================================
# Reset
# ==========================================================

def reset():
    height.set("170")
    weight.set("65")
    age.set("25")
    gender.set("Male")
    unit.set("Metric")

    bmi_result.set("--")
    status_result.set("Enter your details")
    advice_result.set("")

    status_label.config(fg="black")


# ==========================================================
# History
# ==========================================================

def update_history():
    history_box.delete(0, tk.END)

    for item in history[-5:]:
        text = (
            f"{item['time']} | "
            f"BMI {item['bmi']} | "
            f"{item['category']}"
        )

        history_box.insert(tk.END, text)


def clear_history():
    history.clear()
    history_box.delete(0, tk.END)


# ==========================================================
# Header
# ==========================================================

header = tk.Frame(
    root,
    bg="#1f6e68",
    height=75
)

header.pack(fill="x")

tk.Label(
    header,
    text="BMI CALCULATOR",
    font=("Arial", 25, "bold"),
    bg="#1f6e68",
    fg="white"
).pack(pady=18)


# ==========================================================
# Input Section
# ==========================================================

input_frame = tk.Frame(
    root,
    bg="#e9f5f4"
)

input_frame.pack(pady=15)


# Age

tk.Label(
    input_frame,
    text="Age",
    font=("Arial", 11, "bold"),
    bg="#e9f5f4"
).grid(row=0, column=0, padx=10, pady=5)

tk.Entry(
    input_frame,
    textvariable=age,
    width=10,
    font=("Arial", 13),
    justify="center"
).grid(row=0, column=1, padx=10)


# Gender

tk.Label(
    input_frame,
    text="Gender",
    font=("Arial", 11, "bold"),
    bg="#e9f5f4"
).grid(row=0, column=2, padx=10)

gender_box = ttk.Combobox(
    input_frame,
    textvariable=gender,
    values=["Male", "Female"],
    width=10,
    state="readonly"
)

gender_box.grid(row=0, column=3, padx=10)


# ==========================================================
# Unit Selection
# ==========================================================

tk.Label(
    root,
    text="Measurement Unit",
    font=("Arial", 11, "bold"),
    bg="#e9f5f4"
).pack()

unit_frame = tk.Frame(
    root,
    bg="#e9f5f4"
)

unit_frame.pack(pady=5)

tk.Radiobutton(
    unit_frame,
    text="Metric (cm / kg)",
    variable=unit,
    value="Metric",
    bg="#e9f5f4",
    command=reset
).pack(side="left", padx=10)

tk.Radiobutton(
    unit_frame,
    text="Imperial (in / lb)",
    variable=unit,
    value="Imperial",
    bg="#e9f5f4",
    command=reset
).pack(side="left", padx=10)


# ==========================================================
# Height
# ==========================================================

tk.Label(
    root,
    text="Height",
    font=("Arial", 13, "bold"),
    bg="#e9f5f4"
).pack(pady=(10, 2))

height_entry = tk.Entry(
    root,
    textvariable=height,
    width=10,
    font=("Arial", 20),
    justify="center"
)

height_entry.pack()

height_slider = ttk.Scale(
    root,
    from_=50,
    to=220,
    orient="horizontal",
    length=300,
    command=lambda value: height.set(f"{float(value):.0f}")
)

height_slider.set(170)
height_slider.pack(pady=5)


# ==========================================================
# Weight
# ==========================================================

tk.Label(
    root,
    text="Weight",
    font=("Arial", 13, "bold"),
    bg="#e9f5f4"
).pack(pady=(10, 2))

weight_entry = tk.Entry(
    root,
    textvariable=weight,
    width=10,
    font=("Arial", 20),
    justify="center"
)

weight_entry.pack()

weight_slider = ttk.Scale(
    root,
    from_=20,
    to=200,
    orient="horizontal",
    length=300,
    command=lambda value: weight.set(f"{float(value):.0f}")
)

weight_slider.set(65)
weight_slider.pack(pady=5)


# ==========================================================
# Buttons
# ==========================================================

button_frame = tk.Frame(
    root,
    bg="#e9f5f4"
)

button_frame.pack(pady=12)

tk.Button(
    button_frame,
    text="Calculate BMI",
    width=16,
    height=2,
    font=("Arial", 10, "bold"),
    bg="#1f6e68",
    fg="white",
    activebackground="#15534f",
    activeforeground="white",
    command=calculate_bmi
).pack(side="left", padx=5)

tk.Button(
    button_frame,
    text="Reset",
    width=10,
    height=2,
    font=("Arial", 10, "bold"),
    bg="#777777",
    fg="white",
    command=reset
).pack(side="left", padx=5)


# ==========================================================
# Result Section
# ==========================================================

result_frame = tk.Frame(
    root,
    bg="white",
    bd=2,
    relief="groove"
)

result_frame.pack(
    fill="x",
    padx=25,
    pady=5
)

tk.Label(
    result_frame,
    text="YOUR BMI",
    font=("Arial", 11, "bold"),
    bg="white"
).pack(pady=(8, 0))

tk.Label(
    result_frame,
    textvariable=bmi_result,
    font=("Arial", 35, "bold"),
    bg="white",
    fg="#1f6e68"
).pack()

status_label = tk.Label(
    result_frame,
    textvariable=status_result,
    font=("Arial", 16, "bold"),
    bg="white"
)

status_label.pack()

tk.Label(
    result_frame,
    textvariable=advice_result,
    font=("Arial", 9),
    bg="white",
    wraplength=380
).pack(pady=8)


# ==========================================================
# History
# ==========================================================

tk.Label(
    root,
    text="Recent Calculations",
    font=("Arial", 12, "bold"),
    bg="#e9f5f4"
).pack(pady=(8, 3))

history_box = tk.Listbox(
    root,
    width=52,
    height=4,
    font=("Arial", 9)
)

history_box.pack()

tk.Button(
    root,
    text="Clear History",
    command=clear_history,
    font=("Arial", 9),
    bg="#eeeeee"
).pack(pady=5)


# ==========================================================
# BMI Reference
# ==========================================================

tk.Label(
    root,
    text="BMI: <18.5 Underweight | 18.5–24.9 Normal | "
         "25–29.9 Overweight | 30+ Obesity",
    font=("Arial", 8),
    bg="#e9f5f4",
    fg="#555555"
).pack(pady=3)


# ==========================================================
# Start Application
# ==========================================================

root.mainloop()
