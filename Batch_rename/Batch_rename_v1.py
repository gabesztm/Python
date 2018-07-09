import tkinter as tk
from tkinter import filedialog, messagebox
import ntpath
from utilities import *
from os import rename
from os.path import join
import xml.etree.ElementTree as ET

version="v1 ™.G"

configfile=join("Configuration","config.xml")
configtree=ET.parse(configfile)
configroot=configtree.getroot()

originalX=int(configroot.find("OriginalX").text)
originalY=int(configroot.find("OriginalY").text)
maincolor=configroot.find("MainColor").text
textcolor=configroot.find("TextColor").text
ButtonBorderColor=configroot.find("ButtonBorderColor").text
ButtonPressColor=configroot.find("ButtonPressColor").text

def scrolltables(direction):
    global InList, OutList
    for table in (InList, OutList):
        table.yview




def preview(*args):
    global files, OutList, sB, ModifyBeginning, newname
    OutList.delete(0, "end")
    thismuch=sB.get()
    newname=[]
    for f in files:
        if ModifyBeginning.get()==True:
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








def openfiles(*args):
    global InList, files, sB, doB
    InList.delete(0,"end")
    files=filedialog.askopenfilenames()
    longest=[]
    if len(files)==0:
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

ModifyBeginning=tk.BooleanVar()
ModifyBeginning.set(True)

files=[]
newname=[]
spinboxMax=0

ButtonFrame=tk.Frame(root,bg=maincolor)
ListFrame=tk.Frame(root,bg=maincolor)
SetupFrame=tk.Frame(root,bg=maincolor)
ButtonFrame.grid(row=0, column=0)
ListFrame.grid(row=1, column=0)
SetupFrame.grid(row=2, column=0,pady=10)

browseB=tk.Button(ButtonFrame, text="Open files",highlightbackground=ButtonBorderColor,activebackground=ButtonPressColor, command=openfiles)
browseB.grid(row=0, column=0, padx=200, pady=10)
doB=tk.Button(ButtonFrame, text="Start",highlightbackground=ButtonBorderColor,activebackground=ButtonPressColor, command=RenameFunc, state="disabled")
doB.grid(row=0, column=1,padx=200)

scrollbarY = tk.Scrollbar(ListFrame, orient='vertical')
scrollbarY.grid(row=1, column=2,sticky="NS")

tk.Label(ListFrame, text="Before                                                                      After",bg=maincolor,fg=textcolor).grid(row=0,column=0,columnspan=2)
InList = tk.Listbox(ListFrame, highlightbackground=maincolor,yscrollcommand=scrollbarY.set, width=55,selectmode="multiple")
OutList = tk.Listbox(ListFrame,highlightbackground=maincolor, yscrollcommand=scrollbarY.set, width=55,selectmode="multiple")
scrollbarY.config(command=scrolltables)
InList.grid(row=1, column=0)
OutList.grid(row=1, column=1)

tk.Label(SetupFrame, text="Position & amount of characters to be removed",bg=maincolor,fg=textcolor).grid(row=0,column=0, columnspan=2,pady=10)
modButtonB=tk.Radiobutton(SetupFrame,highlightbackground=maincolor,bg=maincolor,fg=textcolor, text="Beginning", variable=ModifyBeginning, value=True, command=preview)
modButtonE=tk.Radiobutton(SetupFrame,highlightbackground=maincolor,bg=maincolor,fg=textcolor,text="End          ", variable=ModifyBeginning, value=False,command=preview)
modButtonB.grid(row=1,column=0)
modButtonE.grid(row=2, column=0)

sB=tk.Spinbox(SetupFrame,highlightbackground=maincolor, width=5,from_=0,to_=0,command=preview)
sB.grid(row=1, column=1,padx=45)

tk.Label(root, text=version,bg=maincolor,fg=textcolor).grid(row=3, column=0,sticky="SW")
root.mainloop()