import turtle
t = turtle.Turtle()
turtle.delay(0)
t.speed(0)
t.hideturtle()

x = -450
y = 350
t.pu()
t.setpos(x,y)
t.pd()



pocet_v_riadku = 23
dlzka = 30
pocet_stlpcov = 11




def stvorec(dlzka):
    t.fillcolor("red")
    t.begin_fill()
    for i in range(4):
        t.fd(dlzka)
        t.rt(90)
    t.end_fill()
    t.pu()
    t.fd(dlzka/4)
    t.rt(90)
    t.fd(dlzka/4)
    t.lt(90)
    t.pd()
    t.fillcolor("white")
    t.begin_fill()
    for i in range(4):
        t.fd(dlzka/2)
        t.rt(90)
    t.end_fill()
    t.fd(dlzka/4)
    t.rt(90)
    t.fd(dlzka/2)
    t.rt(90)
    t.fd(dlzka/4)
    t.rt(90)
    t.fd(dlzka/4)
    t.rt(90)
    t.fd(dlzka/2)
    t.lt(90)
    t.pu()
    t.fd(dlzka/2)
    t.lt(90)
    t.fd(dlzka/4)
    t.fd(dlzka/2)
    t.rt(180)
    t.pd()

def trojuholnik(dlzka):
    t.fillcolor("black")
    t.begin_fill()
    for i in range(3):
        t.fd(dlzka)
        t.rt(120)
    t.end_fill()

def dom(d):   
    stvorec(d)
    t.lt(60)
    trojuholnik(d)
    t.rt(60)



def dedina():
    global y
    for i in range(pocet_stlpcov):
     
        for i in range(pocet_v_riadku):
            dom(dlzka)
            t.pu()
            t.fd(dlzka+10)
            t.pd()
        t.pu()
        y = y-70
        t.setpos(x,y)
        t.pd()

dedina()

turtle.exitonclick()

