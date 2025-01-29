import random
import tkinter 

canvas_width = int(input("Šírka plátna: "))
canvas_height = int(input("Výška plátna: "))
pocet = int(input("Zadaj počet štvorcov: "))

canvas = tkinter.Canvas(width=canvas_width,height=canvas_height)
canvas.pack()



for i in range (pocet):
    velkost = random.randint(1,30)
    x = random.randint(3,canvas_width-3-velkost)
    y = random.randint(3,canvas_height-3-velkost)
    



    if velkost < 10:
        color = "Red"
    elif velkost > 10 and velkost < 20:
        color = "Green"
    else: 
        color = "Blue"


    canvas.create_rectangle(x,y,x+velkost,y+velkost,fill=color, width=0,)









tkinter.mainloop()