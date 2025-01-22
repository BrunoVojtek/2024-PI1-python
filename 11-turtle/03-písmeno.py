import turtle
t = turtle.Turtle()
# turtle.delay(0)
t.hideturtle()

dlzka = 10

def stvorkova_ciara():
    for x in range(4):
        stvorec(dlzka)
        t.fd(10)

def stvorec(d):
    for i in range(4):
        t.fd(d)
        t.lt(90)

def sedmickova_ciara():
    for n in range(7):
        stvorec(dlzka)
        t.fd(10)
def dvojkova_ciara():
    for n in range(2):
        stvorec(dlzka)
        t.fd(10)



t.rt(90)
sedmickova_ciara()
t.lt(90)
stvorkova_ciara()
t.pu()
t.fd(10)
stvorec(dlzka)
t.lt(90)
t.fd(10)
t.pd()
dvojkova_ciara()
t.pu()
t.fd(10)
t.pd()
dvojkova_ciara()
t.pu()
t.fd(10)
t.lt(90)
t.fd(10)
t.pd()
stvorkova_ciara()
t.lt(90)
stvorkova_ciara()
t.lt(90)
stvorkova_ciara()

turtle.exitonclick()