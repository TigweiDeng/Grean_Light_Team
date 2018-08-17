from tkinter import *
from AreaCalculator import *
from TypeIndexGet import *
from SetParameter import *
from ButtonClassesAndOperation import *


Conversion=2.54*2.54

def GetParameter(parameter):
    graphicParameter=GraphicParameter[:]
    isGraphicType=IsType[0]
    isUnitType=IsType[1]
    i = GetTypeIndex(isGraphicType)
    j=GetTypeIndex(isUnitType)
    for k in range(0,len(parameter)):
        if parameter[k].get()!='':
            graphicParameter[i][k]=eval(parameter[k].get())
    if i==0 or i==3:
        graphicParameter[i][1]=graphicParameter[i][0]
    if j==1:
        graphicParameter[i][3]=Conversion
    calculate(graphicParameter[i][0],graphicParameter[i][1],graphicParameter[i][2],graphicParameter[i][3])

def calculate(length,width,coeffi,trans):
    result = StringVar()
    result.set('%s'%('%.3f'%(length*width*coeffi*trans)))
    resultLabel = Label(root, font=('微软雅黑', 18), bg='white', fg='black', textvariable=result)
    resultLabel.place(x=300, y=220, width=300, height=80)