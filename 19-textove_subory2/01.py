import tkinter as tk
import random
file = open ("tvary.txt", "w", encoding="utf-8")
c = tk.Canvas()
c.pack()

width = 800
height = 800
odsadenie = 5


for i in range(10):
    type = random.choice("o""r""l")
    x1 = random.randint(odsadenie, width - odsadenie)
    y1 = random.randint(odsadenie, height - odsadenie)
    x2 = random.randint(odsadenie, width - odsadenie)
    y2 = random.randint(odsadenie, height - odsadenie)
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    file.write(f"{type} {x1} {y1} {x2} {y2} {r} {g} {b}\n")
    farba = f"#{r:02x}{g:02x}{b:02x}"
    if type == "r":
        c.create_rectangle(x1,y1,x2,y2,fill=farba)
    elif type == "o":
        c.create_oval(x1,y1,x2,y2, fill=farba)
    else:
        c.create_line(x1,y1,x2,y2,fill=farba)



tk.mainloop()



