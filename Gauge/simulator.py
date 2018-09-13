import tkinter as tk
from gauge import Gauge



i=0

def Increase():
    global i, gauge1
    i+=1
    gauge1.setGauge(i, setcolor(i))


def Decrease():
    global i, gauge1
    i-=1
    gauge1.setGauge(i, setcolor(i))


def setcolor(value):
    greenuntil=4.0
    yellowuntil=6.0
    orangeuntil=8.0
    if value<=greenuntil:
        return "green"
    elif value>greenuntil and value<=yellowuntil:
        return "gold3"
    elif value>yellowuntil and value <=orangeuntil:
        return "orange"
    else:
        return "red"



root=tk.Tk()
width=200
gaugefrom=0
gaugeto=10
IsLabel=True

gauge1=Gauge(root,width,gaugefrom,gaugeto, IsLabel)
gauge1.pack()

tk.Button(root, text=" + ", command=Increase).pack()
tk.Button(root, text=" - ", command=Decrease).pack()

root.mainloop()
