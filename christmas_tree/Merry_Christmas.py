import tkinter as tk
import random


colors=["white","red", "purple", "yellow", "orange","blue","violet","pink"]

Xmins=[140,180,160,180,200,225]
Xmaxs=[360,320,340,300,300,275]
Ymins=[400,370,300,290,200,170]
Ymaxs=[440,400,340,300,240,200]
lights=[]
snow=[]

def blink(*args):
    global lights, landscape, counter, colors
    for light in lights:
        landscape.itemconfig(light, fill=random.choice(colors))
    root.after(150, blink)


def decoratewithlights(*args):
    global landscape
    for j in range(0,int(len(Xmins))):
        for i in range(0,15):
            x=random.randint(Xmins[j],Xmaxs[j])
            y=random.randint(Ymins[j],Ymaxs[j])
            ornament=landscape.create_oval(x, y, x + 5, y + 5, fill="green", outline="green")
            lights.append(ornament)




root=tk.Tk()
root.title("Merry Christmas")
landscape=tk.Canvas(root, width=500, height=500, bg="skyblue")
landscape.pack()
christmastreebranch1=landscape.create_polygon(250, 350, 50, 450, 450, 450, fill="green")
christmastreebranch2=landscape.create_polygon(250, 250, 100, 350, 400, 350, fill="green")
christmastreebranch3=landscape.create_polygon(250, 150, 150, 250, 350, 250, fill="green")
landscape.create_rectangle(230,450,270,480, fill="brown", outline="brown")
decoratewithlights()
blink()
root.mainloop()