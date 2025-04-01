import tkinter as tk
import random

veta = input("Zadaj vetu: ")
slova = veta.split()

c = tk.Canvas(width=800, height=600)
c.pack()

for slovo in slova:
    x = random.randint(10, 700)
    y = random.randint(10, 500)
    for pismeno in slovo:
        farba_pismena = f'#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}'
        c.create_text(x, y, fill=farba_pismena, text=pismeno)
        x += 20  

tk.mainloop()