""" A canvas is a widget that allows you to draw shapes, images, and text on it."""
import tkinter as tk

""" setup """
window = tk.Tk()
window.title("Canvas Demo")
window.geometry("400x400")

""" canvas """
canvas = tk.Canvas(master=window, width=400, height=400, bg="white")
canvas.pack()

canvas.create_rectangle(10, 10, 50, 50, fill="red") # x1, y1, x2, y2, width= would be border width
canvas.create_line(100, 10, 50, 50, fill="blue") # x1, y1, x2, y2
canvas.create_oval(100, 100, 150, 150, fill="green") # x1, y1, x2, y2
canvas.create_polygon(50, 50, 250, 250, 200, 250, fill="yellow") # x1, y1, x2, y2, x3, y3
canvas.create_arc(200, 200, 300, 300, start=0, extent=160, fill="purple", style = tk.ARC) # x1, y1, x2, y2, start=, extent=

canvas.create_text(200, 200, text="Hello, World!", font="Arial 20 bold", fill="black") # x, y - text center

canvas.create_window(200, 200, window=tk.Button(master=canvas, text="Click Me")) # x, y, window= - add a widget to the canvas 
# this window has nothing to do with the main window

""" run """
window.mainloop()