import psutil   #pip3 install psutil
import tkinter as tk
import gc
import gauge

gc.enable()
version="v1.1  ™.G"

cpuLabels=[]
cpugauges=[]
canvaslength=50
NumOfCpu=psutil.cpu_count()

gaugewidth=35

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
    global memL, memC, memG
    PercentValues=psutil.cpu_percent(percpu=True)
    for i in range(0, NumOfCpu):
        cpuLabels[i].configure(text=str(PercentValues[i])+" %", fg=setcolor(PercentValues[i]))
        cpugauges[i].setGauge(PercentValues[i],setcolor(PercentValues[i]))
    memPercent=psutil.virtual_memory()[2]
    memL.configure(text=str(memPercent)+" %", fg=setcolor(memPercent))
    memG.setGauge(memPercent,setcolor(memPercent))
    gc.collect()
    root.after(1000,measureusage)

root=tk.Tk()
root.title("System monitor")
root.geometry("{}x{}".format(230,260))
cpuFrame=tk.Frame(root, bd=2, relief="groove",width=200, height=120)
cpuFrame.grid(row=0, column=0,pady=10,padx=15)
cpuFrame.grid_propagate(False)
tk.Label(cpuFrame, text="CPU usage").grid(row=0,column=0, columnspan=3)
memFrame=tk.Frame(root, bd=2, relief="groove",width=200, height=70)
memFrame.grid(row=1, column=0,pady=10, padx=15)
memFrame.grid_propagate(False)
tk.Label(memFrame, text="Memory usage").grid(row=0,column=0, columnspan=3)
for i in range(0, NumOfCpu):
    tk.Label(cpuFrame, text="Core "+str(i+1)).grid(row=i+1, column=0, sticky="w")
    cpuL=tk.Label(cpuFrame, text="",width=6)
    cpuL.grid(row=i+1, column=1, sticky="e",padx=10)
    cpuLabels.append(cpuL)
    cpuG=gauge.Gauge(cpuFrame,gaugewidth,0,100,False)
    cpuG.grid(row=i+1, column=2)
    cpugauges.append(cpuG)
tk.Label(memFrame, text="Virtual").grid(row=1, column=0,sticky="w")
memL=tk.Label(memFrame, text="", width=6)
memL.grid(row=1, column=1,sticky="e",padx=10)
memG=gauge.Gauge(memFrame,gaugewidth,0,100,False)
memG.grid(row=1, column=2)
measureusage()
cpuFrame.grid_propagate(False)
tk.Label(root,text=version).grid(row=3,column=0, sticky="SW")
root.mainloop()
