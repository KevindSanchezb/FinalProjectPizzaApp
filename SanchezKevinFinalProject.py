
# SanchezKevinFinalProject.py
# Pizza Ordering Application - Final Project
# Author: Kevin Sanchez
# Description: A modular Python Tkinter-based GUI application to simulate a pizza ordering system.
# It allows users to customize their pizza, view order summary, and validate input securely.

import tkinter as tk
from tkinter import messagebox, Toplevel, Label, PhotoImage

# Globals
pizza_size = tk.StringVar()
crust_type = tk.StringVar()
topping_vars = {}

def create_main_window():
    """Create and display the main ordering window"""
    root = tk.Tk()
    root.title("Pizza Ordering System")
    root.geometry("400x600")

    Label(root, text="Choose Pizza Size:").pack()
    for size in ["Small", "Medium", "Large"]:
        tk.Radiobutton(root, text=size, variable=pizza_size, value=size).pack()

    Label(root, text="Choose Crust Type:").pack()
    for crust in ["Thin", "Thick", "Cheese Stuffed"]:
        tk.Radiobutton(root, text=crust, variable=crust_type, value=crust).pack()

    Label(root, text="Select Toppings:").pack()
    for topping in ["Pepperoni", "Mushrooms", "Green Peppers", "Onions", "Bacon"]:
        topping_vars[topping] = tk.IntVar()
        tk.Checkbutton(root, text=topping, variable=topping_vars[topping]).pack()

    tk.Button(root, text="Place Order", command=place_order).pack(pady=5)
    tk.Button(root, text="Clear", command=clear_order).pack(pady=5)
    tk.Button(root, text="About", command=create_about_window).pack(pady=5)
    tk.Button(root, text="Exit", command=root.quit).pack(pady=5)

    root.mainloop()

def place_order():
    """Validate input and show order summary"""
    size = pizza_size.get()
    crust = crust_type.get()
    toppings = [t for t, var in topping_vars.items() if var.get() == 1]

    if not size or not crust:
        messagebox.showerror("Input Error", "Please select both pizza size and crust type.")
        return

    summary = f"Order Summary:\nSize: {size}\nCrust: {crust}\nToppings: {', '.join(toppings) if toppings else 'None'}"
    messagebox.showinfo("Order Placed", summary)

def clear_order():
    """Reset all selections"""
    pizza_size.set("")
    crust_type.set("")
    for var in topping_vars.values():
        var.set(0)

def create_about_window():
    """Open a secondary window with app info and images"""
    about_win = Toplevel()
    about_win.title("About This App")
    about_win.geometry("300x300")

    Label(about_win, text="Pizza Ordering System\nVersion 1.0\nBy Kevin Sanchez", justify="center").pack(pady=10)

    try:
        pizza_img = PhotoImage(file="pizza_image.png")  # Placeholder for actual image
        img_label = Label(about_win, image=pizza_img)
        img_label.image = pizza_img  # Keep reference
        img_label.pack()
        Label(about_win, text="Image: Freshly baked pizza").pack()
    except Exception as e:
        Label(about_win, text="(Image could not be loaded)").pack()

# Start the application
if __name__ == "__main__":
    create_main_window()
