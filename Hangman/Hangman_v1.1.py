#Author:	Gábor Tóth-Molnár

import tkinter as tk
from random import randint
from tkinter import messagebox

version="v1.1"
szoFile=open("szolista.txt",'r',encoding='utf-8')
wordFile=open("words.txt",'r',encoding='utf-8')
countHu=4026
countEn=2000

akasztofa="Akasztófa   ™.G"
hangman="Hangman   ™.G"
rootlabtextHu="Karakterek száma"
rootlabtextEn="Number of characters"

def keypress(event):
    global lang
    if event.char not in ("a","á","b","c","d","e","é","f","g","h","i","í","j","k","l","m","n","o","ó","ö","ő","p","q","r","s","t","u","ú","ü","ű","v","w","x","y","z","-"):
        if event.keycode not in (8,22,23,36):                                               #backspace és Tab keycode-ja. Ha kijívatja a rossz szöveget, akkor nem dob hibát
            if lang.get()==0:
                messagebox.showinfo("Hahó!", "Hibás karaktert írtál!")
            else:
                messagebox.showinfo("Hey!", "Wrong character!")


def updateroot(*args):
    global lang,root,rootLab
    if lang.get()==1:
        root.title(hangman)
        rootLab.configure(text=rootlabtextEn)
    else:
        root.title(akasztofa)
        rootLab.configure(text=rootlabtextHu)

def checkword( word, canvas,guess):
    global currentstatus, labeltext, gameL, labeltextReal, wronggues,guessB, guessE, wrongtext,wrongL,gamewindow
    wordLi=list(str(word))
    position=[]
    for i in range(0,len(wordLi)):
        if wordLi[i]==guess.upper():
            position.append(i)
    if position==[]:
        wrongtext.append(str(guess))
        if wronggues==0:
            canvas.create_line(120, 200, 120, 50, fill="red", width=2)
            wronggues+=1
        elif wronggues==1:
            canvas.create_line(120, 50, 190, 50, fill="red", width=2)
            wronggues+=1
        elif wronggues==2:
            canvas.create_line(120, 80, 150, 50, fill="red", width=2)
            wronggues+=1
        elif wronggues == 3:
            canvas.create_line(190, 50, 190, 80, fill="red", width=2)
            wronggues += 1
        elif wronggues == 4:
            canvas.create_oval(175, 80, 205, 100, fill="red", width=2)
            wronggues += 1
        elif wronggues == 5:
            canvas.create_line(190, 100, 190, 150, fill="red", width=2)
            wronggues += 1
        elif wronggues == 6:
            canvas.create_line(190, 120, 182, 150, fill="red", width=2)
            wronggues += 1
        elif wronggues == 7:
            canvas.create_line(190, 120, 197, 150, fill="red", width=2)
            wronggues += 1
        elif wronggues == 8:
            canvas.create_line(190, 150, 197, 180, fill="red", width=2)
            wronggues += 1
        elif wronggues == 9:
            canvas.create_line(190, 150, 182, 180, fill="red", width=2)
            wronggues += 1
            if lang.get()==0:
                messagebox.showinfo("","Vesztettél!\n"+str(word)+" volt a megoldás")
            else:
                messagebox.showinfo("","You've lost!\nSolution was: "+str(word))
            guessB.configure(state="disabled")
            gamewindow.destroy()


    for j in range(0,len(currentstatus)):
        if j in position:
            if currentstatus[j*2]=="_":
                currentstatus[j*2]=guess
    labeltext=currentstatus
    check=""
    for f in word:
        check+=f
        check+=" "
    labeltextReal=""
    for d in range(0, len(labeltext)):
        labeltextReal+=str(labeltext[d])
    try:
        gameL.config(text=labeltextReal)
        wrongL.config(text=wrongtext)
    except Exception:
        ()
    if labeltext==list(check):
        if lang.get()==0:
            messagebox.showinfo("","Gratulálok!")
        else:
            messagebox.showinfo("", "Congratulations!")
        guessB.configure(state="disabled")
        gamewindow.destroy()
    try:
        guessE.delete(0, "end")
    except Exception:
        ()


