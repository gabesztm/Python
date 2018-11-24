import tkinter as tk
from random import choice

version="v1.0 ™.G"

defaultkeycolor="grey"

characterlist=["ö","ü","ó","q",
               "w","e","r","t",
               "z","u","i","o",
               "p","ő","ú","a",
               "s","d","f","g",
               "h","j","k","l",
               "é","á","ű","í",
               "y","x","c","v",
               "b","n","m",",",
               ".","-"]

keyobjects=[]
TARGET=""
targetssofar=-1     # makes accuracy correct
pressedkeyssofar=0


def drawkeys(*args):
    global keyframe, characterlist, keyobjects
    r=0
    c=9   #on Hungarian keyboard the first letter starts on 9th place
    for character in characterlist:
        key=tk.Label(keyframe, text=character, width=5, height=2, bg=defaultkeycolor)
        key.grid(row=r, column=c, padx=1, pady=1)
        keyobjects.append(key)
        c+=1
        if c==12:
            r+=1
            c=0


def showtarget(*args):
    global keyframe, characterlist, keyobjects, TARGET, targetssofar
    target=choice(characterlist)
    while target==TARGET:
        target=choice(characterlist)
    targetnumber=characterlist.index(target)
    TARGET = target
    keyobjects[targetnumber].config(bg="goldenrod4")
    targetssofar+=1


def colorrange(number):
    if number>=80:
        return "green"
    if number>=60 and number <80:
        return "yellow"
    if number>=40 and number <60:
        return "orange"
    else:
        return "red"


def updatestats(*args):
    global promptsC, actionsC, accuracyC
    promptsC.config(text=targetssofar)
    actionsC.config(text=pressedkeyssofar)
    accuracy="{:.2f}".format(targetssofar*100/pressedkeyssofar)
    accuracyC.config(text=accuracy+"%", fg=colorrange(float(accuracy)))



def keypress(key):
    global keyobjects, TARGET, pressedkeyssofar
    try:
        pressedkey=str(key).split('char=')[1][1]
        try:
            pressedkeynumber=characterlist.index(pressedkey)
            if pressedkey==TARGET:
                colorkey(pressedkeynumber,"green")
                showtarget()
            else:
                colorkey(pressedkeynumber,"red")
        except ValueError:      # e.g. pressed a number key
            pass
    except IndexError:          # e.g. pressed ctrl key
        pass
    pressedkeyssofar += 1
    updatestats()


def colorkey(key,color):
    global keyobjects
    keyobjects[key].config(bg=color)
    root.after(200, lambda: keyobjects[key].config(bg=defaultkeycolor))

def defaultcolorkey(color):
    global keyobjects
    for key in keyobjects:
        key.config(bg=defaultkeycolor)





def newsession(*args):
    showtarget()




root =tk.Tk()
root.title("Gépírás")
statframe=tk.Frame(root)
statframe.grid(row=0, column=0, pady=30)
prompts=tk.Label(statframe, text="Célok:",font=25, justify="left", width=10)
prompts.grid(row=0, column=0)
promptsC=tk.Label(statframe, text="",font=25, justify="right", width=8)
promptsC.grid(row=0,column=1)
actions=tk.Label(statframe, text="Leütések:",font=25, justify="left", width=10)
actions.grid(row=1, column=0)
actionsC=tk.Label(statframe, text="",font=25, justify="right", width=8)
actionsC.grid(row=1,column=1)
accuracy=tk.Label(statframe, text="Pontosság:",font=25, justify="left", width=10)
accuracy.grid(row=2, column=0)
accuracyC=tk.Label(statframe, text="",font=25, justify="right", width=8)
accuracyC.grid(row=2,column=1)

keyframe=tk.Frame(root, padx=20, pady=20)
keyframe.grid(row=1, column=0)

tk.Label(root, text=version).grid(row=2, column=0, sticky="sw")

drawkeys()
newsession()
root.bind("<Key>",keypress)
root.mainloop()
