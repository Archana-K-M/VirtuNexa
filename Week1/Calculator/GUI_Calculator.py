import tkinter as tk
from tkinter import messagebox
import sqlite3

# Database setup
def create_database():
    conn = sqlite3.connect("calculator_history_gui.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            operation TEXT,
            result REAL
        )
    """)
    conn.commit()
    conn.close()

def save_to_history(operation, result):
    conn = sqlite3.connect("calculator_history_gui.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO history (operation, result) VALUES (?, ?)", (operation, result))
    conn.commit()
    conn.close()

def view_history():
    conn = sqlite3.connect("calculator_history_gui.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM history ORDER BY id DESC LIMIT 10")
    rows = cursor.fetchall()
    conn.close()

    history_text = "\n".join([f"{row[1]} = {row[2]}" for row in rows])
    if not history_text:
        history_text = "No history available."

    messagebox.showinfo("History", history_text)

# Calculator logic
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)  # Evaluates the expression
        result_label.config(text=f"Result: {result}")

        save_to_history(expression, result)
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero!")
    except Exception:
        messagebox.showerror("Error", "Invalid input! Please enter a valid mathematical expression.")

# GUI Setup
root = tk.Tk()
root.title("GUI Calculator")
root.geometry("300x300")

tk.Label(root, text="Enter Expression:").pack(pady=5)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

tk.Button(root, text="Calculate", command=calculate).pack(pady=5)
result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=5)

tk.Button(root, text="View History", command=view_history).pack(pady=5)
tk.Button(root, text="Exit", command=root.quit).pack(pady=5)

create_database()
root.mainloop()
