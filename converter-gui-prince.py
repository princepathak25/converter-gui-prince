# 🔄 Prince's Beautiful Unit Converter GUI App
# Convert between Temperature, Length, and Weight — all in one elegant interface 💙
# Requirements: tkinter, ttk (comes with Python standard library)
from tkinter import *
from tkinter import ttk

# 📂 Conversion data
conversion_data = {
    'Length': {
        'Meter': 1.0,
        'Kilometer': 0.001,
        'Centimeter': 100.0,
        'Millimeter': 1000.0,
        'Mile': 0.000621371,
        'Yard': 1.09361,
        'Foot': 3.28084,
        'Inch': 39.3701
    },
    'Weight': {
        'Kilogram': 1.0,
        'Gram': 1000.0,
        'Milligram': 1000000.0,
        'Pound': 2.20462,
        'Ounce': 35.274
    },
    'Temperature': {
        'Celsius': 1.0,
        'Fahrenheit': 1.0,
        'Kelvin': 1.0
    }
}

# 🔀 Conversion logic
def convert():
    try:
        value = float(entry_value.get())
        category = category_cb.get()
        from_unit = from_cb.get()
        to_unit = to_cb.get()

        if category == 'Temperature':
            result = convert_temperature(value, from_unit, to_unit)
        else:
            if from_unit in conversion_data[category] and to_unit in conversion_data[category]:
                base = value / conversion_data[category][from_unit]
                result = base * conversion_data[category][to_unit]
            else:
                result_var.set("⚠️ Invalid unit selected.")
                return

        result_var.set(f"✅ Result: {result:.4f} {to_unit}")
    except ValueError:
        result_var.set("❌ Please enter a valid number.")

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == 'Celsius':
        return value * 9/5 + 32 if to_unit == 'Fahrenheit' else value + 273.15
    elif from_unit == 'Fahrenheit':
        return (value - 32) * 5/9 if to_unit == 'Celsius' else (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin':
        return value - 273.15 if to_unit == 'Celsius' else (value - 273.15) * 9/5 + 32

# 🖼️ GUI setup
root = Tk()
root.title("Prince's Beautiful Converter 🌟")
root.geometry("500x500")
root.config(bg="#111111")

style = ttk.Style()
style.theme_use("clam")
style.configure("TCombobox",
                fieldbackground="#2a2a2a",
                background="#2a2a2a",
                foreground="white",
                font=("Segoe UI", 12))

# 🔠 Input
Label(root, text="🔢 Enter value:", fg="white", bg="#111111", font=("Segoe UI", 12)).pack(pady=(20, 0))
entry_value = Entry(root, font=("Segoe UI", 18), bg="#2a2a2a", fg="white", insertbackground="white", relief=FLAT)
entry_value.pack(ipady=8, ipadx=5, padx=20, fill=X)

# 📂 Category
Label(root, text="📂 Choose category:", fg="white", bg="#111111", font=("Segoe UI", 12)).pack(pady=(20, 0))
category_cb = ttk.Combobox(root, values=list(conversion_data.keys()), state="readonly")
category_cb.current(0)
category_cb.pack(padx=20, pady=5, fill=X)

# 📤 From
Label(root, text="📤 From unit:", fg="white", bg="#111111", font=("Segoe UI", 12)).pack(pady=(15, 0))
from_cb = ttk.Combobox(root, state="readonly")
from_cb.pack(padx=20, pady=5, fill=X)

# ⬅️➡️ To
Label(root, text="📥 To unit:", fg="white", bg="#111111", font=("Segoe UI", 12)).pack(pady=(15, 0))
to_cb = ttk.Combobox(root, state="readonly")
to_cb.pack(padx=20, pady=5, fill=X)

# 🔄 Update units

def update_units(event):
    units = list(conversion_data[category_cb.get()].keys())
    from_cb['values'] = units
    to_cb['values'] = units
    from_cb.current(0)
    to_cb.current(1 if len(units) > 1 else 0)

category_cb.bind("<<ComboboxSelected>>", update_units)
update_units(None)

# 🚀 Convert
convert_btn = Button(root,
                     text="🧐 Convert Now",
                     font=("Segoe UI", 14, "bold"),
                     bg="#00cc44",
                     fg="white",
                     activebackground="#00e65c",
                     bd=0,
                     padx=10,
                     pady=10,
                     command=convert)
convert_btn.pack(pady=25, ipadx=10)

# ✅ Result
result_var = StringVar()
result_label = Label(root, textvariable=result_var, fg="#00ffff", bg="#111111", font=("Segoe UI", 13, "bold"))
result_label.pack()

root.mainloop()

# End of the converter GUI app
# Enjoy converting with style! 🎉