import tkinter as tk
from tkinter import messagebox
import csv
import os
from tkinter import scrolledtext

# Prices for items
prices = {
    "Uttapa": 50,
    "Dosa": 40,
    "Idli": 30,
    "Wada": 20,
  "paper dosa": 50,
  
  
}

# File to store transactions
transaction_file = "transactions.csv"

def calculate_bill():
    total = 0
    items_purchased = []

    for item, price in prices.items():
        quantity = quantity_vars[item].get()
        if quantity > 0:
            total += price * quantity
            items_purchased.append(f"{item}: {quantity} x ₹{price} = ₹{quantity * price}")

    if total > 0:
        invoice = "\n".join(items_purchased) + f"\n\nTotal Amount: ₹{total}"
        display_invoice(invoice)
        save_transaction(items_purchased, total)
    else:
        messagebox.showerror("Error", "No items selected.")

def save_transaction(items, total):
    with open(transaction_file, mode="a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([", ".join(items), total])

def reset():
    for var in quantity_vars.values():
        var.set(0)

def view_transactions():
    if os.path.exists(transaction_file):
        with open(transaction_file, mode="r") as file:
            reader = csv.reader(file)
            transactions = "\n".join([f"Items: {row[0]}, Total: ₹{row[1]}" for row in reader])
            messagebox.showinfo("Transactions", transactions)
    else:
        messagebox.showinfo("Transactions", "No transactions recorded yet.")

def display_invoice(invoice):
    global invoice_window
    invoice_window = tk.Toplevel(window)
    invoice_window.title("Invoice")
    invoice_window.geometry("400x300")
    invoice_window.configure(bg="#f5f5f5")

    tk.Label(invoice_window, text="Invoice", font=("Arial", 18, "bold"), bg="#4CAF50", fg="white", padx=10, pady=5).pack(fill="x")
    invoice_text = scrolledtext.ScrolledText(invoice_window, wrap=tk.WORD, height=10, width=50, font=("Arial", 12), bg="#ffffff")
    invoice_text.insert(tk.END, invoice)
    invoice_text.pack(padx=10, pady=10)

    print_button = tk.Button(invoice_window, text="Print Bill", command=print_bill, font=("Arial", 12), bg="#4CAF50", fg="white", padx=10, pady=5)
    print_button.pack(side=tk.LEFT, padx=10, pady=10)

    close_button = tk.Button(invoice_window, text="Close", command=invoice_window.destroy, font=("Arial", 12), bg="#FF5722", fg="white", padx=10, pady=5)
    close_button.pack(side=tk.RIGHT, padx=10, pady=10)

def print_bill():
    invoice_text = invoice_window.children['!scrolledtext'].get("1.0", tk.END)
    print_invoice_text(invoice_text)

def print_invoice_text(text):
    # This function could send text to a printer. For simplicity, we just print it to the console.
    # In a real application, integrate with a printing library or system print command.
    print("Printing Invoice:")
    print(text)

# Set up the main window with styling
window = tk.Tk()
window.title("Snacks Billing System")
window.configure(bg="#f5f5f5")

# Header Label
tk.Label(window, text="Indian Snacks Billing", font=("Arial", 18, "bold"), bg="#4CAF50", fg="white", padx=20, pady=10).grid(row=0, column=0, columnspan=2, pady=10)

# Item selection with colors and padding
quantity_vars = {}
row = 1
for item, price in prices.items():
    tk.Label(window, text=f"{item} (₹{price}):", font=("Arial", 12), bg="#f5f5f5", fg="#333").grid(row=row, column=0, sticky="w", padx=10, pady=5)
    quantity_vars[item] = tk.IntVar(value=0)
    tk.Entry(window, textvariable=quantity_vars[item], width=5, font=("Arial", 12)).grid(row=row, column=1, padx=10, pady=5)
    row += 1

# Buttons with colors and padding
button_style = {"font": ("Arial", 12), "bg": "#2196F3", "fg": "white", "padx": 10, "pady": 5}
tk.Button(window, text="Calculate Bill", command=calculate_bill, **button_style).grid(row=row, column=0, pady=10, padx=10, sticky="e")
tk.Button(window, text="Reset", command=reset, **button_style).grid(row=row, column=1, pady=10, padx=10, sticky="w")

# View Transactions Button with different color
tk.Button(window, text="View Transactions", command=view_transactions, font=("Arial", 12), bg="#FF5722", fg="white", padx=10, pady=5).grid(row=row+1, column=0, columnspan=2, pady=10)

# Run the application
window.mainloop()
