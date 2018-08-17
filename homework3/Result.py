from tkinter import *


PI=3.14159
Conversion=2.54*2.54

def calculate(root,length,width,coeffi,trans):
    result = StringVar()
    result.set('%s'%('%.3f'%(length*width*coeffi*trans)))
    resultLabel = Label(root, font=('微软雅黑', 18), bg='white', fg='black', textvariable=result)
    resultLabel.place(x=300, y=220, width=300, height=80)