import tkinter as tk
from math import sin, cos, radians

class Gauge(tk.Widget):
    def __init__(self,master, sizeinpixel,_from,_to, Isshowrange=True):
        self.can=tk.Canvas(master, height=sizeinpixel/2, width=sizeinpixel)
        self.can.create_arc(2,sizeinpixel,sizeinpixel,2,start=0, extent=180, width=4, style="arc")
        self._from=_from
        self._to=_to
        self.armlength=sizeinpixel/2
        self.arm=self.can.create_line(0,self.armlength,self.armlength, self.armlength, width=4)
        if Isshowrange:
            self.can.create_text(15,sizeinpixel/2-5, text=str(_from))
            self.can.create_text(sizeinpixel-15,sizeinpixel/2-5, text=str(_to))
        else:
            self.can.create_text(15,sizeinpixel/2-5)
            self.can.create_text(sizeinpixel-15,sizeinpixel/2-5)
    def pack(self):
        self.can.pack()
    def grid(self, row, column):
        self.can.grid(row=row, column=column)
    def setGauge(self,pointTo,color):
        if pointTo<self._from:
            pointTo=self._from
        elif pointTo>self._to:
            pointTo=self._to
        _range=abs(self._from)+abs(self._to)
        step=pointTo-self._from
        rotatedegree=180/_range*step
        self.can.delete(self.arm)
        armX=self.armlength*cos(radians(rotatedegree))
        armY=self.armlength*sin(radians(rotatedegree))
        self.arm=self.can.create_line(self.armlength-armX,self.armlength-armY,self.armlength, self.armlength, width=4,fill=color)


