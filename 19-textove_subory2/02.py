import tkinter as tk
import random

subor = open("tvary.txt", "r", encoding="utf-8")
riadky = subor.readlines()

for i in riadky:
    rozdelenie = i.strip()
    list_rozdelenie = rozdelenie.split()
    typ = list_rozdelenie[0]
    x1 = list_rozdelenie[1]    
    y1 = list_rozdelenie[2]
    x2 = list_rozdelenie[3]
    y2 = list_rozdelenie[4]


print(x1)
