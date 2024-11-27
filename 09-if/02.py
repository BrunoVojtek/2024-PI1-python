import random
import tkinter 

pocet = 10000
canvas_width = int(input("Šírka plátna: "))
canvas_height = int(input("Výška plátna: "))


canvas = tkinter.Canvas(width=canvas_width,height=canvas_height)
canvas.pack()

for i in range (pocet):
    a = 10
    x = random.randint(3,canvas_width-3-a)
    y = random.randint(3,canvas_height-3-a)

    # if x < canvas_width / 2  and y < canvas_height / 2 :   #Zložená podmienka
    #     color = "Blue"
    # elif x > canvas_width / 2  and y < canvas_height / 2 :
    #     color = "Red"
    # elif x > canvas_width / 2 and y > canvas_height / 2:
    #     color = "Yellow"
    # elif x < canvas_width / 2 and y > canvas_height / 2:
    #     color = "Green"
    # else: 
    #     continue

    if x < canvas_width / 2:
        if y < canvas_height / 2:
            color = "blue"
        else:
            color = "green"
    else:
        if y < canvas_height / 2:
            color = "red"
        else:
             color = "yellow"
    
    canvas.create_oval (x,y,x+10,y+10,fill= color)







tkinter.mainloop()