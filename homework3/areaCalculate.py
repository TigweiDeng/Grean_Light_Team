
from GridClass import *
from Const import *

class labelClass(gridClass):

    isLabel = True

    def __init__(self, typeName = '', rowIndex = 0, columnIndex = 0, width = restWidth, height = interfaceHeight, \
        dColor = defaultColor, iColor = defaultColor, cColor = defaultColor, fontName = '微软雅黑', fontSize = 18):
        gridClass.__init__(self, typeName, rowIndex, columnIndex, width, height, dColor, iColor, cColor, fontName, fontSize)
       
