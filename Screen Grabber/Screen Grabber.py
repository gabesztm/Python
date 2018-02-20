# Author:          Gábor Tóth-Molnár
# Created:         25 July, 2017
# Last Modified:   20 Feb, 2018

import datetime
import tkinter as tk
from tkinter import filedialog
from os.path import join
from PIL import ImageGrab


version="v1.1  ™.G"

running = False
AllColor="goldenrod2"


def grabberfunc(*args):
    global directory
    savedir=str(directory.get())
    savefile="Screenshot_"+str("{:%Y_%m_%d-%H_%M_%S}".format(datetime.datetime.now()))+".png"
    savedirfile=join(savedir,savefile)
    screenshot=ImageGrab.grab()
    screenshot.save(str(savedirfile))

def dirIn(*args):
    global directory, dirLabel,start
    directory.set(filedialog.askdirectory())
    dirLabel.config(text=directory.get())
    if directory.get()!="":
        start.config(state="normal")


def scanning():
    interval=deftimeInput.get()
    if running:
        grabberfunc()
    root.after(int(interval)*1000, scanning)


def start():
    global running
    running = True
    start.config(state="disabled", bg="gainsboro")
    stop.config(bg="indianred",state="normal")

def stop():
    global running
    running = False
    start.config(state="normal", bg="green3")
    stop.config(bg="gainsboro",state="disabled")

root = tk.Tk()
root.title("Screen Grabber")
root.config(bg=AllColor)
directory=tk.StringVar()
directory.set("")
appFrame=tk.Frame(root, bd=2, relief="groove",bg=AllColor)
appFrame.grid(row=0, column=0,pady=10,padx=10)
browse=tk.Button(appFrame, command=dirIn, text="Output directory", bg="skyblue")
browse.grid(row=0, column=0,padx=5)
dirLabel=tk.Label(appFrame, text=directory.get(),bg=AllColor,width=80)
dirLabel.grid(row=0,column=1,pady=10)
dirLabel.grid_propagate(0)
tk.Label(appFrame,text="Interval [s]: ",bg=AllColor).grid(row=1,column=0)
deftime=tk.StringVar(value="1")
deftimeInput=tk.Entry(appFrame,textvariable=deftime,width=10)
deftimeInput.grid(row=1,column=1)
start = tk.Button(appFrame, text="Start Scan", command=start,state="disabled", bg="gainsboro")
stop = tk.Button(appFrame, text="Stop", command=stop,state="disabled", bg="gainsboro")
start.grid(row=2, column=0)
stop.grid(row=2, column=1, pady=10)
tk.Label(root,text=version,bg=AllColor).grid(row=3,column=0, sticky="SW")
interval=deftimeInput.get()
root.after(int(interval), scanning)
root.mainloop()