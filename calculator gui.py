import tkinter as tk
from tkinter import ttk, messagebox

# Function to perform calculation
def calculate():
    try:
        n1 = float(entry_num1.get())
        n2 = float(entry_num2.get())
        operation = combo_operation.get()

        if operation == "Addition (+)":
            result = n1 + n2
        elif operation == "Subtraction (-)":
            result = n1 - n2
        elif operation == "Multiplication (*)":
            result = n1 * n2
        elif operation == "Division (/)":
            if n2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
            result = n1 / n2
        elif operation == "Modulus (%)":
            result = n1 % n2
        elif operation == "Exponentiation (**)":
            result = n1 ** n2
        else:
            messagebox.showerror("Error", "Invalid operation.")
            return

        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Function for hover effect on button
def on_enter(e):
    e.widget['background'] = '#2f6aff'
    e.widget['foreground'] = 'white'

def on_leave(e):
    e.widget['background'] = '#4d88ff'
    e.widget['foreground'] = 'white'

# Create main window
root = tk.Tk()
root.title("Stylish Calculator")
root.geometry("380x350")
root.config(bg="#f0f4ff")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="Stylish Calculator", font=("Segoe UI", 18, "bold"), bg="#f0f4ff", fg="#1a1a1a")
title_label.pack(pady=15)

# Input Frame
frame_inputs = tk.Frame(root, bg="#f0f4ff")
frame_inputs.pack(pady=5)

tk.Label(frame_inputs, text="First Number:", font=("Segoe UI", 11), bg="#f0f4ff").grid(row=0, column=0, padx=5, pady=5)
entry_num1 = tk.Entry(frame_inputs, font=("Segoe UI", 11), width=15, bd=2, relief="solid")
entry_num1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Second Number:", font=("Segoe UI", 11), bg="#f0f4ff").grid(row=1, column=0, padx=5, pady=5)
entry_num2 = tk.Entry(frame_inputs, font=("Segoe UI", 11), width=15, bd=2, relief="solid")
entry_num2.grid(row=1, column=1, padx=5, pady=5)

# Operation Selector
tk.Label(root, text="Select Operation:", font=("Segoe UI", 11), bg="#f0f4ff").pack(pady=(10, 0))
combo_operation = ttk.Combobox(root, font=("Segoe UI", 11), values=[
    "Addition (+)",
    "Subtraction (-)",
    "Multiplication (*)",
    "Division (/)",
    "Modulus (%)",
    "Exponentiation (**)"
])
combo_operation.current(0)
combo_operation.pack(pady=5)

# Button Style
calc_button = tk.Button(root, text="Calculate", font=("Segoe UI", 12, "bold"),
                        bg="#4d88ff", fg="white", activebackground="#2f6aff",
                        activeforeground="white", width=15, height=1, bd=0,
                        relief="ridge", command=calculate)
calc_button.pack(pady=15)
calc_button.bind("<Enter>", on_enter)
calc_button.bind("<Leave>", on_leave)

# Result Label
label_result = tk.Label(root, text="Result: ", font=("Segoe UI", 14, "bold"), bg="#f0f4ff", fg="#1a1a1a")
label_result.pack(pady=10)

# Footer
footer = tk.Label(root, text="Made by Umer 💻", font=("Segoe UI", 9), bg="#f0f4ff", fg="#5a5a5a")
footer.pack(side="bottom", pady=5)

# Run the window
root.mainloop()
