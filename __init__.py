#!/usr/bin/python3.7

"""
OVERVIEW:
    This app intended to be run in Windows 10. This app function to generate
    folder structure and sub-folder.
"""
import tkinter as tk
import pathlib
import test

# Title of the interface
window = tk.Tk()
window.title("Template Folder Structure")
frm_a = tk.Frame(master=window, width=400, height=150)

frm_a.pack()

# Set layout post
lbl_path = tk.Label(master=frm_a, text="Save as path: ")
lbl_path.pack()
lbl_path.place(x=10, y=25)

# Set entry for input
ent_path = tk.Entry(master=frm_a, width=40, borderwidth=1)
root_path = pathlib.Path(ent_path)

ent_path.pack()
ent_path.place(x=80, y=25)

# create button to interact the function
btn_generate = tk.Button(master=frm_a, text="Generate Folder")
btn_generate.place(x=80, y=50)

# function run when click
btn_generate.bind("<Button-1>", test.create_folders)

# Keep the app running
window.mainloop()
