import tkinter as tk

c = tk.Canvas()
c.pack()

fbody = open ("body.txt", "r")
for body in fbody:
    print(body)
    medzera = body.find(" ")
    print(medzera)
    x = int(body[:medzera])
    y = int(body[medzera+1:])
    print(x)
    print(y)
    c.create_oval(x-5,y-5,x+5,y+5)


fbody.close()
tk.mainloop()
