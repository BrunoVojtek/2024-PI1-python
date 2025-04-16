import tkinter as tk
import random


r = tk.Tk()


cisla = list(range(1,9)) * 2
random.shuffle(cisla)

stav = {
    "prva_karta":None,
    "druha_karta":None,
    "tlacidla":[]
}

def kontrola_kariet():
    prva = stav["prva_karta"]
    druha = stav["druha_karta"]

    if prva is not None and druha is not None:
        if cisla[prva] == cisla[druha]:
            stav["tlacidla"][prva]["state"] = "disabled"
            stav["tlacidla"][druha]["state"] = "disabled"
        else:
            stav["tlacidla"][prva]["text"] = ""
            stav["tlacidla"][druha]["text"] = ""
        stav["prva_karta"] = None
        stav["druha_karta"] = None

def klik(index):
    if stav["prva_karta"] is None:
        stav["prva_karta"] = index
        stav["tlacidla"][index]["text"] = str(cisla[index])
    elif stav["druha_karta"] is None and index != stav["prva_karta"]:
        stav["druha_karta"] =index
        stav["tlacidla"][index]["text"] = str(cisla[index])
        r.after(500, kontrola_kariet)  





for i in range(4):
    for j in range(4):
        index = i*4+j
        button = tk.Button(r, text="", width=6, height=3, command=lambda idx=index: klik(idx))
        button.grid(row=i, column=j)
        stav["tlacidla"].append(button)


tk.mainloop()