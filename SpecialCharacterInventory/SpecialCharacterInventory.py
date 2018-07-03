import tkinter as tk
import xml.etree.ElementTree as ET


configtree=ET.parse("config.xml")
configroot=configtree.getroot()
maincolor=configroot.find("MainColor").text
originalX=int(configroot.find("OriginalX").text)
originalY=int(configroot.find("OriginalY").text)

expandedX=originalX
expandedY=int(configroot.find("ExpandedY").text)

MAX_COLUMNS=int(configroot.find("MaxColumnsNumber").text)

buttoncolor=configroot.find("DropDownButtonColor").text
hovercolor=configroot.find("DropDownButtonHoverColor").text
buttonbordercolor=configroot.find("ButtonBorderColor").text

SpecChars=[]
ScTextList=[]

tree = ET.parse('SpecialCharactersList.xml')
xmlroot=tree.getroot()

for specchar in xmlroot.findall("SpecialCharacter"):
    SpecChars.append(specchar.text)


def set_text(text):
    global entry
    entry.delete(0,"end")
    entry.insert(0, text)
    print(text)



def togglesize(*args):
    global root, geometry, dropdownButton, ButtonFrame, entry,ScButtonList
    if geometry=="original":
        root.geometry("{}x{}".format(expandedX, expandedY))
        dropdownButton.configure(text="▲")
        SCframe=tk.Frame(root,bg=maincolor)
        SCframe.grid(row=1, column=0)
        sc_row=1
        sc_col=0
        for sc in SpecChars:
            sct=tk.Text(SCframe, height=1,width=2, relief="groove",highlightbackground=maincolor)
            sct.insert(1.5,str(sc))
            sct.grid(row=sc_row, column=sc_col)
            ScTextList.append(sct)
            sc_col += 1
            if (sc_col == MAX_COLUMNS):
                sc_col = 0
                sc_row += 1
        geometry="expanded"
    else:
        root.geometry("{}x{}".format(originalX, originalY))
        dropdownButton.configure(text="▼")
        for text in ScTextList:
            text.grid_forget()
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
root.grid_columnconfigure(0, weight=1)
root.resizable(False,False)
root.mainloop()