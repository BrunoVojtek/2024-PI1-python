import tkinter as tk 
import random as rd


counter = 1
bet = 100

def bet(money):
    while True:
        try:
            bet = int(input(f"Bet between 1 to {money}: "))
        except Exception:
            print("Your bet is not integer \n")
            continue
        if bet in range(1,money + 1):
            print(f"Your bet is {bet} \n")
            break

        else:
            print(f"Your bet is out of the range. Please bet between 1 to {money} \n")
            continue
    return bet


def AkciaTlacidla1():
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

def AkciaTlacidla2():
    global bet                                       
    mojeCislo = int(textbox.get())
    bet = int(textbox2.get())
    if mojeCislo < cisloPC:
        bet = bet / 2
    elif mojeCislo > cisloPC:
        bet = bet / 2
    else:
        bet = bet * 2  



root = tk.Tk()
root.attributes("-fullscreen", True)
root.state = False


# frame = tk.Frame(root)
# frame.pack(expand=True)

button_exit_2 = tk.Button(root,text="x",width=8   ,bg="red" , command=root.destroy,)
button_exit_2.place(relx=1.0, rely=0.0, anchor='ne')
                                                                
cisloPC = rd.randint(0,9)

label = tk.Label(root, text="Zadaj svoju stávku: ")
label.pack()

textbox2 = tk.Entry(root)
textbox2.pack()

button2 = tk.Button(root, text= "Apply", command= bet)
button2.pack()


label = tk.Label(root, text="Hádaj")
label.pack()

textbox = tk.Entry(root)
textbox.pack()

button = tk.Button(root, text= "Apply", command= AkciaTlacidla1)
button.pack()



tk.mainloop()