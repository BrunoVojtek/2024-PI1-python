import tkinter as tk
import random

counter = 1


def akciaTlacidla():
    global counter, cisloPC
    mojeCislo = int(textbox.get())
    if mojeCislo < cisloPC:
        label.config(text="Dal si menšie číslo")
        counter += 1
    elif mojeCislo > cisloPC:
        label.config(text="Dal si väčšie číslo")
        counter +=1
    else:
        label.config(text=f"Uhádol si, počet pokusov: {counter}")
        



root = tk.Tk()
root.geometry("200x200")

cisloPC = random.randint(0,9)

label = tk.Label(root, text= "Hádaj číslo")
label.pack()

textbox = tk.Entry(root)
textbox.pack()

button = tk.Button(root, text= "Hádaj", command=akciaTlacidla)
button.pack()




tk.mainloop()
