import tkinter as tk
from animation import Animation
from packbuttons import Gridbuttons
from configmanager import Configmanager

version="v2 ™.G"

anim=Animation()
configmanager=Configmanager()

maincolor=configmanager.getconfigvalue("MainColor")
if ("gray" in str(maincolor)) or ("black" in str(maincolor)):
    logocolor="white"
else:
    logocolor="black"
originalX=int(configmanager.getconfigvalue("OriginalX"))
originalY=int(configmanager.getconfigvalue("OriginalY"))
expandedX=int(configmanager.getconfigvalue("ExpandedX"))
expandedY=int(configmanager.getconfigvalue("ExpandedY"))
MAX_COLUMNS=int(configmanager.getconfigvalue("MaxColumnsNumber"))
buttoncolor=configmanager.getconfigvalue("DropDownButtonColor")
hovercolor=configmanager.getconfigvalue("DropDownButtonHoverColor")
buttonbordercolor=configmanager.getconfigvalue("ButtonBorderColor")
scbuttonpresscolor=configmanager.getconfigvalue("SpecCharButtonPressColor")
URLbuttonList=[]
DevButtonList=[]
Devices=[]
URLs=[]

configmanager.getdevices(Devices)
configmanager.geturls(URLs)


def Htogglesize(*args):
    global root, geometry, VtoggleB, ButtonFrame,DevButtonList, vl
    vl.grid_forget()
    if geometry=="expanded":
        IncAnim=Animation()
        IncAnim.resize(root,expandedX,expandedY,20,20)
        VtoggleB.configure(text="◂")
        devframe=tk.Frame(root, bg=maincolor)
        devframe.grid(row=1, column=1)
        DevButtonList.append(devframe)
        Phoneframe=tk.Frame(devframe, bg=maincolor)
        Tabletframe=tk.Frame(devframe, bg=maincolor)
        Phoneframe.grid(row=0, column=3)
        Tabletframe.grid(row=0, column=4)
        phL=tk.Label(Phoneframe, text="Phones", bg=maincolor, fg=logocolor)
        phL.grid(row=0,column=0,  pady=0)
        tL=tk.Label(Tabletframe, text="Tablets", bg=maincolor, fg=logocolor)
        tL.grid(row=0,column=0, pady=0)
        DevButtonList.append(phL)
        DevButtonList.append(tL)
        phonerow=1
        tabletrow=1
        gridObj=Gridbuttons
        gridObj.sortdevices(gridObj,Devices,Phoneframe,Tabletframe,phonerow, tabletrow,DevButtonList, maincolor, scbuttonpresscolor,MAX_COLUMNS)
        vl.grid(row=0, column=2)
        geometry="Right-expanded"
    else:
        DecAnim=Animation()
        DecAnim.resize(root,originalX,expandedY,20,20)
        VtoggleB.configure(text="▸")
        for button in DevButtonList:
            button.grid_forget()
        vl.grid(row=0,column=1)
        geometry = "expanded"


def Vtogglesize(*args):
    global root, geometry, dropdownButton, ButtonFrame,URLbuttonList, VtoggleB
    if geometry=="original":
        IncAnim=Animation()
        IncAnim.resize(root,originalX,expandedY,20,20)
        dropdownButton.configure(text="▲")
        urlframe=tk.Frame(root, bg=maincolor)
        urlframe.grid(row=1, column=0)
        WorkFrame=tk.Frame(urlframe, bg=maincolor)
        PrivateFrame=tk.Frame(urlframe, bg=maincolor)
        WorkFrame.grid(row=0, column=0, sticky="W")
        PrivateFrame.grid(row=0, column=1, sticky="W")
        AdditionalRightFrame=tk.Frame(urlframe, bg=maincolor)
        AdditionalRightFrame.grid(row=0,column=2,padx=20, sticky="W")
        wL=tk.Label(WorkFrame, text="Work", bg=maincolor, fg=logocolor)
        wL.grid(row=0, column=0, pady=0)
        privL=tk.Label(PrivateFrame, text="Private", bg=maincolor, fg=logocolor)
        privL.grid(row=0, column=0, pady=0)
        URLbuttonList.append(wL)
        URLbuttonList.append(privL)
        workrow=1
        privaterow=1
        gridObj=Gridbuttons
        gridObj.sorturls(gridObj, URLs, WorkFrame, PrivateFrame, workrow, privaterow, URLbuttonList, maincolor, scbuttonpresscolor, MAX_COLUMNS)
        VtoggleB=tk.Button(AdditionalRightFrame, text="▸",highlightbackground=buttonbordercolor, bg=buttoncolor, activebackground=hovercolor,command=Htogglesize)
        VtoggleB.grid(row=0, column=0,ipady=20)
        URLbuttonList.append(VtoggleB)

        geometry="expanded"
    else:
        DecAnim=Animation()
        DecAnim.resize(root,originalX,originalY,20,20)
        dropdownButton.configure(text="▼")
        for button in URLbuttonList:
            button.grid_forget()
        for button in DevButtonList:
            button.grid_forget()
        geometry = "original"




root=tk.Tk()
root.title(configmanager.getconfigvalue("user")+"'s Inventory")
root.geometry("{}x{}".format(originalX,originalY))
geometry="original"
root.configure(bg=maincolor)
ButtonFrame=tk.Frame(root,bg=maincolor)
ButtonFrame.grid(row=0, column=0)
dropdownButton=tk.Button(ButtonFrame, width=20, text="▼", command=Vtogglesize, highlightbackground=buttonbordercolor, bg=buttoncolor, activebackground=hovercolor, anchor="center")
dropdownButton.grid(row=0, column=0, pady=5)
vl=tk.Label(root,text=version, bg=maincolor,fg=logocolor)
vl.grid(row=0,column=1)
root.grid_columnconfigure(0, weight=1)
root.resizable(False,False)
root.mainloop()
