from tkinter import *
from TypeIndexGet import *
from GetResult import *

def SetParameterText(labelColor):
    parameter=[]
    for i in range(0,2):
        if labelColor[i]=='#EEE9E9':
            parameter.append(Entry(root,font=('微软雅黑',18)))
            parameter[-1].place(x=150+300*i,y=160,width=150,height=60)
    calculateButton = Button(root, text='calculate area in cm²', font=('微软雅黑', 18), fg=('black'),  command=lambda: GetParameter(parameter))
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