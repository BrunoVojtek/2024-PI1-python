import tkinter as tk

r = tk.Tk()
c = tk.Canvas(r, width=400, height=400)
c.pack()

fbody = open("body.txt", "r") 
riadky = fbody.readlines()

for i in range(0, len(riadky), 3):
    obrys = riadky[i].strip()
    farba = riadky[i+1].strip()
    pozícia = riadky[i+2].strip()

    medzera = pozícia.find(" ")
    x = int(pozícia[:medzera])
    y = int(pozícia[medzera+1:])

    if obrys == "o":
        c.create_oval(x - 5, y - 5, x + 5, y + 5, fill=farba)
    elif obrys == "r":
        c.create_rectangle(x - 5, y - 5, x + 5, y + 5, fill=farba)


r.mainloop()