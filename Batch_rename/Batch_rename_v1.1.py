"Batch rename script can load multiple files from a directory and adds or removes specified amount of characters to/from the beginning/end of the filename"

import tkinter as tk
from tkinter import filedialog, messagebox
import ntpath
from utilities import *
from os import rename
from os.path import join
import xml.etree.ElementTree as ET
from random import randint

version="v1.1 ™.G"

configfile=join("Configuration","config.xml")
configtree=ET.parse(configfile)
configroot=configtree.getroot()

originalX=int(configroot.find("OriginalX").text)
originalY=int(configroot.find("OriginalY").text)
maincolor=configroot.find("MainColor").text
textcolor=configroot.find("TextColor").text
ButtonBorderColor=configroot.find("ButtonBorderColor").text
ButtonPressColor=configroot.find("ButtonPressColor").text


def togglemode(*args):
    global RemoveFrame, AppendFrame, RemButtonB, RemButtonE, sB, IndexB, RandomB, StringB, RandomSB, SameStrEn
    remframe=[RemButtonE,RemButtonB,sB]
    appendframe=[IndexB,RandomB, StringB, RandomSB, SameStrEn]
    if str(Mode.get())=="Remove":
        for widget in remframe:
            widget.config(state="normal")
        for widget in appendframe:
            widget.config(state="disabled")
        RemoveFrame.config(bd=2)
        AppendFrame.config(bd=0)
    else:
        for widget in remframe:
            widget.config(state="disabled")
        for widget in appendframe:
            widget.config(state="normal")
        RemoveFrame.config(bd=0)
        AppendFrame.config(bd=2)



def scrolltables(direction):
    global InList, OutList
    for table in (InList, OutList):
        table.yview




def preview(*args):
    global files,newname, Mode, OutList, sB, RemoveBeginning, AppendHow, RandomSB, SameStrEn
    OutList.delete(0, "end")
    thismuch=sB.get()
    newname=[]
    runningindex=1
    randomnumbers=int(RandomSB.get())
    samestr=str(SameStrEn.get())
    for f in files:
        if str(Mode.get())=="Remove":
            if RemoveBeginning.get()==True:
                name=str(ntpath.basename(f))[int(thismuch):]
                OutList.insert("end",name)
                newname.append(name)
            else:
                if int(thismuch)==0:
                    name=str(ntpath.basename(f)[int(thismuch):])
                    OutList.insert("end", name )
                    newname.append(name)
                else:
                    name=str(ntpath.basename(f))[:-int(thismuch)]
                    OutList.insert("end", name)
                    newname.append(name)
        else:
            if str(AppendHow.get())=="Index":
                AmountOfFiles=len(files)
                LeadingZeros=len(str(AmountOfFiles))
                name=str(runningindex).zfill(LeadingZeros)+"_"+str(ntpath.basename(f))
                OutList.insert("end", name)
                newname.append(name)
                runningindex+=1
            elif str(AppendHow.get())=="Random":
                randomstring=""
                for i in range(0, randomnumbers):
                    UpperLower=randint(1,2)
                    if UpperLower==1:
                        char=randint(65,90)
                    else:
                        char=randint(97, 122)
                    randomstring+=chr(char)
                name=randomstring+"_"+str(ntpath.basename(f))
                OutList.insert("end",name)
                newname.append(name)
            else:
                name=samestr+"_"+str(ntpath.basename(f))
                OutList.insert("end",name)
                newname.append(name)









def openfiles(*args):
    global InList, files, sB, doB, OutList
    InList.delete(0,"end")
    files=filedialog.askopenfilenames()
    longest=[]
    if len(files)==0:
        OutList.delete(0,"end")
        messagebox.showwarning("","No files specified!")
    else:
        for f in files:
            InList.insert("end",ntpath.basename(f))
            longest.append(len(ntpath.basename(f)))
        sB.config(to_=Statistics.Minimum(longest))
        preview()
        doB.config(state="normal")

def RenameFunc(*args):
    global files, newname, InList, OutList, doB
    directory=ntpath.dirname(files[0])
    for n in range(0,len(newname)):
        new=join(directory, newname[n])
        rename(files[n],new)
    InList.delete(0,"end")
    OutList.delete(0, "end")
    doB.config(state="disabled")
    messagebox.showinfo("","Files are renamed")



root=tk.Tk()
root.title("Batch rename")
root.geometry("{}x{}".format(originalX,originalY))
root.configure(bg=maincolor)

files=[]
newname=[]


ButtonFrame=tk.Frame(root,bg=maincolor)
ListFrame=tk.Frame(root,bg=maincolor)
ModeSelectFrame=tk.Frame(root, bg=maincolor,bd=2, relief="groove")
ModesFrame=tk.Frame(root, bg=maincolor)
RemoveFrame=tk.Frame(ModesFrame,bg=maincolor,bd=2, relief="sunken")
AppendFrame=tk.Frame(ModesFrame, bg=maincolor,bd=0, relief="sunken")
ButtonFrame.grid(row=0, column=0)
ListFrame.grid(row=1, column=0)
ModeSelectFrame.grid(row=2, column=0, pady=10)
ModesFrame.grid(row=3, column=0, padx=20)
RemoveFrame.grid(row=0, column=0, padx=10)
AppendFrame.grid(row=0, column=1, padx=10)

