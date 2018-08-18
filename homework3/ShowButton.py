from tkinter import *
from ButtonClass import *
from Const import *

def showButton(root, buttonClass):
    button=Button(root, text = buttonClass.name, font = (buttonClass.fontName,buttonClass.fontSize), \
        command = lambda :pressButton(), bg = buttonClass.initialColor)
    button.place(y = buttonClass.row*buttonClass.gridHeight, x = firstColumnWidth+buttonClass.column*buttonClass.gridWidth, \
        width = buttonClass.gridWidth, height = buttonClass.gridHeight)