# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 17:41:13 2018

@author: Tigwei's
"""

import re,os
from math import asin,acos,atan,sin,cos,tan,log,log10,log1p,\
pow,factorial,radians,degrees,e,pi

def illustrate():
    print  char,'\n',char,\
    u'\n\n\n欢迎使用基于Python语言开发的“我的简易计算器”\
    \n\n程序，本程序旨在解决用户一些基本的算术问题，您\
    \n\n可以在以下输入您所要计算的算式。\
    \n\n（ps.输入help可查看帮助）\n\n',char,'\n',char,'\n\n'
    os.system('pause')
    os.system('cls')
    calinput()
    
def calhelp():
    print  char,'\n',char,\
    u'\n\n\n三角函数：sin(x)、cos(x)、tan(x)，\
    \n\n反三角函数：asin(x)、acos(x)、atan(x)，\
    \n\n对数：lg(x)、ln(x)、log(真数,底数)，\
    \n\n指数：x^(y)、%(x,开y次幂)，\
    \n\n特殊：x！阶乘、x%y求余，\
    \n\n常数：圆周率 pi 、自然常数 e\
    \n\n特别说明：本计算器采用角度制而非弧度值\
    \n'    
    
def calinput():
    global equa0,equa1,bool0
    while True:
        print char,'\n',char,u'\n\n\n请输入算式或查看帮助：'
        equa0=raw_input('\n')
        equa1=equa0[:]
        standard()
        if equa1=='help':
            bool0=True
            os.system('cls')
            calhelp()
        else:
            check()

def check(): 
    if equa1.find('i')!=1 or equa1.find('j')!=-1:
        stancomp()
    if equa1.find('%')!=-1:
        stanroot()
    if equa1.find('!')!=-1:
        stanfac()
    if equa1.find('&')!=-1:
        stanrema()
    if equa1.find('lg')!=-1 or equa1.find('ln')!=-1:
        stanlg()
        stanln()
    if equa1.find('asin(')!=-1 or equa1.find('acos(')!=-1 or \
    equa1.find('atan(')!=-1:
        stanasin()
        stanacos()
        stanatan()
    elif equa1.find('sin(')!=-1 or equa1.find('cos(')!=-1 or \
    equa1.find('tan(')!=-1:
        stansin()
        stancos()
        stantan()
    result()
    
def standard():
    stanlow()
    standelem()
    stanflo()
    stanpow()
    stanmul()

def result():
    result=eval(equa1)
    print '= ',result,'\n'
    os.system('pause')
    os.system('cls')
    if bool0:
        calhelp()
    calinput()
    
def stanlow():
    global equa1
    equa1=equa1.lower()
    
def standelem():
    global equa1
    equa2=list(equa1)
    num=equa1.count(' ')
    for i in range(num):
        equa2.remove(' ')
        i+=1
    equa1=''.join(equa2)
    
def stanflo():
    i=equa1.find('/')
    global equa1
    while i!=-1:
        equa2=list(equa1)
        if i>0 and equa1[i-1].isdigit():
            equa2[i]='./'
        equa1=''.join(equa2)
        i=equa1.find('/',i+2,)
    
def stanpow():
    global equa1
    equa1=equa1.replace('^','**')
     
def stanmul():
    i=equa1.find('(')
    global equa1
    while i!=-1 :
        equa2=list(equa1)
        if i>0 and ( equa1[i-1]==')' or equa1[i-1].isdigit() ) :
            equa2[i]='*('
        equa1=''.join(equa2)
        i=equa1.find('(',i+2,)
        
def stancomp():
    i=equa1.find('i')
    global equa1
    while i!=-1:
        equa2=list(equa1)
        if i>0 and equa1[i-1]!='s' and equa1[i-1]!='p':
            equa2[i]='j'
        equa1=''.join(equa2)
        i=equa1.find('i',i+1,)
    j=equa1.find('j')
    while j!=-1:
        equa2=list(equa1)
        if j==0 or ( j>0 and not (equa1[j-1].isdigit()) ):
            equa2[j]='1j'
        equa1=''.join(equa2)
        j=equa1.find('j',j+2,)
        
def stanroot():
    i=equa1.find('%(')
    global equa1
    while i!=-1:
        equa2=list(equa1)
        if i>0 and equa1[i-1].isdigit():
            equa2[i]='*pow'
        else:
            equa2[i]='pow'
        equa1=''.join(equa2)
        ilist,jlist=lbrac(i+1)
        i=ilist[0]
        j=jlist[0]
        klist=[x.start()+i for x in re.finditer(',',equa1[i:j])]
        k=0
        p=0
        l=0
        while p<len(klist):
            boolean=False
            l=len(ilist)-1
            k=klist[p]
            while l<len(ilist) and l>=0:
                if k<jlist[l] and k>ilist[l]:
                    boolean=True
                    break
                l-=1
            if l==0 and boolean:
                break
            p+=1
        equa2=list(equa1)
        if l==-1:
            equa2[j]=',1./2)'
        elif l==0 and equa1[j-1]==',':
            equa2[j]='1./2)'
        else:
            equa2[k]=',1./('
            equa2[j]='))'
        equa1=''.join(equa2)
        i=equa1.find('%(',i,)
        
def stanfac():
    i=equa1.find('!')
    global equa1
    while i!=-1:
        equa2=list(equa1)
        equa2[i]=')'
        j=i
        if equa1[i-1]==')':
            ilist,jlist=rbrac(i-1)
            i=ilist[0]
            j=jlist[0]
        else :
            while j>0 and equa1[j-1].isdigit():
                j-=1
        equa2.insert(j,'factorial(')
        equa1=''.join(equa2)
        i=equa1.find('!',i+10,)
        
def stanrema():
    global equa1
    equa1=equa1.replace('&','%')
    
def stanlg():
    i=equa1.find('lg(')
    global equa1
    while i!=-1:
        equa2=list(equa1)
        if i>0 and equa1[i-1].isdigit():
            equa1[i]='*l'
        equa1=''.join(equa2)
        i=equa1.find('lg(',i+3,)
    equa1=equa1.replace('lg(','log10(')
    
def stanln():
    i=equa1.find('ln(')
    global equa1
    while i!=-1:
        equa2=list(equa1)
        if i>0 and equa1[i-1].isdigit():
            equa1[i]='*l'
        equa1=''.join(equa2)
        i=equa1.find('ln(',i+3,)
    equa1=equa1.replace('ln(','log1p(-1+')
    
def stanasin():
    i=equa1.find('asin(')
    global equa1
    while i!=-1:
        equa2=list(equa1)
        if i>0 and equa1[i-1].isdigit():
            equa2[i]='*degrees(a'
        else:
            equa2[i]='degrees(a'
        ilist,jlist=lbrac(i)
        j=jlist[0]
        equa2[j]='))'
        equa1=''.join(equa2)
        i=equa1.find('asin(',i+10,)
        
def stanacos():
    i=equa1.find('acos(')
    global equa1
    while i!=-1:
        equa2=list(equa1)
        if i>0 and equa1[i-1].isdigit():
            equa2[i]='*degrees(a'
        else:
            equa2[i]='degrees(a'
        ilist,jlist=lbrac(i)
        j=jlist[0]
        equa2[j]='))'
        equa1=''.join(equa2)
        i=equa1.find('acos(',i+10,)
        
def stanatan():
    i=equa1.find('atan(')
    global equa1
    while i!=-1:
        equa2=list(equa1)
        if i>0 and equa1[i-1].isdigit():
            equa2[i]='*degrees(a'
        else:
            equa2[i]='degrees(a'
        ilist,jlist=lbrac(i)
        j=jlist[0]
        equa2[j]='))'
        equa1=''.join(equa2)
        i=equa1.find('atan(',i+10,)
        
def stansin():
    i=equa1.find('sin(')
    global equa1
    while i!=-1:
        equa2=list(equa1)
        if i>0 and equa1[i-1].isdigit():
            equa2[i]='*s'
        equa2[i+3]='(radians('
        ilist,jlist=lbrac(i)
        j=jlist[0]
        equa2[j]='))'
        equa1=''.join(equa2)
        i=equa1.find('sin(',i+10,)     
        
def stancos():
    i=equa1.find('cos(')
    global equa1
    while i!=-1:
        equa2=list(equa1)
        if i>0 and equa1[i-1].isdigit():
            equa2[i]='*c'
        equa2[i+3]='(radians('
        ilist,jlist=lbrac(i)
        j=jlist[0]
        equa2[j]='))'
        equa1=''.join(equa2)
        i=equa1.find('cos(',i+10,) 

def stantan():
    i=equa1.find('tan(')
    global equa1
    while i!=-1:
        equa2=list(equa1)
        if i>0 and equa1[i-1].isdigit():
            equa2[i]='*t'
        equa2[i+3]='(radians('
        ilist,jlist=lbrac(i)
        j=jlist[0]
        equa2[j]='))'
        equa1=''.join(equa2)
        i=equa1.find('tan(',i+10,)
        
def rbrac(x):
    rlist=[]
    llist=[]
    i=0
    while i!=1:
        if equa1[x]==')':
            rlist.append(x)
            llist.append(-1)
        elif equa1[x]=='(':
            i=len(rlist)
            while i>0 and llist[i-1]!=-1:
                i-=1
            llist[i-1]=x
        x-=1
    return rlist,llist
    
def lbrac(x):
    rlist=[]
    llist=[]
    i=0
    while i!=1:
        if equa1[x]=='(':
            llist.append(x)
            rlist.append(-1)
        elif equa1[x]==')':
            i=len(llist)
            while i>0 and rlist[i-1]!=-1:
                i-=1
            rlist[i-1]=x
        x+=1
    return llist,rlist
      
equa0=[]
equa1=[]
bool0=False
char='_'*60
os.system('cls')
illustrate()