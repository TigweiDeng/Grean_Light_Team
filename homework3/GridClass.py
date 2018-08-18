
from tkinter import *
from Const import *
from ButtonFunction import *

class gridClass:

    name = None 

    row = None
    column = None

    gridWidth = None
    gridHeight = None

    defaultColor = None
    initialColor = None
    changedColor = None

    fontName = None
    fontSize = None

    isButton = False
    isLabel = False
    isText = False

    grid = None
    labelName = None


    def __init__(self, name = '', rowIndex = 0, columnIndex = 0, width = restWidth, height = interfaceHeight, \
        iColor = defaultColor, dColor = defaultColor, cColor = defaultColor, fontName = '微软雅黑', fontSize = 18, \
        isButton = False, isLabel = False, isText = False):
        self.name = name
        self.row = rowIndex
        self.column = columnIndex
        self.gridWidth = width
        self.gridHeight = height
        self.defaultColor = dColor
        self.initialColor = iColor
        self.changedColor = cColor
        self.fontName = fontName
        self.fontSize = fontSize
        self.isButton = isButton
        self.isLabel = isLabel
        self.isText = isText

    def showGrid(self, root, gridList = []):
        xDefault = firstColumnWidth

        if self.isButton:
            self.grid = Button(root, text = self.name, font = (self.fontName,self.fontSize), \
                command = lambda :buttonFunction(gridList, self.name), bg = self.initialColor)

        if self.isLabel:
            self.labelName = StringVar()
            self.labelName.set(self.name)
            self.grid = Label(root, font = (self.fontName, self.fontSize), textvariable = self.labelName, bg = self.initialColor, fg = 'black')
            if self.column == 0:
                xDefault = 0

#        if self.isText:

        self.grid.place(y = self.row*self.gridHeight, x = xDefault+self.column*self.gridWidth, \
            width = self.gridWidth, height = self.gridHeight)




"""
        parameterName[j]=StringVar()
        parameterName[j].set(GraphicParameterName[i][j])
        parameterLabel[j]=Label(root,font = ('微软雅黑',15),fg = 'black',textvariable = parameterName[j])
        parameterLabel[j].place(x=j*300, y=160, width=150, height=60)
        if GraphicParameterName[i][j]!='':
            parameterLabel[j]['bg']='#EEE9E9'
        labelColor.append(parameterLabel[j]['bg'])
"""