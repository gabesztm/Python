import tkinter as tk
from tkinter import filedialog, messagebox
import csv





version="v1.0  ™.G"

inCSVs=[]
commonheader=""

def dirIn(*args):
    global  directory, lista,expB,exportdata, inCSVs, commonheader
    inCSVs=filedialog.askopenfilenames()
    expB.config(state="disabled")
    lista.delete(0, "end")
    if len(inCSVs):
        for file in inCSVs:
            if file.endswith(".csv") or file.endswith(".CSV") and ("snipped" not in file):
                expB.config(state="normal")
                curFile=open(file, "r",encoding="UTF-8")
                curFile.seek(0)
                commonheader= curFile.readline()
                lista.insert("end", commonheader)
                curFile.close()







def exportFunction(*args):
    global delimiter,exportdata,expB, removeThese, inCSVs, commonheader
    removeHeaders=[x.strip() for x in removeThese.get().split(";")]
    commonheaderlist=[x.strip() for x in commonheader.split(",")]
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
            outfilename=str(splittedfilename[0])+"_snipped.csv"
            inF=open(files,"r", encoding="UTF-8")
            reader=csv.reader(inF)      #'file.readline()' doesn't work for some unknown reason, it misses lines.
            try:
                outF=open(outfilename, "w",encoding="UTF-8")
            except:
                messagebox.showerror("Oops!", "Couldn't create output file. Maybe the same directory has write protection")
                break
            linecounter=1

            for line in reader:
                snippedtobeList=line
                linetowrite=""
                ind = 0
                for column in commonheaderlist:
                    if ind not in removeIndices:
                        if(2<len(snippedtobeList)):
                            linetowrite+=str(snippedtobeList[ind]+",")

                    ind+=1
                outF.write(linetowrite+"\n")
                linecounter+=1
            inF.close()
            outF.close()
    messagebox.showinfo("Info","Snipped files are exported to the same directory where the input ones are.")

def helpfunc(*args):
    messagebox.showinfo("Help","I.\tOpen CSV files with headers from which you'd like to discard\n\tcolumns with specific or repetitively occurring headers.\n\tYou can select multiple files.\n\nII.\tIf you have a header like\n\t\theader_A_1, header_B_1, header_A_2, header_B_2\n\tand you type  _A\n\t\theader_A_1, header_A_2,\n\tand their columns are removed.\n\nIII.\tThe header snippets are cAsE sEnSiTiVe\n\nIV.\tUse ; as a separator\n\nV.\tMake sure you have write priviliges on\n\tthe input folder.\n\nVI.\tAlready snipped files will not be snipped again, but can be\n\toverwritten! Use different filename!")


root = tk.Tk()
root.title("CSV column remover")
root.geometry('{}x{}'.format(615, 400))
menubar=tk.Menu(root)
menubar.add_command(label="Help (F1)", command=helpfunc)
root.config(menu=menubar)

directory=tk.StringVar()
directory.set("")
removeThese=tk.StringVar()
removeThese.set("")


mappaF=tk.Frame(root, bd=2, relief="groove")
mappaF.grid(row=0, column=0,pady=10,padx=10)
browse=tk.Button(mappaF, command=dirIn, text="Open files", bg="skyblue")
browse.grid(row=0, column=0,padx=5)
tk.Label(mappaF, text="Header snippets\nUse ; as separator!  Case sensitive!").grid(row=0, column=1)
tk.Entry(mappaF, width=50, textvariable=removeThese).grid(row=0, column=2,padx=10)


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
delimiter=tk.StringVar()
delimiter.set(";")

expF=tk.Frame(root, bd=0, relief="sunken")
expF.grid(row=2, column=0, pady=20)

expB=tk.Button(expF, text="Export to file", state="disabled",bg="skyblue",command=exportFunction)
expB.grid(row=5, column=0, pady=10)

tk.Label(root,text=version).grid(row=3,column=0, sticky="SW")
root.bind("<F1>", helpfunc)
root.mainloop()