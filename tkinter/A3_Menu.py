""" Nesting Menus is common. """

import tkinter as tk
from tkinter import ttk

# Create the main window
window = tk.Tk()
window.title("Menu")
window.geometry("1600x900")

# Menu Setup
menu = tk.Menu(window, tearoff=False)
window.config(menu=menu)

# Sub Menu for File...
file_menu = tk.Menu(menu, tearoff=False)
file_menu.add_command(label="New", command= lambda: print("New File"))
file_menu.add_separator()
file_menu.add_command(label="Open", command= lambda: print("Open File"))
file_check_string = tk.StringVar()
file_menu.add_checkbutton(label="Check", onvalue="on", offvalue="off", variable= file_check_string)

menu.add_cascade(label="File", menu=file_menu)



# Sub Menu for Edit...
edit_menu = tk.Menu(menu, tearoff=False)
edit_menu.add_command(label="Cut", command= lambda: print("Cut"))
edit_menu.add_command(label="Copy", command= lambda: print("Copy"))
menu.add_cascade(label="Edit", menu=edit_menu)

# Sub Menu for Paste...
paste_menu = tk.Menu(edit_menu, tearoff=False)
paste_menu.add_command(label="Paste", command= lambda: print("Paste"))
paste_menu.add_command(label="Paste Special", command= lambda: print("Paste Special"))
edit_menu.add_cascade(label="Paste", menu=paste_menu)

""" Menu BUtton"""
# Create a Menu Button
menu_button = tk.Menubutton(window, text="Menu Button", relief="raised")
menu_button.pack()

# Create a Sub Menu for the Menu Button

sub_menu = tk.Menu(menu_button, tearoff=False)
sub_menu.add_command(label="Sub Menu 1", command= lambda: print("Sub Menu 1"))
sub_menu.add_command(label="Sub Menu 2", command= lambda: print("Sub Menu 2"))
menu_button.config(menu=sub_menu)


# Start the main event loop
window.mainloop()