import psutil   #pip3 install psutil
import tkinter as tk
import gauge
version="v1.0  ™.G"

cpuLabels=[]
cpuCanvases=[]
canvaslength=50
NumOfCpu=psutil.cpu_count()


def setcolor(value):
    greenuntil=40.0
    yellowuntil=60.0
    orangeuntil=80.0
    if value<=greenuntil:
        return "green"
    elif value>greenuntil and value<=yellowuntil:
        return "gold3"
    elif value>yellowuntil and value <=orangeuntil:
        return "orange"
    else:
        return "red"



def measureusage():
    global memL, memC
    PercentValues=psutil.cpu_percent(percpu=True)
    for i in range(0, NumOfCpu):
        cpuCanvases[i].delete("ALL")
        cpuLabels[i].configure(text=str(PercentValues[i])+" %", fg=setcolor(PercentValues[i]))
        cpuCanvases[i].create_line(0,5,canvaslength*PercentValues[i]/100,5, fill=setcolor(PercentValues[i]),width=6)
        cpuCanvases[i].create_line(canvaslength*PercentValues[i]/100,5,canvaslength,5, fill="black",width=6)
    memL.configure(text=str(psutil.virtual_memory()[2])+" %", fg=setcolor(psutil.virtual_memory()[2]))
    memC.delete("ALL")
    memC.create_line(0,5,canvaslength*psutil.virtual_memory()[2]/100,5, fill=setcolor(psutil.virtual_memory()[2]),width=6)
    memC.create_line(canvaslength*psutil.virtual_memory()[2]/100,5,canvaslength,5, fill="black",width=6)
    root.after(1000,measureusage)

root=tk.Tk()
root.title("System monitor")
root.geometry("{}x{}".format(230,220))
cpuFrame=tk.Frame(root, bd=2, relief="groove",width=200, height=100)
cpuFrame.grid(row=0, column=0,pady=10,padx=15)
cpuFrame.grid_propagate(False)
tk.Label(cpuFrame, text="CPU usage").grid(row=0,column=0, columnspan=3)
memFrame=tk.Frame(root, bd=2, relief="groove",width=200, height=50)
memFrame.grid(row=1, column=0,pady=10, padx=15)
memFrame.grid_propagate(False)
tk.Label(memFrame, text="Memory usage").grid(row=0,column=0, columnspan=3)
for i in range(0, NumOfCpu):
    tk.Label(cpuFrame, text="Core "+str(i+1)).grid(row=i+1, column=0, sticky="w")
    cpuL=tk.Label(cpuFrame, text="",width=6)
    cpuL.grid(row=i+1, column=1, sticky="e",padx=10)
    cpuLabels.append(cpuL)
    cpuC=tk.Canvas(cpuFrame, width=canvaslength, height=10)
    cpuC.grid(row=i+1, column=2)
    cpuCanvases.append(cpuC)
tk.Label(memFrame, text="Virtual").grid(row=1, column=0,sticky="w")
memL=tk.Label(memFrame, text="", width=6)
memL.grid(row=1, column=1,sticky="e",padx=10)
memC=tk.Canvas(memFrame, width=canvaslength, height=10)
memC.grid(row=1, column=2)
measureusage()
cpuFrame.grid_propagate(False)
tk.Label(root,text=version).grid(row=3,column=0, sticky="SW")
root.mainloop()
