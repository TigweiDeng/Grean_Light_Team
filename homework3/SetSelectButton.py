
from Const import *
from GridClass import *

button = []

def setSelectButton():
    for i in range(0, buttonTypeNumber):
        buttonNumber = len(buttonName[i])
        button.append([])

        for j in range(0, buttonNumber):
            defaultGridWidth = restWidth/defaultColumnNumber[i]
            buttonType = gridClass(buttonName[i][j], i, j, defaultGridWidth, defaultGridHeight, \
                initialColor[i][j], defaultColor, changedColor[i], isButton = True)
            button[i].append(buttonType)

    return button