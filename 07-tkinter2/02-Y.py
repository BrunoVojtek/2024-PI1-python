import tkinter
canvas = tkinter.Canvas(width=600, height=600)
canvas.pack()
def yps(x, y, color):

    canvas.create_rectangle(x, y, x+10, y+10, fill=color)
    canvas.create_rectangle(x, y+10, x+10, y+20, fill=color)
    canvas.create_rectangle(x+10,y+20,x+20,y+30, fill=color)
    canvas.create_rectangle(x+20, y+30, x+30, y+40, fill=color)
    canvas.create_rectangle(x+20, y+40, x+30, y+50, fill=color)
    canvas.create_rectangle(x+20, y+50, x+30, y+60, fill=color)
    canvas.create_rectangle(x+20, y+60, x+30, y+70,fill=color)
    canvas.create_rectangle(x+30, y+20, x+40, y+30, fill=color)
    canvas.create_rectangle(x+40, y+10, x+50, y+20, fill=color)
    canvas.create_rectangle(x+40, y, x+50, y+10, fill=color)

def riadok_y(x,y,color, pocet):
    for i in range(pocet):
        yps(x, y, color)
        x += 70
def riadky_y(x,y,pocet_riadkov,pocet_stlpcov):
    for i in range(pocet_stlpcov):
        riadok_y (x, y, pocet_riadkov)
        y += 80




yps(10,10,"black")

riadok_y(10, 90,"black",  3)
 
# riadky_y(10, 180, 4, 5)


tkinter.mainloop()