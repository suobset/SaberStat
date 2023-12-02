"""
UI for dsplaying StatInterface
"""

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class SaberStatUI:
    def __init_(self, master):
        self.master = master
        master.title("SaberStat ServerTracker v0.0.2")

        # Start Drawing Window
        self.name_label = ttk.Label(master, text="Enter Name:")
        self.name_label.grid(row=0, column=0, pady=10, padx=10, sticky=tk.W)
        self.name_enter = ttk.Entry(master, width=30)
        self.name_enter.grid(row=0, column=1, pady=10, padx=10, sticky=tk.W)

        