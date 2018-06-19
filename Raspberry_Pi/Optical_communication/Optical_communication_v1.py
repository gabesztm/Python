import tkinter as tk
import RPi.GPIO as io
from time import sleep
import threading


version="v1   ™.G"
title="RaspberryPi Optical chat"

io.setwarnings(False)
io.setmode(io.BCM)

sendport=20
receiveport=12

io.setup(sendport,io.OUT)
io.output(sendport,False)
io.setup(receiveport, io.IN)


interfaceWidth=150
interfaceHeight=300

signaltime=0.05

startsignaltrue=0.06
startsignalfalse=0.06

EndOfTransmission=4 #ASCII code
msgString=''

	
class signalread(threading.Thread):
	def run(self):
		global globmode, msgString
		while True:
			signallist=[]
			if io.input(receiveport)==1:
				sleep(startsignalfalse)
				sleep(startsignaltrue)
				for bit in range(0,7):
					sleep(signaltime/2)
					signallist.append(io.input(receiveport))
					sleep(signaltime/2)
					sleep(signaltime)
			if len(signallist)>0:
				signallistReal=[]
				for bits in signallist:
					signallistReal.insert(0,int(bits))
				self.msgBin=''
				for bits in signallistReal:
					self.msgBin+=str(bits)
				self.receiveDec=int(self.msgBin,2)
				if self.receiveDec==ord('_'):
					msgString+=' '
				else:
					msgString+=chr(self.receiveDec)
				if self.receiveDec==EndOfTransmission:
					sleep(0.9)
					msgString=''
			sleep(0.0001)
					
					
class GUI(threading.Thread):
	def run(self):		
		self.root=tk.Tk()
		global mode, interfaceF, globmode
		self.root.title(title)
		self.root.geometry("{}x{}".format(400,300))
		self.vL=tk.Label(self.root, text=version)
		self.vL.pack(pady=10,anchor="ne")
		self.mode=tk.IntVar()	#1: send, 2: receive
		self.modeF=tk.Frame(self.root, bd=1, relief="sunken")
		self.modeF.pack(pady=10)
		self.interfaceF=tk.Frame(self.root,width=interfaceWidth, height=interfaceHeight)
		self.interfaceF.pack()
		self.destroyableF=tk.Frame(self.interfaceF)  #frame that contain different widgets for the different modes
		self.destroyableF.pack(fill="both", expand=True)
		tk.Label(self.modeF, text="Select mode", font="Helvetica 12 bold").pack()
		tk.Radiobutton(self.modeF,text="Send     ", variable=self.mode, value=1, command=self.setinterface).pack()
		tk.Radiobutton(self.modeF,text="Receive", variable=self.mode, value=2, command=self.setinterface).pack()
		self.root.mainloop()
	def setinterface(self):
		global mode, destroyableF, interfaceF, msgE, msgL, sendB, root, msgString
		if self.mode.get()==2:     # receive mode
			try:
				self.destroyableF.destroy()
			except Exception:
				()
			self.destroyableF=tk.Frame(self.interfaceF,width=interfaceWidth, height=interfaceHeight)
			self.destroyableF.pack(fill="both", expand=False)
			self.scrollbar = tk.Scrollbar(self.destroyableF, orient='vertical')
			self.scrollbar.grid(row=0, column=1, sticky="NS")
			self.lista = tk.Listbox(self.destroyableF, yscrollcommand=self.scrollbar.set, width=25,selectmode="multiple")
			self.scrollbar.config(command=self.lista.yview)
			self.lista.grid(row=0, column=0)
			self.updateinterface()
		if self.mode.get()==1:				#send mode
			global msg
			try:
				self.destroyableF.destroy()
			except Exception:
				()
			self.destroyableF=tk.Frame(self.interfaceF,width=interfaceWidth, height=interfaceHeight)
			self.destroyableF.pack(fill="both", expand=False)
			self.msg=tk.StringVar()
			self.msgE=tk.Entry(self.destroyableF,textvariable=self.msg, width=25, font="Helvetica 12").pack()
			self.sendB=tk.Button(self.destroyableF, text="Send", command=self.sendF).pack()
			self.destroyableF.bind("<Return>",self.sendF)
	
	def updateinterface(self):
		global mode, msgString, destroyableF,root
		if self.mode.get()==2:
			if len(msgString)>0 and msgString[len(msgString)-1]==chr(EndOfTransmission):
				self.lista.insert('end',msgString[:-1])
			
			self.root.after(900, self.updateinterface)
			
			
			
	def sendF(self):
		global msg, msgE
		self.msgstring=self.msg.get()+chr(EndOfTransmission)
		if self.msgstring=="":
			self.msgstring="_"
		try:
			self.msgE.delete(0,"end")
		except Exception:
			()
		for chars in self.msgstring:
			if chars==' ':
				chars='_'
			self.msgdec=ord(str(chars))
			self.msgbin="{0:b}".format(self.msgdec)
			io.output(sendport,True)    #start signalling
			sleep(startsignaltrue)
			io.output(sendport,False)
			sleep(startsignalfalse)
			self.msgbinR=[]
			for bits in self.msgbin:
				self.msgbinR.insert(0, int(bits))
			for bit in self.msgbinR:
				if int(bit)==1:
					io.output(sendport,True)
					sleep(signaltime)
					io.output(sendport,False)
					sleep(signaltime)
				else:
					sleep(signaltime)
					sleep(signaltime)
		
	


GUI().start()
signalread().start()

