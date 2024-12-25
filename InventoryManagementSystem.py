import tkinter as tk
from tkinter import messagebox
import json

# File to store inventory data
data_file = "inventory_data.json"

# Function to load data from file
def load_data():
    try:
        with open(data_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

# Function to save data to file
def save_data(data):
    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)

# Function to validate numeric input
def validate_numeric(value):
    try:
        return float(value)
    except ValueError:
        return None

# User authentication
def authenticate(username, password):
    # Replace with real authentication logic
    valid_users = {"admin": "password123", "user": "userpass"}
    return valid_users.get(username) == password

# Add product
def add_product(data, name, quantity, price):
    if name in data:
        messagebox.showerror("Error", "Product already exists.")
        return
    data[name] = {"quantity": quantity, "price": price}
    save_data(data)
    messagebox.showinfo("Success", "Product added successfully.")

# Edit product
def edit_product(data, name, quantity, price):
    if name not in data:
        messagebox.showerror("Error", "Product does not exist.")
        return
    data[name] = {"quantity": quantity, "price": price}
    save_data(data)
    messagebox.showinfo("Success", "Product updated successfully.")

# Delete product
def delete_product(data, name):
    if name not in data:
        messagebox.showerror("Error", "Product does not exist.")
        return
    del data[name]
    save_data(data)
    messagebox.showinfo("Success", "Product deleted successfully.")

# Generate low-stock report
def generate_low_stock_report(data, threshold):
    low_stock = [name for name, info in data.items() if info["quantity"] < threshold]
    if not low_stock:
        messagebox.showinfo("Report", "No low-stock items.")
    else:
        report = "\n".join(low_stock)
        messagebox.showinfo("Low-Stock Report", f"Low-stock items:\n{report}")

# Create GUI
def create_gui():
    data = load_data()

    def handle_add():
        name = name_entry.get()
        quantity = validate_numeric(quantity_entry.get())
        price = validate_numeric(price_entry.get())
        if not name or quantity is None or price is None:
            messagebox.showerror("Error", "Invalid input.")
            return
        add_product(data, name, quantity, price)

    def handle_edit():
        name = name_entry.get()
        quantity = validate_numeric(quantity_entry.get())
        price = validate_numeric(price_entry.get())
        if not name or quantity is None or price is None:
            messagebox.showerror("Error", "Invalid input.")
            return
        edit_product(data, name, quantity, price)

    def handle_delete():
        name = name_entry.get()
        if not name:
            messagebox.showerror("Error", "Invalid input.")
            return
        delete_product(data, name)

    def handle_report():
        threshold = validate_numeric(threshold_entry.get())
        if threshold is None:
            messagebox.showerror("Error", "Invalid threshold.")
            return
        generate_low_stock_report(data, threshold)

    root = tk.Tk()
    root.title("Inventory Management System")

    tk.Label(root, text="Product Name:").grid(row=0, column=0)
    name_entry = tk.Entry(root)
    name_entry.grid(row=0, column=1)

    tk.Label(root, text="Quantity:").grid(row=1, column=0)
    quantity_entry = tk.Entry(root)
    quantity_entry.grid(row=1, column=1)

    tk.Label(root, text="Price:").grid(row=2, column=0)
    price_entry = tk.Entry(root)
    price_entry.grid(row=2, column=1)

    tk.Button(root, text="Add Product", command=handle_add).grid(row=3, column=0)
    tk.Button(root, text="Edit Product", command=handle_edit).grid(row=3, column=1)
    tk.Button(root, text="Delete Product", command=handle_delete).grid(row=4, column=0)

    tk.Label(root, text="Low-Stock Threshold:").grid(row=5, column=0)
    threshold_entry = tk.Entry(root)
    threshold_entry.grid(row=5, column=1)
    tk.Button(root, text="Generate Low-Stock Report", command=handle_report).grid(row=6, column=0, columnspan=2)

    root.mainloop()

# Run the application
if __name__ == "__main__":
    create_gui()

