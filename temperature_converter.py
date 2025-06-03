import tkinter as tk
from tkinter import ttk, messagebox

def convert_temperature():
    try:
        temp = float(entry_temp.get())
        unit = combo_from.get()
        to_unit = combo_to.get()

        if unit == to_unit:
            result.set(f"{temp:.2f} °{to_unit[0]}")
            return

        # Convert input to Celsius first
        if unit == "Fahrenheit":
            celsius = (temp - 32) * 5/9
        elif unit == "Kelvin":
            celsius = temp - 273.15
        else:
            celsius = temp

        # Convert from Celsius to target unit
        if to_unit == "Fahrenheit":
            converted = (celsius * 9/5) + 32
        elif to_unit == "Kelvin":
            converted = celsius + 273.15
        else:
            converted = celsius

        result.set(f"{converted:.2f} °{to_unit[0]}")

    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number.")

# GUI Setup
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x250")
root.resizable(False, False)

# Input field
tk.Label(root, text="Enter Temperature:").pack(pady=5)
entry_temp = tk.Entry(root, width=20, font=("Arial", 14))
entry_temp.pack()

# From and To dropdowns
tk.Label(root, text="From:").pack(pady=5)
combo_from = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"])
combo_from.current(0)
combo_from.pack()

tk.Label(root, text="To:").pack(pady=5)
combo_to = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"])
combo_to.current(1)
combo_to.pack()

# Convert button
tk.Button(root, text="Convert", command=convert_temperature).pack(pady=10)

# Result display
result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 14), fg="blue").pack()

root.mainloop()
