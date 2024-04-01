import tkinter as tk

def toggle_label():
    if label.winfo_ismapped():
        label.grid_forget()
        button.config(text="Show Label")
    else:
        label.grid(row=1, column=0)
        button.config(text="Hide Label")

root = tk.Tk()

label = tk.Label(root, text="This is a label")
label.grid(row=1, column=0)

button = tk.Button(root, text="Hide Label", command=toggle_label)
button.grid(row=0, column=0)

root.mainloop()