#!/usr/bin/python3.7

"""
OVERVIEW:
    This app intended to be run in Windows 10. This app function to generate
    folder structure and sub-folder.
"""

import tkinter as tk
import pathlib
import main


# Create function
def create_folders(root_path):
    for folder in main.mainFolder:
        (root_path / folder).mkdir(parents=True, exist_ok=True)
       
def main():
    root = tk.get() 
    root_path = pathlib.Path(root)
    create_folders(root_path)

if __name__ == "__main__":
    main()

# Title of the interface
window = tk.Tk()
window.title("Template Folder Structure")
frame = tk.Frame(master=window)
# Set layout post
lbl_path = tk.Label(master=window, text="Save as path: ")
lbl_path.grid(row=0, column=0, padx=5, pady=5, sticky='w')

# Set entry for input
ent_path = tk.Entry(master=window, width=40, borderwidth=1)
ent_path.grid(row=0, column=1, padx=5, pady=5, sticky='e')

# create button to interact the function
btn_generate = tk.Button(
    master=window, text="Generate Folder", command=create_folders
)
btn_generate.grid(row=1, column=1, padx=5, pady=5, sticky='e')


# Keep the app running
window.mainloop()