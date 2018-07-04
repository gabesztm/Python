import tkinter as tk
import xml.etree.ElementTree as ET
import pyperclip
from os.path import join

version="v1.2 ™.G"

configfile=join("Configuration","config.xml")
configtree=ET.parse(configfile)
configroot=configtree.getroot()
maincolor=configroot.find("MainColor").text
if ("gray" in str(maincolor)) or ("black" in str(maincolor)):
    logocolor="white"
else:
    logocolor="black"

originalX=int(configroot.find("OriginalX").text)
originalY=int(configroot.find("OriginalY").text)

expandedX=originalX
expandedY=int(configroot.find("ExpandedY").text)

MAX_COLUMNS=int(configroot.find("MaxColumnsNumber").text)

buttoncolor=configroot.find("DropDownButtonColor").text
hovercolor=configroot.find("DropDownButtonHoverColor").text
buttonbordercolor=configroot.find("ButtonBorderColor").text
scbuttonpresscolor=configroot.find("SpecCharButtonPressColor").text

SpecChars=[]
ScButtonList=[]
characterlistfile=join("Configuration","SpecialCharactersList.xml")
tree = ET.parse(characterlistfile)
xmlroot=tree.getroot()

for specchar in xmlroot.findall("SpecialCharacter"):
    SpecChars.append(specchar.text)


def copytoclipboard(character):
    pyperclip.copy(character)


def togglesize(*args):
    global root, geometry, dropdownButton, ButtonFrame,ScButtonList
    if geometry=="original":
        root.geometry("{}x{}".format(expandedX, expandedY))
        dropdownButton.configure(text="▲")
        SCframe=tk.Frame(root,bg=maincolor)
        SCframe.grid(row=1, column=0)
        sc_row=1
        sc_col=0
        for sc in SpecChars:
            scb=tk.Button(SCframe, width=1,text=str(sc),highlightbackground=maincolor, activebackground=scbuttonpresscolor,command=lambda value=sc:copytoclipboard(str(value)))
            scb.grid(row=sc_row, column=sc_col)
            ScButtonList.append(scb)
            sc_col += 1
            if (sc_col == MAX_COLUMNS):
                sc_col = 0
                sc_row += 1
        geometry="expanded"
    else:
        root.geometry("{}x{}".format(originalX, originalY))
        dropdownButton.configure(text="▼")
        for button in ScButtonList:
            button.grid_forget()
        geometry = "original"




root=tk.Tk()
root.title("Common special characters")
root.geometry("{}x{}".format(originalX,originalY))
geometry="original"
root.configure(bg=maincolor)
ButtonFrame=tk.Frame(root,bg=maincolor)
ButtonFrame.grid(row=0, column=0)
dropdownButton=tk.Button(ButtonFrame, width=20, text="▼",command=togglesize,highlightbackground=buttonbordercolor,bg=buttoncolor,activebackground=hovercolor, anchor="center")
dropdownButton.grid(row=0, column=0, pady=5)
vl=tk.Label(root,text=version, bg=maincolor,fg=logocolor)
vl.grid(row=0,column=1)
root.grid_columnconfigure(0, weight=1)
root.resizable(False,False)
root.mainloop()