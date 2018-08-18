from ButtonClass import *
from Const import *

button = []

def setSelectButton():
    for i in range(0, buttonTypeNumber):
        button.append([])
        buttonNumber = len(buttonName[i])
        button.append([])

        for j in range(0, buttonNumber):
            buttonType = ButtonType(buttonName[i][j], i, j+1, interfaceWidth/defaultColumnNumber[i], defaultGridHeight, initialColor[i], laterColor[i])
            button[i].append(buttonType)

    return button