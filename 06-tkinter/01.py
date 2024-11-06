import tkinter

canvas = tkinter.Canvas()  # vytvorenie platna a jeho priradenie do premennej canvas
canvas.pack()  # umiestnenie platna do okna 

canvas.create_text(100,75,text="Ahoj") 
# vypise text "Ahoj" na pozicii x= 100, y= 100
# suradnice zadavame vzdy v poradi x a potom y
# x rastie smerom doprava ale y rastie smerom dole
canvas.create_rectangle(50, 50, 150, 100)
# vykreslenie stvorca resp. obdlznika
# prve dve cisla urcuju poziciu zaciatocneho bodu
# dalsie dve urcuju poziciu koncoveho bodu

canvas.create_oval(50, 50, 150, 100)
# vykreslenie kruhu resp. elipsy
# prve dve cisla urcuju poziciu zaciatocneho bodu
# dalsie dve urcuju poziciu koncoveho bodu

tkinter.mainloop() # aby zostalo okno otvorene, aby sa nezavrelo
