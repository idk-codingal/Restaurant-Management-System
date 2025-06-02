import tkinter as tk
from tkinter import messagebox

class Restaurantapp:# Class
    def __init__(self, root):
        self.root = root
        root.title("Restaurant App")
        # menu
        self.menu = {
            "cheese burger": 2.99,
            "Steak": 5.99,
            "Fries": 2.50,
            "Pizza": 7.99,
            }
        
        tk.Label(root, text="Restaurant Menu", font= ("Times New Roman", 18)).pack(pady= 10)
        self.entries = {}
        for item, price in self.menu.items():
            frame = tk.Frame(root)
            frame.pack()