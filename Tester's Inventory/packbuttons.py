import tkinter as tk
import pyperclip
import webbrowser
from configmanager import Configmanager

class Gridbuttons():
    def __init__(self):
        pass

    def sortdevices(self,Devices,LeftFrame, RightFrame,LeftStartRow, RightStartRow,ToBeForgottenList,BackGroundcolor,ButtonPressColor,MaxColumns):
        col=0
        for dev in Devices:
            buttonname=str(dev['mfg'])+"\t"+str(dev['id'])
            if dev["type"]=="phone":
                devb=tk.Button(LeftFrame, width=20,text=buttonname,highlightbackground=BackGroundcolor, activebackground=ButtonPressColor,command=lambda value=dev:self.copytoclipboard(value))
                devb.grid(row=LeftStartRow, column=col)
                ToBeForgottenList.append(devb)
                col += 1
                if (col == MaxColumns):
                    col = 0
                    LeftStartRow += 1
            else:
                devb=tk.Button(RightFrame, width=20,text=buttonname,highlightbackground=BackGroundcolor, activebackground=ButtonPressColor,command=lambda value=dev:self.copytoclipboard(value))
                devb.grid(row=RightStartRow, column=col)
                ToBeForgottenList.append(devb)
                col += 1
                if (col == MaxColumns):
                    col = 0
                    RightStartRow += 1

    def sorturls(self, URLs, LeftFrame, RightFrame, LeftStartRow, RightStartRow, ToBeForgottenList, BackGroundcolor, ButtonPressColor, MaxColumns):
        col=0
        for url in URLs:
            buttonname= str(url['name'])
            if url["type"]== "work":
                urlB=tk.Button(LeftFrame, width=20, text=buttonname, highlightbackground=BackGroundcolor, activebackground=ButtonPressColor, command=lambda value=url:self.openinbrowser(value))
                urlB.grid(row=LeftStartRow, column=col)
                ToBeForgottenList.append(urlB)
                col += 1
                if (col == MaxColumns):
                    col = 0
                    LeftStartRow += 1
            else:
                urlB=tk.Button(RightFrame, width=20, text=buttonname, highlightbackground=BackGroundcolor, activebackground=ButtonPressColor, command=lambda value=url:self.openinbrowser(value))
                urlB.grid(row=RightStartRow, column=col)
                ToBeForgottenList.append(urlB)
                col += 1
                if (col == MaxColumns):
                    col = 0
                    RightStartRow += 1


    def copytoclipboard(device):
        copytoclipboard=device['mfg']+" "+device['model']+" "+device['OS']+" v"+device['version']
        pyperclip.copy(copytoclipboard)

    def openinbrowser(url):
        configmanager=Configmanager()
        webbrowser.get(configmanager.getconfigvalue("browserexecutable")).open_new_tab(url['address'])