# ----------------------ButtonFrame
browseB=tk.Button(ButtonFrame, text="Open files",highlightbackground=ButtonBorderColor,activebackground=ButtonPressColor, command=openfiles)
browseB.grid(row=0, column=0, padx=200, pady=10)
doB=tk.Button(ButtonFrame, text="Start",highlightbackground=ButtonBorderColor,activebackground=ButtonPressColor, command=RenameFunc, state="disabled")
doB.grid(row=0, column=1,padx=200)

# ----------------------ListFrame
scrollbarY = tk.Scrollbar(ListFrame, orient='vertical')
scrollbarY.grid(row=1, column=2,sticky="NS")
tk.Label(ListFrame, text="Before                                                                      After",bg=maincolor,fg=textcolor).grid(row=0,column=0,columnspan=2)
InList = tk.Listbox(ListFrame, highlightbackground=maincolor,yscrollcommand=scrollbarY.set, width=55,selectmode="multiple")
OutList = tk.Listbox(ListFrame,highlightbackground=maincolor, yscrollcommand=scrollbarY.set, width=55,selectmode="multiple")
scrollbarY.config(command=scrolltables)
InList.grid(row=1, column=0)
OutList.grid(row=1, column=1)

# ----------------------ModeSelectFrame
Mode=tk.StringVar()
Mode.set("Remove")
tk.Label(ModeSelectFrame, text="Select mode", bg=maincolor, fg=textcolor).grid(row=0, column=0)
ModeBRem=tk.Radiobutton(ModeSelectFrame,highlightbackground=maincolor,bg=maincolor,fg=textcolor, text="Remove characters", variable=Mode, value="Remove", command=togglemode)
ModeBApp=tk.Radiobutton(ModeSelectFrame,highlightbackground=maincolor,bg=maincolor,fg=textcolor, text="Append characters ", variable=Mode, value="Append", command=togglemode)
ModeBRem.grid(row=1,column=0)
ModeBApp.grid(row=2,column=0)

# ----------------------RemoveFrame
spinboxMax=0
RemoveBeginning=tk.BooleanVar()
RemoveBeginning.set(True)
tk.Label(RemoveFrame, text="Position & amount of characters to be removed",bg=maincolor,fg=textcolor).grid(row=0,column=0, columnspan=2,pady=10)
RemButtonB=tk.Radiobutton(RemoveFrame,highlightbackground=maincolor,bg=maincolor,fg=textcolor, text="Beginning", variable=RemoveBeginning, value=True, command=preview, state="normal")
RemButtonE=tk.Radiobutton(RemoveFrame,highlightbackground=maincolor,bg=maincolor,fg=textcolor,text="End          ", variable=RemoveBeginning, value=False,command=preview, state="normal")
RemButtonB.grid(row=1,column=0)
RemButtonE.grid(row=2, column=0)
sB=tk.Spinbox(RemoveFrame,highlightbackground=maincolor, width=5,from_=0,to_=0,command=preview, state="normal")
sB.grid(row=1, column=1, pady=5)

# ----------------------AppendFrame
AppendHow=tk.StringVar()
AppendHow.set("Index")
samestring=tk.StringVar()
samestring.set("")
randomlength=tk.IntVar()
randomlength.set(0)
tk.Label(AppendFrame, text="What to append to the beginning",bg=maincolor,fg=textcolor).grid(row=0,column=0, columnspan=2,pady=10)
IndexB=tk.Radiobutton(AppendFrame,highlightbackground=maincolor,bg=maincolor,fg=textcolor, text="Index    ", variable=AppendHow, value="Index", command=preview, state="disabled")
RandomB=tk.Radiobutton(AppendFrame,highlightbackground=maincolor,bg=maincolor,fg=textcolor, text="Random", variable=AppendHow, value="Random", command=preview, state="disabled")
StringB=tk.Radiobutton(AppendFrame,highlightbackground=maincolor,bg=maincolor,fg=textcolor, text="String    ", variable=AppendHow, value="String", command=preview, state="disabled")
RandomSB=tk.Spinbox(AppendFrame,highlightbackground=maincolor, width=3,from_=1,to_=100,command=preview, state="disabled")
SameStrEn=tk.Entry(AppendFrame, textvariable=samestring, width=10, state="disabled")
SameStrEn.bind("<KeyPress>",preview)
IndexB.grid(row=1, column=0)
RandomB.grid(row=2, column=0)
RandomSB.grid(row=2, column=1)
StringB.grid(row=3, column=0)
SameStrEn.grid(row=3, column=1, pady=5)



tk.Label(root, text=version,bg=maincolor,fg=textcolor).grid(row=0, column=0,sticky="NW")
root.mainloop()