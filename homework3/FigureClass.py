
from Const import *

class figureClass():

    type = None
    parameter = []
    parameterNumber = 1

    def __init__(self, j):
        self.type = geometryName[j]
        self.parameter = parameterName[j]
        self.parameterNumber = len(self.parameter)
        

"""
def __init__(self, typeName = '', rowIndex = 0, columnIndex = 0, width = restWidth, height = interfaceHeight, \
    dColor = defaultColor, iColor = defaultColor, cColor = defaultColor, fontName = '微软雅黑', fontSize = 18):
    gridClass.__init__(self, typeName, rowIndex, columnIndex, width, height, dColor, iColor, cColor, fontName, fontSize)

def showButton(self, root):
    button=Button(root, text = self.name, font = (self.fontName,self.fontSize), \
        command = lambda :pressButton(), bg = self.initialColor)
    button.place(y = self.row*self.gridHeight, x = firstColumnWidth+self.column*self.gridWidth, \
        width = self.gridWidth, height = self.gridHeight)
"""       
