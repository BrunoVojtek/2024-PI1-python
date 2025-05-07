import tkinter as tk
import random

subor = open("tvary.txt", "r", encoding="utf-8")
riadky = subor.readlines()

c = tk.Canvas()
c.pack()


for i in riadky:
    rozdelenie = i.strip()
    list_rozdelenie = rozdelenie.split()
    typ = list_rozdelenie[0]
    x1 = int(list_rozdelenie[1])    
    y1 = int(list_rozdelenie[2])
    x2 = int(list_rozdelenie[3])
    y2 = int(list_rozdelenie[4])
    r = int(list_rozdelenie[5])
    g = int(list_rozdelenie[6])
    b = int(list_rozdelenie[7])
    farba = f"#{r:02x}{g:02x}{b:02x}"
    if typ == "o":
        c.create_oval(x1,y1,x2,y2, fill=farba)
    elif typ == "r":
        c.create_rectangle(x1,y1,x2,y2,fill=farba)
    else:
        c.create_line(x1,y1,x2,y2,fill=farba)



tk.mainloop()