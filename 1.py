import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageGrab

# cоздаем главное окно класса Tk
root = tk.Tk()
root.title("Relax drawing")

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
    canvas.create_oval(x, y, x+4, y+4, fill=current_color, width=0)

def save_image():
    x = root.winfo_rootx() + canvas.winfo_x()
    y = root.winfo_rooty() + canvas.winfo_y()
    x1 = x + canvas.winfo_width()
    y1 = y + canvas.winfo_height()
    # открываем диалоговое окно для сохранения файла и возвращаем путь к сохранённому файлу
    filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("png files", "*.png")])
    if filename:
        image = ImageGrab.grab(bbox=(x, y, x1, y1))
        image.save(filename)
        messagebox.showinfo("сохранение", "Изображение сохранено успешно!")

def show_image():
    filename = filedialog.askopenfilename(filetypes=[("png files", "*.png")])
    if filename:
        image = Image.open(filename)
        image.show()

save_button = tk.Button(root, text="Сохранить", command=save_image)
save_button.pack(side='left')

show_button = tk.Button(root, text="Показать", command=show_image)
show_button.pack(side='left')

canvas.bind("<B1-Motion>", draw)
root.mainloop()
