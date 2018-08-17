from tkinter import *
from ButtonDo import *


ButtonTypeName=[['square','rectangular','triangle','circular'],['in centimeter','in inch']]
Color=[['blue']+['#EEE9E9']*3,['red','#EEE9E9']]
ButtonType=[[0,0,0,0],[0,0]]
IsType=[[True]+[False]*3,[True,False]]

class ButtonClass:
    root=NONE
    type=NONE
    name=NONE
    iIndex=NONE
    jIndex=NONE
    xPosition=NONE
    yPosition=NONE
    buttonWidth=NONE
    buttonHeight=NONE
    buttonColor=NONE
    def __init__(self,mainRoot,textName,iIndexNumber,jIndexNumber,x,y,width,height,color):
        self.root=mainRoot
        self.name=textName
        self.iIndex=iIndexNumber
        self.jIndex=jIndexNumber
        self.xPosition=x
        self.yPosition=y
        self.buttonWidth=width
        self.buttonHeight=height
        self.buttonColor=color
    def setButton(self):
        self.type=Button(self.root,text=self.name,font=('微软雅黑',18),command=lambda :buttonDo(self.iIndex,self.jIndex,self.buttonColor),\
        bg = Color[self.iIndex][self.jIndex])
        self.type.place(x=self.xPosition,y=self.yPosition,width=self.buttonWidth,height=self.buttonHeight)
