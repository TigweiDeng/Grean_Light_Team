from ButtonClassesAndOperation import *

def setButtonClass():
    buttonType=[[0,0,0,0],[0,0]]
    for i in range(0,2):
        color=['blue','red']
        num=len(buttonType[i])
        for j in range(0,num):
            buttonType[i][j]=ButtonClass(ButtonTypeName[i][j],i,j,150*(i+1)*j,80*i,150*(i+1),80,color[i])
            buttonType[i][j].setButton()
    return buttonType

