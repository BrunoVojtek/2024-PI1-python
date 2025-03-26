import tkinter as tk
import random

c = tk.Canvas(width=800, height=600)
c.pack()
for i in range(1000):
    x = random.randint(3,700)
    y = random.randint(3,500)
    farba = f'#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}'
    c.create_rectangle(x,y,x+40,y+40, fill=farba)



tk.mainloop()