"""
UI for dsplaying StatInterface
"""

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class SaberStatUI:
    def __init__(self, root):
        self.root = root
        self.root.title("SaberStat Server UI")

        # Variables to track hits and misses
        self.hits = 0
        self.misses = 0
        self.round_number = 1

        # Name Entry
        self.name_label = ttk.Label(root, text="Enter Your Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.name_entry = ttk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Round Number
        self.round_label = ttk.Label(root, text="Round:")
        self.round_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.round_var = tk.StringVar()
        self.round_var.set(str(self.round_number))
        self.round_display = ttk.Label(root, textvariable=self.round_var)
        self.round_display.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # Hits and Misses
        self.hits_label = ttk.Label(root, text="Hits:")
        self.hits_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.hits_var = tk.StringVar()
        self.hits_var.set(str(self.hits))
        self.hits_display = ttk.Label(root, textvariable=self.hits_var, font=("Helvetica", 16, "bold"))
        self.hits_display.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.misses_label = ttk.Label(root, text="Misses:")
        self.misses_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.misses_var = tk.StringVar()
        self.misses_var.set(str(self.misses))
        self.misses_display = ttk.Label(root, textvariable=self.misses_var, font=("Helvetica", 16, "bold"))
        self.misses_display.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        # Button to simulate hits and misses
        self.hit_button = ttk.Button(root, text="Hit!", command=self.record_hit)
        self.hit_button.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        self.miss_button = ttk.Button(root, text="Miss!", command=self.record_miss)
        self.miss_button.grid(row=4, column=1, padx=10, pady=10, sticky="w")

    def record_hit(self):
        self.hits += 1
        self.update_stats()

    def record_miss(self):
        self.misses += 1
        self.update_stats()

    def update_stats(self):
        self.hits_var.set(str(self.hits))
        self.misses_var.set(str(self.misses))

        # You can implement logic to increment the round number when needed
        # For example, after a certain number of hits or misses

        # Update the round number display
        self.round_number += 1
        self.round_var.set(str(self.round_number))