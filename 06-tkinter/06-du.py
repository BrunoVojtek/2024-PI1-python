import tkinter
canvas = tkinter.Canvas()
canvas.pack()
# prvy stlpec
canvas.create_rectangle(10,10,20,20)
canvas.create_rectangle(10,20,20,30)
canvas.create_rectangle(10,30,20,40)
canvas.create_rectangle(10,40,20,50)
canvas.create_rectangle(10,50,20,60)
canvas.create_rectangle(10,60,20,70)
canvas.create_rectangle(10,70,20,80)
#druhy stlpec
canvas.create_rectangle(30,10,20,20)
canvas.create_rectangle(30,40,20,50)
canvas.create_rectangle(30,70,20,80)





tkinter.mainloop()