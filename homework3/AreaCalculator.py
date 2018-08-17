#!/usr/bin/env python
# -*- coding:utf-8 -*-

from tkinter import *
from math import  *
from SetParameter import *

root=Tk()
root.minsize(600,300)
root.title('Area Calculator')

PI=3.1415926
GraphicParameterName=[['length',''],['length','width'],['base','height'],['radius','']]
GraphicParameter=[[0,1,1,1],[0,0,1,1],[0,0,0.5,1],[0,1,PI,1]]

SetParameterLabel()

root.mainloop()