class ButtonType:

    name=None
    row=None
    column=None
    buttonWidth=None
    buttonHeight=None
    initialColor=None
    laterColor=None

    def __init__(self,typeName,rowIndex,columnIndex,width,height,icolor,lcolor):
        self.name=typeName
        self.row=rowIndex
        self.column=columnIndex
        self.buttonWidth=width
        self.buttonHeight=height
        self.initialColor=icolor
        self.laterColor=lcolor


"""    def setButton(self,root=None):
        self.type=Button(self.root,text=self.name,font=('微软雅黑',18),command=lambda :buttonDo(self.iIndex,self.jIndex,self.buttonColor),\
        bg = Color[self.iIndex][self.jIndex])
        self.type.place(x=self.xPosition,y=self.yPosition,width=self.buttonWidth,height=self.buttonHeight)"""
