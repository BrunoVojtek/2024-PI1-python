import tkinter as tk
from random import shuffle

root = tk.Tk()

cisla = list(range(1,9))*2
shuffle(cisla)

stav = {
"prva_karta" : None,
"druha_karta" : None,
"tlacidla" : []
}

def kontrola_kariet():
    prva_index = stav["prva_karta"]
    druha_index = stav["druha_karta"]

    if prva_index is not None and druha_index is not None:
        if cisla[prva_index] == cisla[druha_index]:
            stav["tlacidla"][prva_index]["state"] = "disabled"
            stav["tlacidla"][druha_index]["state"] = "disabled"
        else:
            stav["tlacidla"][prva_index]["text"] = ""
            stav["tlacidla"][druha_index]["text"] = ""
        stav["prva_karta"] = None
        stav["druha_karta"] = None
    
def klik(index):
    if stav["prva_karta"] is None:
        stav["prva_karta"] = index
        stav["tlacidla"][index]["text"] = str(cisla[index])
    elif stav["druha_karta"] is None and index != stav["prva_karta"]:
        stav["druha_karta"] = index
        stav["tlacidla"][index]["text"] = str(cisla[index])
    root.after(2000, kontrola_kariet)

for i in range(4):
    for j in range(4):
        index = i*4+j
        button = tk.Button(root, text="", width=6, height=3, command= lambda idx = index: klik(idx))
        button.grid(row=i, column=j)
        stav["tlacidla"].append(button)



tk.mainloop()        