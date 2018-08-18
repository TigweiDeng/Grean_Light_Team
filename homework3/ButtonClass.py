
from tkinter import *
from GridClass import *
from Const import *

class buttonClass(gridClass):

    isButton = True
    isLabel = False

    def __init__(self, typeName = '', rowIndex = 0, columnIndex = 0, width = restWidth, height = interfaceHeight, \
        dColor = defaultColor, iColor = defaultColor, cColor = defaultColor, fontName = '微软雅黑', fontSize = 18):
        gridClass.__init__(self, typeName, rowIndex, columnIndex, width, height, dColor, iColor, cColor, fontName, fontSize)

    def showButton(self, root):
        button=Button(root, text = self.name, font = (self.fontName,self.fontSize), \
            command = lambda :pressButton(), bg = self.initialColor)
        button.place(y = self.row*self.gridHeight, x = firstColumnWidth+self.column*self.gridWidth, \
            width = self.gridWidth, height = self.gridHeight)
       
