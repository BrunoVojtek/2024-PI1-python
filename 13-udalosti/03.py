import tkinter as tk
from tkinter import colorchooser

current_color = 'red'

def on_entry_click(event):
    if entry.get() == "Zadaj veľkosť:":
        entry.delete(0, "end")
        entry.unbind('<FocusIn>')
    else:
        return

def update_scale(event):
    try:
        size = int(entry.get())
        if 1 <= size <= 40:
            velkost.set(size)
    except ValueError:
        pass

def change_color(color):
    global current_color
    current_color = color

def choose_color():
    color_code = colorchooser.askcolor(title="Choose color")
    if color_code:
        change_color(color_code[1])
    else:
        return

def tahaj(event):
    try:
        size = int(entry.get())
    except ValueError:
        size = velkost.get()
    x, y = event.x, event.y
    canvas.create_oval(x - size, y - size, x + size, y + size, fill=current_color, outline=current_color)

canvas = tk.Canvas(width=700, height=500)
canvas.pack(side='left')
canvas.bind('<B1-Motion>', tahaj)

def delete():
    canvas.delete("all")



tk.Button(text="Vyber farbu", command=choose_color).pack()
tk.Button(text="Vymazať", command=delete).pack()
tk.Button(text="Guma", background="white", command=lambda: change_color("White")).pack()

entry = tk.Entry()
entry.pack()
entry.insert(0, "Zadaj veľkosť:")
entry.bind('<FocusIn>', on_entry_click)
entry.bind('<KeyRelease>', update_scale)

velkost = tk.Scale(orient='horizontal', from_=1, to=40, length=75)
velkost.pack()

tk.mainloop()