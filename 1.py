import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
import os

root = tk.Tk()
root.title("релакс рисование")

canvas = tk.Canvas(root, width=1000, height=800, bg='white')
canvas.pack()

current_color = "black"

def change_color(color):
    global current_color
    current_color = color

colors = ["black", "red", "green", "pink", "gray", "blue", "yellow", "violet", "darkgreen", "orange"]
for color in colors:
    color_button = tk.Button(root, bg=color, width=2, command=lambda c=color: change_color(c))
    color_button.pack(side='right')

def draw(event):
    x, y = event.x, event.y
    canvas.create_oval(x, y, x + 4, y + 4, fill=current_color, width=0)

def save_image():
    filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("png files", "*.png")])
    if filename:
        temp_postscript_file = "temp_canvas.eps"
        canvas.postscript(file=temp_postscript_file, colormode='color')

        with open(temp_postscript_file, 'r') as file:
            img = Image.open(temp_postscript_file)
            img.save(filename, "png")

        messagebox.showinfo("сохранение", "изображение успешно сохранено!")

def show_image():
    filename = filedialog.askopenfilename(filetypes=[("png files", "*.png")])
    if filename:
        opened_image = Image.open(filename)
        opened_image.show()

save_button = tk.Button(root, text="сохранить", command=save_image)
save_button.pack(side='left')

show_button = tk.Button(root, text="показать", command=show_image)
show_button.pack(side='left')

canvas.bind("<B1-Motion>", draw)

root.mainloop()