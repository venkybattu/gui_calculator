import tkinter as tk
import math

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("360x520")
root.resizable(False, False)

# Display box
display = tk.Entry(root, font=("Arial", 24), bd=10, justify="right")
display.pack(fill="both", padx=10, pady=10)

# ---------------- Functions ---------------- #

def press(value):
    display.insert(tk.END, value)

def clear():
    display.delete(0, tk.END)

def backspace():
    text = display.get()
    display.delete(0, tk.END)
    display.insert(0, text[:-1])

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def square():
    try:
        value = float(display.get())
        display.delete(0, tk.END)
        display.insert(0, value ** 2)
    except:
        display.insert(0, "Error")

def squareroot():
    try:
        value = float(display.get())
        display.delete(0, tk.END)
        display.insert(0, math.sqrt(value))
    except:
        display.insert(0, "Error")

# ---------------- Buttons ---------------- #

frame = tk.Frame(root)
frame.pack()

buttons = [
    ("C", clear), ("⌫", backspace), ("%", lambda: press("%")), ("/", lambda: press("/")),
    ("7", lambda: press("7")), ("8", lambda: press("8")), ("9", lambda: press("9")), ("*", lambda: press("*")),
    ("4", lambda: press("4")), ("5", lambda: press("5")), ("6", lambda: press("6")), ("-", lambda: press("-")),
    ("1", lambda: press("1")), ("2", lambda: press("2")), ("3", lambda: press("3")), ("+", lambda: press("+")),
    ("0", lambda: press("0")), (".", lambda: press(".")), ("x²", square), ("=", calculate),
    ("√", squareroot), ("xʸ", lambda: press("**"))
]

row = 0
col = 0

for text, cmd in buttons:
    tk.Button(frame, text=text, width=8, height=3, font=("Arial", 12),
              command=cmd).grid(row=row, column=col, padx=3, pady=3)
    col += 1
    if col == 4:
        col = 0
        row += 1

# Run application
root.mainloop()
