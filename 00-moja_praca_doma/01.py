import tkinter
canvas = tkinter.Canvas(width=600, height=600)
canvas.pack()
def yps(x,y,color, outline_color):
    canvas.create_rectangle(x, y, x+10, y+10, fill=color, outline=outline_color)
    canvas.create_rectangle(x, y+10, x+10, y+20, fill=color, outline=outline_color)
    canvas.create_rectangle(x+10,y+20,x+20,y+30, fill=color, outline=outline_color)
    canvas.create_rectangle(x+20, y+30, x+30, y+40, fill=color, outline=outline_color)
    canvas.create_rectangle(x+20, y+40, x+30, y+50, fill=color, outline=outline_color)
    canvas.create_rectangle(x+20, y+50, x+30, y+60, fill=color, outline=outline_color)
    canvas.create_rectangle(x+20, y+60, x+30, y+70,fill=color, outline=outline_color)
    canvas.create_rectangle(x+30, y+20, x+40, y+30, fill=color, outline=outline_color)
    canvas.create_rectangle(x+40, y+10, x+50, y+20, fill=color, outline=outline_color)
    canvas.create_rectangle(x+40, y, x+50, y+10, fill=color, outline=outline_color)

def riadok (x,y,color,outline_color,pocet):
    for i in range (pocet):
        yps(x,y,color,outline_color)
        x+=70

riadok(10,10,input("Zadaj farbu štvorčekov: "), input("Zadaj farbu pozadia štvorčekov: "), int(input("Zadaj počet riadkov: ")) )





tkinter.mainloop()