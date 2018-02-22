
try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

from tkinter import filedialog, messagebox
version="v2.1  ™.G"

def showxy(event):
    rad=2
    global sites, lista, sitecoords
    sx1, sy1 = (event.x - rad), (event.y - rad)
    sx2, sy2 = (event.x + rad), (event.y + rad)
    site=cv.create_oval(sx1, sy1, sx2, sy2, fill="red", outline="red",tag="wafer")
    sites.append(site)
    sx,sy="{0:.2f}".format((event.x-wafercenterx)*wafersize.get()/drawdiameter),"{0:.2f}".format((wafercentery-event.y)*wafersize.get()/drawdiameter)
    lista.insert("end",str(len(sites))+".    "+str(sx)+"   "+str(sy))
    sitecoords.append((sx,sy))


def showcurrent(event):
    global LX,LY
    LX.config(text="{0:.2f}".format((event.x - wafercenterx) * wafersize.get() / drawdiameter))
    LY.config(text="{0:.2f}".format((wafercentery-event.y)*wafersize.get()/drawdiameter))


def clearcanvas(*args):
    global cv,sites, sitecoords
    for site in sites:
        cv.delete(site)
    sites=[]
    sitecoords=[]
    lista.delete(0,"end")

def removesites(*args):
    global cv,sites, lista
    rem=lista.curselection()
    help=0
    for site in rem:
        cv.delete(sites[site-help])
        lista.delete(site)
        del sites[site-help]
        del sitecoords[site-help]
        help+=1

def export(*args):
    global sitecoords
    if len(sitecoords)>0:
        if swtype.get()==1:
            file=filedialog.asksaveasfile(defaultextension=".csv",filetypes=(("Comma-separated Values", "*.csv"), ))
            try:
                print(file.name)
                f=open(file.name,'w',encoding='UTF-8')
                f.write("...Company confidential header.....\n")
                elementnumber=1
                for elements in sitecoords:
                    f.write(str(float(elements[0]))+str(float(elements[1])))
                    elementnumber+=1
                f.close()
            except AttributeError:
                messagebox.showwarning("Warning!","No file specified")
        if swtype.get()==2:
            file=filedialog.asksaveasfile(defaultextension=".xml",filetypes=(("Extensible Markup Language", "*.xml"), ))
            try:
                print(file.name)
                f=open(file.name,'w',encoding='UTF-8')
                f.write("...Company confidential structure...")
                for elements in sitecoords:
                    f.write(str(float(elements[0]))+str(float(elements[1])))    #this is not a duplicate with line60 in the original version
                f.close()
            except AttributeError:
                messagebox.showwarning("Warning!","No file specified")
    else:
        messagebox.showwarning("Warning!","There is nothing to export")
root = tk.Tk()
root.title("Manual site generator")
root.geometry('{}x{}'.format(680, 525))
global cv,lista, LX, LY
wafersize=tk.IntVar()
wafersize.set(300)
swtype=tk.IntVar()
swtype.set(1)
w = 400
h = 400
sites=[]
sitecoords=[]
df=tk.Frame(root,bd=2,relief="groove")

df.grid(row=0,column=0,padx=20,pady=20)
cv = tk.Canvas(df, width=w, height=h, bg='lightblue',cursor="dotbox")
cv.pack()
labF=tk.Frame(df,bd=1, relief="solid")
labF.pack(pady=5)

# upper left corner coordinates x1, y1
# lower right corner coordinates x2, y2
x1 = 20
y1 = 30
x2 = 380
y2 = 370
drawdiameter=x2-x1

wafercenterx,wafercentery=x1+(x2-x1)/2, y1+(y2-y1)/2
cv.create_oval(x1, y1, x2, y2, fill="grey",outline="lightblue", tag="wafer")
cv.create_oval(wafercenterx-2,wafercentery-2, wafercenterx+2, wafercentery+2, fill="black", outline="black", tag="wafer")
cv.create_polygon((x1+(x2-x1)/2-10, y2, x1+(x2-x1)/2+10, y2, x1+(x2-x1)/2, y2-10), fill="lightblue", outline="lightblue")
# bind left mouse click within shape rectangle
cv.tag_bind('wafer', '<Button-1>', showxy)

tk.Label(labF,text="X: ").grid(row=0,column=0)
tk.Label(labF,text="Y: ").grid(row=1,column=0)
LX=tk.Label(labF,text="",width=15)
LX.grid(row=0,column=1)
LY=tk.Label(labF,text="",width=15)
LY.grid(row=1,column=1)
cv.tag_bind("wafer","<Motion>", showcurrent)

utils=tk.Frame(root,bd=2,relief="groove")
utils.grid(row=0,column=1, pady=10)
rbF=tk.Frame(utils,bd=2, relief="ridge")
rbF.grid(row=0,column=0,pady=10)
tk.Label(rbF,text="Select wafersize").pack()
tk.Radiobutton(rbF, text="100 mm", variable=wafersize, value=100, command=clearcanvas).pack()
tk.Radiobutton(rbF, text="125 mm", variable=wafersize, value=125, command=clearcanvas).pack()
tk.Radiobutton(rbF, text="150 mm", variable=wafersize, value=150, command=clearcanvas).pack()
tk.Radiobutton(rbF, text="200 mm", variable=wafersize, value=200, command=clearcanvas).pack()
tk.Radiobutton(rbF, text="300 mm", variable=wafersize, value=300, command=clearcanvas).pack()

swrbF=tk.Frame(utils,bd=2, relief="ridge")
swrbF.grid(row=1,column=0,pady=5)
tk.Label(swrbF,text="Select Software").pack()
tk.Radiobutton(swrbF, text="software 1", variable=swtype, value=1).pack()       #Confidential software names come here
tk.Radiobutton(swrbF, text="software 2", variable=swtype, value=2).pack()

butts=tk.Frame(utils)
butts.grid(row=2,column=0,ipady=10)
clearB=tk.Button(butts,text="Clear map",width=13,command=clearcanvas,cursor="pirate")
clearB.grid(row=0,column=0)

saveB=tk.Button(butts,text="Export",width=13,command=export)
saveB.grid(row=2,column=0)
lbF=tk.Frame(utils)
lbF.grid(row=3,column=0)
scrollbar = tk.Scrollbar(lbF, orient='vertical')
scrollbar.grid(row=0, column=1, sticky="NS")
lista = tk.Listbox(lbF, yscrollcommand=scrollbar.set, width=25, height=8,selectmode="multiple")
scrollbar.config(command=lista.yview)
lista.grid(row=0, column=0)

tk.Label(root,text=version).grid(row=1,column=0, sticky="W")

root.mainloop()