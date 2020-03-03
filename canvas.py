import tkinter as tk


window = tk.Tk()
window.title("Template Folder")
frame_a = tk.Frame(width=400, height=190)

label_a = tk.Label(master=frame_a, text="Save as path: ")
label_a.pack()

entry = tk.Entry(frame_a, text="Please fill the path")
entry.place(x=100, y=25)

frame_a.pack()

window.mainloop()
