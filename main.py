import tkinter as tk
from tkinter import messagebox

class Restaurantapp:# Class
    def __init__(self, root):
        self.root = root
        root.title("Restaurant App")
        # menu
        self.menu = {
            "Non-Veg Options": None, 
            "cheese burger": 2.99,
            "Steak": 5.99,
            "Fries": 2.50,
            "Pizza": 7.99,
            "Veg Options": None,
            "Veg Pizza": 7.99,
            "Veg Burger": 3.99,
            "Sodas": 0.00,
            "Pepsi": 0.99,
            "Coke": 0.99,
            }
        
        tk.Label(root, text="Restaurant Menu", font= ("Times New Roman", 18)).pack(pady= 10)
        self.entries = {}
        for item, price in self.menu.items():
            frame = tk.Frame(root)
            frame.pack()
            tk.Label(frame, text=f"{item} (${price})", width=15).pack(side="left")

            entry = tk.Entry(frame, width=5)
            entry.pack(side="left")
        tk.Button(root, text="Place Order", command=self.place_order).pack(pady=20)

    def place_order(self):
            total = 0
            summary = "Order Summary: \n"
            for item, entry in self.entries.items():
                
                 qty = entry.get()
                 if qty.isdigit():
                      qty = int(qty)
                      cost = qty*self.menu[item]

                      total +=cost 
                      if qty > 0:
                           summary +=f"{item}: {qty} x ${self.menu[item]} = ${cost}\n"

            if total > 0:
                 summary +=f"\nTotal : ${total}"
                 messagebox.showinfo("Order Placed", summary)    
            else:
                messagebox.showwarning("Order Not Placed")

# Running codes
root = tk.Tk()
app = Restaurantapp(root)
root.mainloop()