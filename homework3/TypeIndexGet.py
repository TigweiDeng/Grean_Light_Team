from tkinter import *
from SetParameter import *
from ButtonClassesAndOperation import *


def GetTypeIndex(isType):
    i=0
    while True:
        if isType[i]:
            break
        i+=1
    return i