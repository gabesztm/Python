import matplotlib.pyplot as plt
from utilities import *
import datetime
import matplotlib.dates as mdates
import tkinter as tk
from tkinter.filedialog import askopenfilenames



def openlogs(*args):
    global inputfiles, ListWidget, PlotButton
    inputfiles=askopenfilenames()
    if len(inputfiles)==0:
        import sys
        sys.exit()
    for logs in inputfiles:
        ListWidget.insert("end",logs)
    PlotButton.config(state="normal")

def plotfunc(*args):
    global inputfiles

    AllDate=[]
    AllTemperature=[]
    AllHumidity=[]
    AllDewpoint=[]
    AllPressure=[]

    AllDateX=[]
    AllTemperatureV=[]
    AllHumidityV=[]
    AllDewpointV=[]
    AllPressureV=[]


    for logfile in inputfiles:
        Date, Temperature, Humidity, Pressure = FileTweaks.CsvColumnToArray(logfile, True, True, [1, 2, 3,4], ";")
        AllDate.append(Date)
        AllTemperature.append(Temperature)
        AllHumidity.append(Humidity)
        AllPressure.append(Pressure)
        DewPoint=[]
        for i in range(0, len(Temperature)):
            DewPoint.append(Science.DewPointMagnus(float(Temperature[i]), float(Humidity[i])))
        AllDewpoint.append(DewPoint)
        DateX = []
        for i in range(0, len(Date)):
            DateX.append(datetime.datetime.strptime(Date[i], '%Y-%m-%d %H:%M:%S'))
        AllDateX.append(DateX)
        TemperatureV = []
        for i in range(0, len(Temperature)):
            TemperatureV.append(round(float(Temperature[i]), 2))
        AllTemperatureV.append(TemperatureV)
        HumidityV = []
        for i in range(0, len(Humidity)):
            HumidityV.append(round(float(Humidity[i]), 2))
        AllHumidityV.append(HumidityV)
        PressureV = []
        for i in range(0, len(Pressure)):
            PressureV.append(round(float(Pressure[i]), 2))
        AllPressureV.append(PressureV)
        DewPointV = []
        for i in range(0, len(DewPoint)):
            DewPointV.append(round(float(DewPoint[i]), 2))
        AllDewpointV.append(DewPointV)


    fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True,figsize=(16, 9), dpi=70, facecolor='w', edgecolor='k')

    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
    for i in range(0,len(inputfiles)):
        if i==0:
            ax1.plot(AllDateX[i], AllTemperatureV[i], "r", label="Ambient temperature")
            ax1.plot(AllDateX[i], AllDewpointV[i], 'b', label="Dew point")
        else:
            ax1.plot(AllDateX[i], AllTemperatureV[i], "r")
            ax1.plot(AllDateX[i], AllDewpointV[i], 'b')
    ax1.set_ylabel('Temperature [°C]')
    ax1.legend(loc='best', fontsize="x-large")
    ax1.grid(True)

    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
    for i in range(0,len(inputfiles)):
        ax2.plot(AllDateX[i], AllHumidityV[i],"g")
    ax2.set_ylabel("Relative Humidity [%]")
    ax2.grid(True)

    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
    for i in range(0, len(inputfiles)):
        ax3.plot(AllDateX[i], AllPressureV[i], "orange")
    ax3.set_ylabel("Pressure [Pa]")
    ax3.grid(True)

    plt.xlabel('Time')
    fig.autofmt_xdate(rotation=60)
    fig.tight_layout()

    plt.show()


root=tk.Tk()
root.geometry("{}x{}".format(605,200))
tk.Button(root,text="Open files",command=openlogs).grid(row=0,column=0,pady=5)

scrollbarY = tk.Scrollbar(root, orient='vertical')
scrollbarY.grid(row=1, column=1,sticky="NS")
scrollbarX = tk.Scrollbar(root, orient='horizontal')
scrollbarX.grid(row=2, column=0,sticky="EW",padx=10)
ListWidget = tk.Listbox(root, yscrollcommand=scrollbarY.set,xscrollcommand=scrollbarX.set, width=70,height=5,selectmode="multiple")
scrollbarY.config(command=ListWidget.yview)
scrollbarX.config(command=ListWidget.xview)
ListWidget.grid(row=1, column=0,padx=10)

PlotButton=tk.Button(root, text="Plot", command=plotfunc, state="disabled")
PlotButton.grid(row=3, column=0,pady=5)
root.mainloop()