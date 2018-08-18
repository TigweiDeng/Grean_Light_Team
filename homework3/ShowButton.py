from tkinter import *
from ButtonClass import *
from Const import *

def showButton(root, buttonClass):
    button=Button(root, text = buttonClass.name, font=('微软雅黑',18), command=lambda :pressOperation())
    button.place(y = buttonClass.row*buttonClass.buttonHeight, x = buttonClass.column*buttonClass.buttonWidth, \
        width = buttonClass.buttonWidth, height = buttonClass.buttonHeight)