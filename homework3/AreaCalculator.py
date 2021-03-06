#!/usr/bin/env python
# -*- coding:utf-8 -*-


from tkinter import *
from math import  *
from Const import *
from SetSelectButton import *
from GridClass import *
from SetRowLabel import *


root=Tk()
root.title('Area Calculator')
root.minsize(interfaceWidth,interfaceHeight)


SelectButtonClass = setSelectButton()

for i in range(0, buttonTypeNumber):
    buttonNumber = len(buttonName[i])

    for j in range(0, buttonNumber):
        SelectButtonClass[i][j].showGrid(root, SelectButtonClass)


CalculateButton = gridClass('Calculate', 3, 2, SelectButtonClass[3][0].gridWidth, SelectButtonClass[3][0].gridHeight, \
    iColor = 'gray', cColor= 'gray ', isButton = True)
CalculateButton.showGrid(root)


RowLabel = setRowLabel()
for i in range(0, defaultGridRowNumber):
    RowLabel[i].showGrid(root)


root.mainloop()