
import tkinter
canvas = tkinter.Canvas(height=600, width=600)
canvas.pack()
def srdcove_eso(x,y):

    canvas.create_rectangle(x,y,x+90,y+150)

    canvas.create_text(x+10,y+15,text="A")







srdcove_eso(10,10)

tkinter.mainloop()