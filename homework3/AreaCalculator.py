#!/usr/bin/env python
# -*- coding:utf-8 -*-

from tkinter import *
from math import  *
from Const import *
from SetSelectButton import *
from ShowButton import *

root=Tk()
root.title('Area Calculator')
root.minsize(interfaceWidth,interfaceHeight)

SelectButtonClass = setSelectButton()

for i in range(0, buttonTypeNumber):
    buttonNumber = len(buttonName[i])

    for j in range(0, buttonNumber):
        showButton(root, SelectButtonClass[i][j])




root.mainloop()