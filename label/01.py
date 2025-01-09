import tkinter as tk 
import random as rd


counter = 1



def AkciaTlacidla():
    global counter
    mojeCislo = int(textbox.get())
    if mojeCislo < cisloPC:
        label.config(text= "Dal si menšie číslo")
        counter += 1
    elif mojeCislo > cisloPC:
        label.config(text= "Dal si väčšie číslo")
        counter += 1
    else:
        label.config (text= f"Uhádol si, počet pokusov je: {counter}")


root = tk.Tk()
root.geometry ("200x200")

button = tk.Button(root, text= "Apply", command= AkciaTlacidla)
button.pack()

cisloPC = rd.randint(0,9)

label = tk.Label(root, text="Hádaj")
label.pack()

textbox = tk.Entry(root)
textbox.pack()


tk.mainloop()