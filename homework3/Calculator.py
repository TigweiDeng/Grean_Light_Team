#!/usr/bin/env python
# -*- coding:utf-8 -*-

from tkinter import *
from math import  *
from Result import *


class ButtonClass:
    type=NONE
    name=NONE
    iIndex=NONE
    jIndex=NONE
    xPosition=NONE
    yPosition=NONE
    buttonWidth=NONE
    buttonHeight=NONE
    buttonColor=NONE
    def __init__(self,textName,iIndexNumber,jIndexNumber,x,y,width,height,color):
        self.name=textName
        self.iIndex=iIndexNumber
        self.jIndex=jIndexNumber
        self.xPosition=x
        self.yPosition=y
        self.buttonWidth=width
        self.buttonHeight=height
        self.buttonColor=color
    def setButton(self):
        self.type=Button(root,text=self.name,font=('微软雅黑',18),command=lambda :ChangeColor(self.iIndex,self.jIndex,self.buttonColor),\
        bg = Color[self.iIndex][self.jIndex])
        self.type.place(x=self.xPosition,y=self.yPosition,width=self.buttonWidth,height=self.buttonHeight)


root=Tk()
root.minsize(600,300)
root.title('calculator')

ButtonTypeName=[['square','rectangular','triangle','circular'],['in centimeter','in inch']]
GraphicParameterName=[['length',''],['length','width'],['base','height'],['radius','']]
GraphicParameter=[[0,1,1,1],[0,0,1,1],[0,0,0.5,1],[0,1,PI,1]]
IsType=[[True]+[False]*3,[True,False]]
ButtonType=[[0,0,0,0],[0,0]]
Color=[['blue']+['#EEE9E9']*3,['red','#EEE9E9']]

for i in range(0,2):
    color=['blue','red']
    num=len(ButtonType[i])
    for j in range(0,num):
        ButtonType[i][j]=ButtonClass(ButtonTypeName[i][j],i,j,150*(i+1)*j,80*i,150*(i+1),80,color[i])
        ButtonType[i][j].setButton()



def ChangeColor(i,j,colour):
    k=0
    num=len(ButtonType[i])
    global IsType
    while k<num:
        if k!=j:
            ButtonType[i][k].type['bg'] = '#EEE9E9'
            IsType[i][k]=False
        k+=1
    ButtonType[i][j].type['bg'] = colour
    IsType[i][j]=True
    SetParameterLabel()




def GetTypeIndex(isType):
    i=0
    while True:
        if isType[i]:
            break
        i+=1
    return i


def SetParameterText(labelColor):
    parameter=[]
    for i in range(0,2):
        if labelColor[i]=='#EEE9E9':
            parameter.append(Entry(root,font=('微软雅黑',18)))
            parameter[-1].place(x=150+300*i,y=160,width=150,height=60)
    calculateButton = Button(root, text='calculate area in cm2', font=('微软雅黑', 18), fg=('black'),  command=lambda: GetParameter(parameter))
    calculateButton.place(y=220,width=300,height=80)






def SetParameterLabel():
    isGraphicType=IsType[0][:]
    i=GetTypeIndex(isGraphicType)
    parameterName=[0,0]
    parameterLabel=[0,0]
    labelColor=[]
    for j in range(0,2):
        parameterName[j]=StringVar()
        parameterName[j].set(GraphicParameterName[i][j])
        parameterLabel[j]=Label(root,font = ('微软雅黑',15),fg = 'black',textvariable = parameterName[j])
        parameterLabel[j].place(x=j*300, y=160, width=150, height=60)
        if GraphicParameterName[i][j]!='':
            parameterLabel[j]['bg']='#EEE9E9'
        labelColor.append(parameterLabel[j]['bg'])
    SetParameterText(labelColor)



def GetParameter(parameter):
    graphicParameter=GraphicParameter[:]
    isGraphicType=IsType[0][:]
    isUnitType=IsType[1][:]
    i = GetTypeIndex(isGraphicType)
    j=GetTypeIndex(isUnitType)
    for k in range(0,len(parameter)):
        if parameter[k].get()!='':
            graphicParameter[i][k]=eval(parameter[k].get())
    if i==0 or i==3:
        graphicParameter[i][1]=graphicParameter[i][0]
    if j==1:
        graphicParameter[i][3]=Conversion
    calculate(root,graphicParameter[i][0],graphicParameter[i][1],graphicParameter[i][2],graphicParameter[i][3])




SetParameterLabel()





root.mainloop()