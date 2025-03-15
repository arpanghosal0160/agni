import tkinter as tk
from tkinter import ttk

def apply_styles(root):
    style = ttk.Style(root)
    
    # Set the theme
    style.theme_use('clam')

    # Configure styles for various widgets
    style.configure('TLabel', font=('Helvetica', 12), background='#f0f0f0', foreground='#333')
    style.configure('TButton', font=('Helvetica', 12), background='#4CAF50', foreground='white', padding=10)
    style.configure('TEntry', font=('Helvetica', 12), padding=5)
    style.configure('TText', font=('Helvetica', 12), padding=5, background='#fff', foreground='#333')

    # Configure specific styles for buttons
    style.map('TButton', background=[('active', '#45a049')])

    # Set the background color for the root window
    root.configure(background='#f0f0f0')