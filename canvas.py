#!/usr/bin/python3.7

"""
OVERVIEW:
    This app intended to be run in Windows 10. This app function to generate
    folder structure and sub-folder.
"""
import tkinter as tk

# Title of the interface
window = tk.Tk()
window.title("Template Folder Structure")
frm_a = tk.Frame(width=400, height=150)
frm_b = tk.Frame(width=400, height=25, bg="grey")

frm_a.pack()
frm_b.pack(fill=tk.X)

# Set layout post
lbl_path = tk.Label(master=frm_a, text="Save as path: ")
lbl_path.pack()
lbl_path.place(x=10, y=25)

# Set entry for input
ent_path = tk.Entry(master=frm_a, width=40, borderwidth=1)
ent_path.pack()
ent_path.place(x=80, y=25)
# Insert sample path:
ent_path.insert(0, "../folderName/filesRevit")

btn_generate = tk.Button(master=frm_a, text="Generate Folder")
btn_generate.place(x=80, y=50)
window.mainloop()

# Version and Credit.
"""
Fix bugs of the text version and credit
"""
lbl_desc = tk.Label(
    master=frm_b,
    text="Beta Version 03/20\t Develops by:Lokman",
    fg="blue",
    bg="grey"
)
lbl_desc.pack()

# Keep the app running
window.mainloop()
