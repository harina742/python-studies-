import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- DATABASE ----------------

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Harinaaakash@18",  
    database="sales_db"
)

cursor = conn.cursor()

# ---------------- FUNCTIONS ----------------

def add_record():

    product = product_entry.get()
    quantity = quantity_entry.get()
    price = price_entry.get()
    date = date_entry.get()

    if product == "" or quantity == "" or price == "" or date == "":
        messagebox.showwarning("Warning", "Please fill all fields")
        return

    cursor.execute(
        "INSERT INTO sales(product, quantity, price, date) VALUES (%s, %s, %s, %s)",
        (product, quantity, price, date)
    )

    conn.commit()

    messagebox.showinfo("Success", "Record Added Successfully")

    product_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)


def view_data():

    window = tk.Toplevel(root)
    window.title("Sales Records")
    window.geometry("700x400")

    tree = ttk.Treeview(window)
    tree["columns"] = ("ID", "Product", "Quantity", "Price", "Date")

    for col in tree["columns"]:
        tree.heading(col, text=col)
        tree.column(col, anchor="center")

    tree.pack(fill="both", expand=True)

    cursor.execute("SELECT * FROM sales")
    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", tk.END, values=row)


def analyze_sales():

    df = pd.read_sql("SELECT * FROM sales", conn)

    if df.empty:
        messagebox.showwarning("Warning", "No data available")
        return

    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    df["revenue"] = df["quantity"] * df["price"]

    total_sales = df["revenue"].sum()
    best_product = df.groupby("product")["revenue"].sum().idxmax()

    messagebox.showinfo(
        "Sales Analysis",
        f"Total Revenue: {total_sales}\nBest Selling Product: {best_product}"
    )


def show_chart():

    df = pd.read_sql("SELECT * FROM sales", conn)

    if df.empty:
        messagebox.showwarning("Warning", "No data available")
        return

    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    df["revenue"] = df["quantity"] * df["price"]

    chart = df.groupby("product")["revenue"].sum()

    plt.figure()
    chart.plot(kind="bar")

    plt.title("Sales Revenue by Product", fontsize=16)
    plt.xlabel("Product", fontsize=14)
    plt.ylabel("Revenue", fontsize=14)

    plt.tight_layout()
    plt.show()


# ---------------- GUI ----------------

root = tk.Tk()
root.title("Sales Data Analysis Tool")
root.geometry("700x600")
root.configure(bg="#1e1e2f")

title = tk.Label(
    root,
    text="SALES DATA ANALYSIS TOOL",
    font=("Arial", 24, "bold"),
    fg="yellow",
    bg="#1e1e2f"
)
title.pack(pady=20)

label_style = {"font": ("Arial", 16), "bg": "#1e1e2f", "fg": "white"}

tk.Label(root, text="Product Name", **label_style).pack()
product_entry = tk.Entry(root, font=("Arial", 16), width=25)
product_entry.pack(pady=5)

tk.Label(root, text="Quantity", **label_style).pack()
quantity_entry = tk.Entry(root, font=("Arial", 16), width=25)
quantity_entry.pack(pady=5)

tk.Label(root, text="Price", **label_style).pack()
price_entry = tk.Entry(root, font=("Arial", 16), width=25)
price_entry.pack(pady=5)

tk.Label(root, text="Date (YYYY-MM-DD)", **label_style).pack()
date_entry = tk.Entry(root, font=("Arial", 16), width=25)
date_entry.pack(pady=5)

# Buttons

btn_style = {
    "font": ("Arial", 16, "bold"),
    "width": 20,
    "height": 2
}

tk.Button(root, text="Add Record", bg="#4CAF50", fg="white",
          command=add_record, **btn_style).pack(pady=10)

tk.Button(root, text="View Records", bg="#2196F3", fg="white",
          command=view_data, **btn_style).pack(pady=10)

tk.Button(root, text="Analyze Sales", bg="#FF9800", fg="white",
          command=analyze_sales, **btn_style).pack(pady=10)

tk.Button(root, text="Show Chart", bg="#9C27B0", fg="white",
          command=show_chart, **btn_style).pack(pady=10)

root.mainloop()
