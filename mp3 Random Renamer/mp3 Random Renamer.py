# Author:   Gábor Tóth-Molnár

import tkinter as tk
from tkinter import filedialog
import os
import getpass
import time
from shutil import copyfile
from random import randint




def ClosePopUp(*args):
    popupinfo.destroy()


def CloseRoot(*args):
    time.sleep(0.05)
    root.destroy()


def dirIn(*args):
    global directory
    global path
    global directoryOut
    if (directory!=defaulttext):
        directory=filedialog.askdirectory()
        path.grid_forget()
        path=tk.Label(root, text=directory, bg="yellowgreen")
        path.grid(row=0, column=2)
    else:
        directory=filedialog.askdirectory()
        curDir.grid_forget()
        path=tk.Label(root, text=directory, bg="yellowgreen")
        path.grid(row=0, column=2)
    if (directory==defaulttext or directoryOut==defaulttext2):
        start.config(state="disabled")
    else:
        start.config(state="normal",bg="OliveDrab1")

def dirOut(*args):
    global directoryOut
    global path
    global directory
    if (directoryOut!=defaulttext2):
        directoryOut=filedialog.askdirectory()
        path.grid_forget()
        path=tk.Label(root, text=directoryOut, bg="yellowgreen")
        path.grid(row=1, column=2)
    else:
        directoryOut=filedialog.askdirectory()
        destDir.grid_forget()
        path=tk.Label(root, text=directoryOut, bg="yellowgreen")
        path.grid(row=1, column=2)
    if (directory==defaulttext or directoryOut==defaulttext2):
        start.config(state="disabled")
    else:
        start.config(state="normal",bg="OliveDrab1")

def rangenerator():
	string=""
	for i in range(1,30):
		kN=randint(1,2)
		if kN==1:
			str= randint(65,90)
		else:
			str= randint(97,122)
		string+=chr(str)
	return string

def copyfunc(route,routeOut):
    totalamount=0
    for filename in os.listdir(route):
        if (filename.endswith(".mp3") or filename.endswith(".MP3")):
            ranfilename=rangenerator()
            CurrentSourceFile=os.path.join(route,filename)
            tempname=str(ranfilename)+"_"+filename
            CurrentDestFile=os.path.join(routeOut,tempname)
            copyfile(CurrentSourceFile,CurrentDestFile)
            totalamount+=1
            print("Copying "+filename+"\n")
            time.sleep(0.2)



    global popupinfo
    popupinfo=tk.Toplevel()
    popupinfo.geometry('{}x{}'.format(370,50))
    popupinfo.title("Information")
    popupinfo.configure(background="goldenrod")
    if totalamount>0:
        infoMSG=str(totalamount)+" file(s) copied"
    else:
        infoMSG="No files copied"
    tk.Label(popupinfo, text=infoMSG, bg="goldenrod").pack()
    tk.Button(popupinfo, text=" Got it ",command=ClosePopUp, bg="skyblue").pack()




root=tk.Tk()
global felirat
global curDelFile
root.geometry('{}x{}'.format(550,150))
root.configure(background="yellowgreen")
root.title("Music Rename   ™.G")
datas= ('kangaroo.ico', '.')
browse=tk.Button(root, command=dirIn, text="Browse Input folder", bg="skyblue")
Destbrowse=tk.Button(root, command=dirOut, text="Browse Output folder", bg="skyblue")
defaulttext="Choose directory"
defaulttext2="Choose directory"
global directory
global directoryOut
directory=defaulttext
directoryOut=defaulttext2
curDir=tk.Label(root, text=directory, bg="yellowgreen")
curDir.grid(row=0,column=2)
destDir=tk.Label(root, text=directoryOut, bg="yellowgreen")
destDir.grid(row=1,column=2)
start=tk.Button(root, command=lambda: copyfunc(directory,directoryOut),text="Copy files", bg="Grey", state="disabled")
dirLabel=tk.Label(root, text="Directory: ", bg="yellowgreen")
dirLabelOut=tk.Label(root, text="Directory: ", bg="yellowgreen")
quitgomb=tk.Button(root, command=CloseRoot, text="Quit",bg="skyblue")

browse.grid(row=0, column=0,padx=10, pady=10)
Destbrowse.grid(row=1, column=0)
tk.Label(root,text="", bg="yellowgreen").grid(row=2,column=0)
start.grid(row=3, column=0,rowspan=5)
quitgomb.grid(row=3, column=2)
dirLabel.grid(row=0, column=1)
dirLabelOut.grid(row=1, column=1)
root.mainloop()
