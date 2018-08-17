from SetButtonClass import *

ButtonType=setButtonClass()

def buttonDo(i,j,colour):
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