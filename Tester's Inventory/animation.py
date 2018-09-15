class Animation():
    def __init__(self):
        self.IsfinishX=False
        self.IsfinishY=False
        self.IncreaseX=True
        self.IncreaseY=True
        self.DirectionX=1
        self.DirectionY=1


    def resize(self,tk_widget,TargetWidth,TargetHeight, velocityX=30, velocityY=30):
        Width=tk_widget.winfo_width()
        Height=tk_widget.winfo_height()
        if Width>=TargetWidth:
            self.IncreaseX=False
        if (self.IncreaseX and Width>=TargetWidth) or (not self.IncreaseX and Width<=TargetWidth):
            self.IsfinishX=True
        if not self.IncreaseX:
            self.DirectionX=-1
        if Height>=TargetHeight:
            self.IncreaseY=False
        if (self.IncreaseY and Height>=TargetHeight) or (not self.IncreaseY and Height<=TargetHeight):
            self.IsfinishY=True
        if not self.IncreaseY:
            self.DirectionY=-1
        if not self.IsfinishX:
            Width+=(velocityX*self.DirectionX)
        if not self.IsfinishY:
            Height+=(velocityY*self.DirectionY)
        tk_widget.geometry("{}x{}".format(Width, Height))
        if self.IsfinishX and self.IsfinishY:
            return
        tk_widget.after(20, lambda: self.resize(tk_widget,TargetWidth, TargetHeight, velocityX,velocityY))

