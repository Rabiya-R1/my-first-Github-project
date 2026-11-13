import tkinter as tk
from tkinter import messagebox
import math

def get_values():
    try:
        v = float(voltage.get())
        i = float(current.get())
        pf = float(power_factor.get())

        if v <= 0 or i <= 0 or not 0 <= pf <= 1:
            raise ValueError

        return v, i, pf

    except ValueError:
        messagebox.showerror(
            "Input Error",
            "Enter positive voltage/current and PF between 0 and 1."
        )
        return None

def single_phase():
    values = get_values()
    if values:
        v, i, pf = values
        apparent = v * i
        active = apparent * pf

        result.config(
            text=f"Apparent Power: {apparent:.2f} VA\n"
                 f"Active Power: {active:.2f} W"
        )

def three_phase():
    values = get_values()
    if values:
        v, i, pf = values
        apparent = math.sqrt(3) * v * i
        active = apparent * pf

        result.config(
            text=f"Apparent Power: {apparent:.2f} VA\n"
                 f"Active Power: {active:.2f} W"
        )

def energy():
    try:
        p = float(power.get())
        h = float(hours.get())
        d = float(days.get())

        if p <= 0 or h < 0 or d <= 0:
            raise ValueError

        units = p * h * d / 1000
        result.config(text=f"Energy Consumption: {units:.2f} kWh")

    except ValueError:
        messagebox.showerror("Input Error", "Enter valid positive values.")

def bill():
    try:
        units = float(consumption.get())
        rate = float(cost.get())

        if units < 0 or rate < 0:
            raise ValueError

        total = units * rate
        result.config(text=f"Estimated Bill: Rs. {total:.2f}")

    except ValueError:
        messagebox.showerror("Input Error", "Enter valid non-negative values.")

root = tk.Tk()
root.title("Electrical Engineering Toolkit")
root.geometry("520x650")
root.configure(bg="#edf2f7")

tk.Label(
    root,
    text="ELECTRICAL ENGINEERING TOOLKIT",
    font=("Arial", 16, "bold"),
    bg="#edf2f7",
    fg="#17365D"
).pack(pady=15)

frame = tk.Frame(root, bg="#edf2f7")
frame.pack(pady=5)

def add_field(label, variable, row):
    tk.Label(frame, text=label, bg="#edf2f7",
             font=("Arial", 10)).grid(row=row, column=0, sticky="w", pady=5)
    tk.Entry(frame, textvariable=variable,
             width=22).grid(row=row, column=1, pady=5)

voltage = tk.StringVar(value="415")
current = tk.StringVar(value="10")
power_factor = tk.StringVar(value="0.8")
power = tk.StringVar(value="1000")
hours = tk.StringVar(value="5")
days = tk.StringVar(value="30")
consumption = tk.StringVar(value="150")
cost = tk.StringVar(value="6")

add_field("Voltage (V)", voltage, 0)
add_field("Current (A)", current, 1)
add_field("Power Factor", power_factor, 2)
add_field("Appliance Power (W)", power, 3)
add_field("Hours per day", hours, 4)
add_field("Number of days", days, 5)
add_field("Energy units (kWh)", consumption, 6)
add_field("Rate per unit (Rs)", cost, 7)

buttons = tk.Frame(root, bg="#edf2f7")
buttons.pack(pady=15)

tk.Button(buttons, text="Single Phase Power",
          command=single_phase, width=22).pack(pady=4)

tk.Button(buttons, text="Three Phase Power",
          command=three_phase, width=22).pack(pady=4)

tk.Button(buttons, text="Energy Consumption",
          command=energy, width=22).pack(pady=4)

tk.Button(buttons, text="Electricity Bill",
          command=bill, width=22).pack(pady=4)

result = tk.Label(
    root,
    text="Your calculation will appear here",
    font=("Arial", 12, "bold"),
    bg="white",
    fg="#17365D",
    width=42,
    height=4,
    wraplength=400
)
result.pack(pady=15)

root.mainloop()
