import random
import tkinter
pocet = int(input("Zadaj počet jednotiek: "))
canvas = tkinter.Canvas(width=500,height=400)
canvas.pack()


prvy = random.choice(["yellow","red","blue"])
druhy= random.choice(["yellow","red","blue"])
treti= random.choice(["yellow","red","blue"])
stvrty= random.choice(["yellow","red","blue"])
piaty= random.choice(["yellow","red","blue"])
siesty= random.choice(["yellow","red","blue"])
siedmy= random.choice(["yellow","red","blue"])
osmy= random.choice(["yellow","red","blue"])
deviaty= random.choice(["yellow","red","blue"])
desiaty= random.choice(["yellow","red","blue"])

def jednotka (x,y):
    x =random.randint(3,500-33)
    y = random.randint(3,400-73)
    canvas.create_rectangle(x,y+10,x+10,y+20,fill=prvy)
    canvas.create_rectangle(x,y+60,x+10,y+70,fill=druhy)
    canvas.create_rectangle(x+10,y,x+20,y+10,fill=treti)
    canvas.create_rectangle(x+10,y+10,x+20,y+20,fill=stvrty)
    canvas.create_rectangle(x+10,y+20,x+20,y+30,fill=piaty)
    canvas.create_rectangle(x+10,y+30,x+20,y+40,fill=siesty)
    canvas.create_rectangle(x+10,y+40,x+20,y+50,fill=siedmy)
    canvas.create_rectangle(x+10,y+50,x+20,y+60,fill=osmy)
    canvas.create_rectangle(x+10,y+60,x+20,y+70,fill=deviaty)
    canvas.create_rectangle(x+20,y+60,x+30,y+70,fill=desiaty)

for i in range (pocet):
    jednotka(10,10)




# jednotka(10,10)
tkinter.mainloop()