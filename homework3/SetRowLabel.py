
from Const import *
from GridClass import *

label = []

def setRowLabel():
    for i in range(0, defaultGridRowNumber):
        labelType = gridClass(rowName[i], i, 0, firstColumnWidth, defaultGridHeight, isLabel = True, iColor = 'SystemButtonFace')
        label.append(labelType)

    return label