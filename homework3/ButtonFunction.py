
from Const import *

def buttonFunction(gridList, name):

    def checkName():
        i = 0
        j = 0
        while True:
            haveBreak = False
            buttonNumber = len(buttonName[i])
            for j in range(0, buttonNumber):
                if gridList[i][j].name == name:
                    haveBreak = True
                    break
            if haveBreak:
                break
            i += 1
        return i, j

    def changeColor(): 
        buttonNumber = len(buttonName[i])
        for k in range(0, buttonNumber):
            gridList[i][k].grid['bg'] = gridList[i][k].defaultColor
        gridList[i][j].grid['bg'] = gridList[i][k].changedColor

    i, j = checkName()
    changeColor()








"""
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
"""