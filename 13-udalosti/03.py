import tkinter as tk

current_color = 'red'



def change_color(color):
    global current_color
    current_color = color

def klik(event):
    x, y = event.x, event.y
    canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill=current_color)

def tahaj(event):
    x = velkost.get()
    y = velkost.get()
    x, y = event.x, event.y
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill=current_color, outline=current_color)



canvas = tk.Canvas()
canvas.pack(side='left')
canvas.bind('<ButtonPress>', klik)
canvas.bind('<B1-Motion>', tahaj)

def delete():
    canvas.delete("all")


tk.Button(text="Vymazať", command=delete).pack()

red_button = tk.Button( width=5,background="red", command=lambda: change_color('red'))
red_button.pack()

blue_button = tk.Button( width=5,background="Blue", command=lambda: change_color('blue'))
blue_button.pack()

green_button = tk.Button( width=5,background="Green", command=lambda: change_color('green'))
green_button.pack()

tk.Label(text='Zmeň veľkosť:').pack()
velkost = tk.Scale(orient='horizontal', from_=10, to=40, length=75)
velkost.pack()


tk.mainloop()