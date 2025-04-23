import tkinter as tk

root = tk.Tk()
c = tk.Canvas(root, width=400, height=400)
c.pack()

with open("body.txt", "r") as fbody:
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


root.mainloop()