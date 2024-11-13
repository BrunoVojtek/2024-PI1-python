import tkinter
canvas = tkinter.Canvas(width=600, height=600)
canvas.pack()

def xko(x, y): # definicica funkcie, xko nazov (ten udavame my), ( ) su to tzv. parametre funkcie

    canvas.create_rectangle(x,y,x+10,y+10,fill="black")
    canvas.create_rectangle(x,y+10,x+10,y+20,fill="black")
    canvas.create_rectangle(x+10,y+20,x+20,y+30,fill="black")
    canvas.create_rectangle(x+20,y+30,x+30,y+40,fill="black")
    canvas.create_rectangle(x+10,y+40,x+20,y+50,fill="black")
    canvas.create_rectangle(x,y+50,x+10,y+60,fill="black")
    canvas.create_rectangle(x,y+60,x+10,y+70,fill="black")
    canvas.create_rectangle(x+30,y+20,x+40,y+30,fill="black")
    canvas.create_rectangle(x+40,y+10,x+50,y+20,fill="black")
    canvas.create_rectangle(x+40,y,x+50,y+10,fill="black")
    canvas.create_rectangle(x+40,y+50,x+50,y+60,fill="black")
    canvas.create_rectangle(x+40,y+60,x+50,y+70,fill="black")
    canvas.create_rectangle(x+30,y+40,x+40,y+50,fill="black")

def riadok_x(x, y, pocet):

        for i in range(pocet):
             xko(x, y)
             x += 60

def riadky_x(x, y , pocet_riadkov, pocet_stlpcov):

     for i in range (pocet_riadkov):
       riadok_x(x, y, pocet_stlpcov)   
       y += 80
        


# xko(10, 10) # volanie funkcie
# xko(70, 10)
# xko(130, 10)

# x = 10
# y = 10
# x_save = x
# odsadenie_x = 60
# odsadenie_y = 80
# pocet_riadkov = 5
# pocet_stlpcov = 5

# for z in range(pocet_riadkov):
#     for i in range(pocet_stlpcov):
#         xko(x, y)
#         x += odsadenie_x
#     y += odsadenie_y
#     x = x_save 


xko(10, 10)
riadok_x(10, 100, 3)
riadky_x(10, 190, 3, 4)


tkinter.mainloop()