def newgame(charNr):
    global lang,szoFile,wordFile, countHu,countEn, currentstatus, labeltext, gameL, labeltextReal, wronggues,guessE,wrongtext, wrongL,gamewindow
    buttontext = ""
    wronggues=0
    currentstatus = list()
    labeltextReal=""
    wrongtext=[]
    for h in range(0,charNr):
        labeltextReal+="_"
        labeltextReal += " "
    for ch in range(0,charNr):
        currentstatus+="_ "
    if lang.get()==0:
        until=randint(0,8000)
        wordcounts=0
        linecounts=0
        Maxlines=countHu
        szoFile.seek(0)
        item=szoFile.readline().splitlines()[0]
        while item:
            linecounts+=1
            if linecounts==Maxlines-10:
                szoFile.seek(0)
                linecounts=0
            if len(item)==charNr:
                wordcounts+=1
            if wordcounts==until:
                #print(item.upper())
                break
            item=szoFile.readline().splitlines()[0]
    if lang.get()==1:
        until=randint(0,8000)
        wordcounts=0
        linecounts=0
        Maxlines=countEn
        wordFile.seek(0)
        item=wordFile.readline().splitlines()[0]
        while item:
            linecounts+=1
            if linecounts==Maxlines-10:
                wordFile.seek(0)
                linecounts=0
            if len(item)==charNr:
                wordcounts+=1
            if wordcounts==until:
                print(item.upper())
                break
            item=wordFile.readline().splitlines()[0]
    target = item.upper()
    gamewindow=tk.Toplevel()
    if lang.get()==0:
        buttontext="Tipp"
    else:
        buttontext="Guess"
    gamewindow.geometry('{}x{}'.format(500, 530))
    global guessB
    guess=tk.StringVar()
    guessFR=tk.Frame(gamewindow, bd=1,relief="solid")
    guessFR.pack(pady=20)
    help=""
    if lang.get()==0:
        help="Írd ide a betűt, majd kattints a gombra vagy nyomd meg ez Enter-t!"
    else:
        help="Type the letter here, then click the button below or press Return key."
    tk.Label(guessFR,text=help).pack()
    guessE=tk.Entry(guessFR,textvariable=guess,width=2, font="Helvetica 35")
    guessE.pack(ipady=10)
    guessB=tk.Button(guessFR,text=buttontext,command=lambda: checkword(target,can, guessE.get().upper()), width=5 )
    guessB.pack(anchor="s",fill="y")
    drawFR=tk.Frame(gamewindow,bd=2,relief="groove")
    drawFR.pack()
    gameL=tk.Label(drawFR, text=labeltextReal, font=("Helvetica", 16))
    gameL.pack()
    can=tk.Canvas(drawFR,bg="lightgreen")
    can.pack()
    wrongL=tk.Label(gamewindow, text=wrongtext,font=("Helvetica", 16))
    wrongL.pack()
    guessE.bind("<KeyPress>",keypress)
    guessE.bind("<Return>",lambda x: checkword(target,can, guessE.get().upper()))
    vL = tk.Label(gamewindow, text=version)
    vL.pack(ipady=50, anchor="sw")






root=tk.Tk()
lang=tk.IntVar()
lang.set(0) #hungarian
root.title(akasztofa)
root.geometry('{}x{}'.format(360, 210))
langFrame=tk.Frame(root,height=2, bd=1, relief="sunken")
langFrame.pack(pady=20)
langB1=tk.Radiobutton(langFrame, text="Magyar", variable=lang, value=0, command=updateroot)
langB1.pack()
langB2=tk.Radiobutton(langFrame, text="English", variable=lang, value=1, command=updateroot)
langB2.pack()
rootLab=tk.Label(root,text=rootlabtextHu)
rootLab.pack()
charButtF=tk.Frame(root, height=3, bd=1,relief="solid")
charButtF.pack()
b0=tk.Button(charButtF, text="3", command=lambda: newgame(3), width=3)
b1=tk.Button(charButtF, text="4", command=lambda: newgame(4), width=3)
b2=tk.Button(charButtF, text="5", command=lambda: newgame(5), width=3)
b3=tk.Button(charButtF, text="6", command=lambda: newgame(6), width=3)
b4=tk.Button(charButtF, text="7", command=lambda: newgame(7), width=3)
b5=tk.Button(charButtF, text="8", command=lambda: newgame(8), width=3)
b6=tk.Button(charButtF, text="9", command=lambda: newgame(9), width=3)
b7=tk.Button(charButtF, text="10", command=lambda: newgame(10), width=3)
b8=tk.Button(charButtF, text="11", command=lambda: newgame(11), width=3)
b9=tk.Button(charButtF, text="12", command=lambda: newgame(12), width=3)
b10=tk.Button(charButtF, text="13", command=lambda: newgame(13), width=3)


MODES=[(3,b0),(4,b1),(5,b2),(6,b3),(7,b4),(8,b5),(9,b6),(10,b7),(11,b8),(12,b9),(13,b10)]
row=1
col=0
for i,b in MODES:
    if (i-3)%4==0:
        row+=1
        col=0
    b.grid(row=row - 1, column=col)
    col+=1

vL=tk.Label(root, text=version)
vL.pack(ipady=50,anchor="sw")
root.mainloop()