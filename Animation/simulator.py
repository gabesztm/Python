import tkinter as tk
from animation import Animation

anim=Animation()


root=tk.Tk()
root.geometry("{}x{}".format(200, 300))
tk.Button(root, text="resize", command=lambda: anim.resize(root,500,400,20,5)).pack()
root.mainloop()
