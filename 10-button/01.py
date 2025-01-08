import tkinter as Tk

root = Tk.Tk()
root.geometry("200x200")

def akcia():
    label.config(text = textbox.get())
    

label = Tk.Label(root, text="Som LABEL")
label.pack()

textbox = Tk.Entry(root)
textbox.pack()

button = Tk.Button(root, text = "Som tlačidlo", command=akcia)
button.pack()


Tk.mainloop()