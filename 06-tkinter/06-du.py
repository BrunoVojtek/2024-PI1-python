import tkinter
canvas = tkinter.Canvas()
canvas.pack ()
#prvy stlpec
canvas.create_rectangle(10,12,20,22,fill="black")
canvas.create_rectangle(10,24,20,34,fill="black")
canvas.create_rectangle(10,36,20,46,fill="black")
canvas.create_rectangle(10,48,20,58,fill="black")
canvas.create_rectangle(10,60,20,70,fill="black")
canvas.create_rectangle(10,72,20,82,fill="black")
canvas.create_rectangle(10,84,20,94,fill="black")
#druhy stlpec
canvas.create_rectangle(32,12,22,22,fill="black")
canvas.create_rectangle(32,48,22,58,fill="black")
canvas.create_rectangle(32,84,22,94,fill="black")
#treti stlpec
canvas.create_rectangle(34,12,44,22,fill="black")
canvas.create_rectangle(34,48,44,58,fill="black")
canvas.create_rectangle(34,84,44,94,fill="black")
#stvrty stlpec
canvas.create_rectangle(46,12,56,22,fill="black")
canvas.create_rectangle(46,48,56,58,fill="black")
canvas.create_rectangle(46,84,56,94,fill="black")
#piaty stlpec
canvas.create_rectangle(58,24,68,34,fill="black")
canvas.create_rectangle(58,36,68,46,fill="black")

canvas.create_rectangle(58,60,68,70,fill="black")
canvas.create_rectangle(58,72,68,82,fill="black")
#v
#prvy stlpec
canvas.create_rectangle(92,12,102,22,fill="black")
canvas.create_rectangle(92,24,102,34,fill="black")
canvas.create_rectangle(92,36,102,46,fill="black")
canvas.create_rectangle(92,48,102,58,fill="black")
#druhy stlplec
canvas.create_rectangle(102,60,112,70,fill="black")
canvas.create_rectangle(102,72,112,82,fill="black")
#treti stlpec
canvas.create_rectangle(114,84,124,94,fill="black")
#stvrty stlpec
canvas.create_rectangle(126,72,136,82,fill="black")
canvas.create_rectangle(126,60,136,70,fill="black")
#piaty stlpec
canvas.create_rectangle(138,48,148,58,fill="black")
canvas.create_rectangle(138,36,148,46,fill="black")
canvas.create_rectangle(138,24,148,34,fill="black")
canvas.create_rectangle(138,12,148,22,fill="black")



tkinter.mainloop()