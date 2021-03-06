import tkinter as tk
from tkinter import filedialog, messagebox
import csv
from os.path import getsize





version="v2.1  ™.G"

inCSVs=[]
commonheader=""

def dirIn(*args):
    global  directory, lista,expB,exportdata, inCSVs, commonheader
    inCSVs=filedialog.askopenfilenames()
    expB.config(state="disabled")
    lista.delete(0, "end")
    if len(inCSVs):
        totalsize=0
        for file in inCSVs:
            if file.endswith(".csv") or file.endswith(".CSV") and ("tweaked" not in file):
                expB.config(state="normal")
                curFile=open(file, "r",encoding="UTF-8")
                curFile.seek(0)
                commonheader= curFile.readline()
                lista.insert("end", commonheader[:5780])    #maximum length of string that an item can contain
                curFile.close()
                totalsize+=getsize(file)
    if int(totalsize)>20000000:
        messagebox.showinfo("","This will be long.\nGo out & have a coffee.")





def exportFunction(*args):
    global delimiter,exportdata,expB, removeThese, inCSVs, commonheader, inPdelimiter
    removeHeaders=[x.strip() for x in removeThese.get().split(";")]
    commonheaderlist=[x.strip() for x in commonheader.split(inPdelimiter.get())]
    removeIndices=[]
    for removable in removeHeaders:
            if removable == "":
                break
            index=0
            for column in commonheaderlist:
                if str(removable) in str(column):
                    removeIndices.append(index)
                index+=1

    for files in inCSVs:
        if ("snipped" not in files):
            splittedfilename=[x.strip() for x in str(files).split(".csv") ]
            outfilename=str(splittedfilename[0])+"_tweaked.csv"
            inF=open(files,"r", encoding="UTF-8")
            # reader=csv.reader(inF, delimiter=inPdelimiter.get())      #'file.readline()' doesn't work for some unknown reason, it misses lines.
            try:
                outF=open(outfilename, "w",encoding="UTF-8")
            except:
                messagebox.showerror("Oops!", "Couldn't create output file. Maybe the same directory has write protection")
                break
            linecounter=1
            WriteThisToFile=""
            lines=inF.readlines()
            for line in lines:
                snippedtobeList=[x.strip() for x in line.split(inPdelimiter.get())]
                linetowrite=""
                ind = 0
                for column in commonheaderlist:
                    if IsRemove.get():
                        if ind not in removeIndices:
                            if(2<len(snippedtobeList)):
                                linetowrite+=str(snippedtobeList[ind]+str(inPdelimiter.get()))
                    else:
                        if ind in removeIndices:
                            if (2 < len(snippedtobeList)):
                                linetowrite += str(snippedtobeList[ind] + str(inPdelimiter.get()))
                    ind+=1
                linetowrite+="\n"
                WriteThisToFile+=linetowrite
                # outF.write(linetowrite+"\n")
                linecounter+=1
            outF.write(WriteThisToFile)
            inF.close()
            outF.close()
    messagebox.showinfo("Info","Snipped files are exported to the same directory where the input ones are.")

def helpfunc(*args):
    messagebox.showinfo("Help","I.\tOpen CSV files with headers from which you'd like to \n\tdiscard/keep columns with specific or repetitively occurring\n\theaders.\n\tYou can select multiple files.\n\nII.\tIf you have a header like\n\t\theader_A_1, header_B_1, header_A_2, header_B_2\n\tand you type  _A\n\t\theader_A_1, header_A_2,\n\tand their columns are removed/kept.\n\nIII.\tThe header snippets are cAsE sEnSiTiVe\n\nIV.\tUse ; as a separator\n\nV.\tMake sure you have write priviliges on\n\tthe input folder.\n\nVI.\tAlready tweaked files will not be tweaked again, but can be\n\toverwritten! Use different filename!")


root = tk.Tk()
root.title("CSV column tweak")
root.geometry('{}x{}'.format(615, 550))
menubar=tk.Menu(root)
menubar.add_command(label="Help (F1)", command=helpfunc)
root.config(menu=menubar)

directory=tk.StringVar()
directory.set("")
removeThese=tk.StringVar()
removeThese.set("")
IsRemove=tk.BooleanVar()
IsRemove.set(True)


mappaF=tk.Frame(root, bd=2, relief="groove")
mappaF.grid(row=0, column=0,pady=10,padx=10)
browse=tk.Button(mappaF, command=dirIn, text="Open files", bg="skyblue")
browse.grid(row=0, column=0,padx=5)
tk.Label(mappaF, text="Header snippets\nUse ; as separator!  Case sensitive!").grid(row=0, column=1)
tk.Entry(mappaF, width=50, textvariable=removeThese).grid(row=0, column=2,padx=10)
RBF=tk.Frame(mappaF)
RBF.grid(row=1, column=2)
RemBut=tk.Radiobutton(RBF, text="Remove 'em", variable=IsRemove, value=True).grid(row=0, column=0,padx=10)
KeepBut=tk.Radiobutton(RBF, text="Keep 'em", variable=IsRemove, value=False).grid(row=0, column=1,padx=10)

outF=tk.Frame(root)
outF.grid(row=1, column=0, padx=10, pady=10)
scrollbarY = tk.Scrollbar(outF, orient='vertical')
scrollbarY.grid(row=1, column=1,sticky="NS")
scrollbarX = tk.Scrollbar(outF, orient='horizontal')
scrollbarX.grid(row=2, column=0,sticky="EW")
tk.Label(outF, text="Headers in files").grid(row=0,column=0)
lista = tk.Listbox(outF, yscrollcommand=scrollbarY.set,xscrollcommand=scrollbarX.set, width=95,selectmode="multiple")
scrollbarY.config(command=lista.yview)
scrollbarX.config(command=lista.xview)
lista.grid(row=1, column=0)

exportdata=[]
inPdelimiter=tk.StringVar()
inPdelimiter.set(",")

expF=tk.Frame(root, bd=5, relief="sunken")
expF.grid(row=2, column=0, pady=20)
tk.Label(expF,text="     Select delimiter of input files     ").grid(row=0, column=0,pady=10)
tk.Radiobutton(expF, text="Tab", variable=inPdelimiter, value="\t",anchor="e").grid(row=1, column=0)
tk.Radiobutton(expF, text="  ;  ", variable=inPdelimiter, value=";",anchor="e").grid(row=2, column=0)
tk.Radiobutton(expF, text="  ,  ", variable=inPdelimiter, value=",",anchor="e").grid(row=3, column=0)
expB=tk.Button(expF, text="Export to files", state="disabled",bg="skyblue",command=exportFunction)
expB.grid(row=5, column=0, pady=10)

tk.Label(root,text=version).grid(row=3,column=0, sticky="SW")
root.bind("<F1>", helpfunc)
root.mainloop()
