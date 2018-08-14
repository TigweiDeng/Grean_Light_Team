# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 17:41:13 2018

@author: Tigwei's
"""

#本程序各部分注释皆置于前一行

#引入re模块以便运用re.finditer函数查找列表中某字符所有位置
#引入os模块以便运用os.system函数进行清屏以及任意键继续操作
import re,os 

#引入数学计算所需函数或常数
from math import asin,acos,atan,sin,cos,tan,log,log10,log1p,\
pow,factorial,radians,degrees,e,pi

#定义calstart函数用以开始程序流程
def calstart(): 
    print  char,'\n',char,\
    u'\n\n\n欢迎使用基于Python语言开发的“我的简易计算器”\
    \n\n程序，本程序旨在解决用户一些基本的算术问题，\
    \n\n您可以在以下输入您所要计算的算式。\
    \n\n（ps.输入help可查看帮助，输入exit或点击右上\
    \n\n  角可退出程序）\n\n',char,'\n',char,'\n\n'
    os.system('pause')
    os.system('cls')
    calinput()

#定义calhelp函数帮助用户查看使用指南    
def calhelp():
    print  char,'\n',char,\
    u'\n\n\n三角函数：sin(x)、cos(x)、tan(x)，\
    \n\n反三角函数：asin(x)、acos(x)、atan(x)，\
    \n\n对数：lg(x)、ln(x)、log(真数,底数)，\
    \n\n指数：底数^(指数)、%(x,开y次幂)，\
    \n\n特殊：x！阶乘、x&y求余，\
    \n\n常数：圆周率 pi 、自然常数 e\
    \n\n特别说明：1.本计算器采用角度制而非弧度值\
    \n\n         2.输入close可关闭帮助内容\n' 

#定义calclose函数关闭帮助内容
def calclose():
    os.system('cls')

#定义calexit函数用以退出程序————跳过各运算步骤    
def calexit():
    os.system('cls')
    print char,'\n',char,\
    u'\n\n\n感谢您的本次使用，再见！\n\n',char,'\n',char,'\n\n'

#定义calinput函数用以接收用户输入的算式或指令    
def calinput():
    global equa0,equa1,bool0
    while True:
        print char,'\n',char,u'\n\n\n请输入算式或指令（查看帮助\
和退出程序）：'
        equa0=raw_input('\n')
        equa1=equa0[:]
        standard()
        #判断输入的是否为算式或指令以及指令的类型
        if equa1=='help':
            bool0=True
            os.system('cls')
            calhelp()
        elif equa1=='close':
            calclose()
            bool0=False
        elif equa1.find('exit')!=-1:
            calexit()
            break
        else:
            check()

#定义standard函数对用户输入的算式或指令格式标准化
#如化为小写、去除空格、除式浮点化等           
def standard():
    stanlow()
    standelem()
    stanflo()
    stanpow()
    stanmul()

#定义check函数检测算式所包含的运算类型并输出结果   
def check(): 
    #判断存在复数时的操作
    if equa1.find('i')!=1 or equa1.find('j')!=-1:
        stancomp()
    #判断存在开方运算时的操作
    if equa1.find('%')!=-1:
        stanroot()
    #判断存在阶乘运算时的操作
    if equa1.find('!')!=-1:
        stanfac()
    #判断存在求余运算时的操作
    if equa1.find('&')!=-1:
        stanrema()
    #判断存在对数运算时的操作
    if equa1.find('lg')!=-1 or equa1.find('ln')!=-1:
        stanlg()
        stanln()
    #判断存在反三角函数时的操作
    #ps.反三角函数的判断必须在三角函数的判断之前
    if equa1.find('asin(')!=-1 or equa1.find('acos(')!=-1 or \
    equa1.find('atan(')!=-1:
        stanasin()
        stanacos()
        stanatan()
    #判断存在三角函数时的操作
    elif equa1.find('sin(')!=-1 or equa1.find('cos(')!=-1 or \
    equa1.find('tan(')!=-1:
        stansin()
        stancos()
        stantan()
    #输出结果
    result()

def result():
    #用函数eval将字符串转为算式并计算
    result=eval(equa1)
    print '= ',result,'\n'
    os.system('pause')
    os.system('cls')
    #判断用户之前是否查看帮助且未关闭帮助内容，若是则保留帮助内容
    if bool0:
        calhelp()

#定义stanlow函数将算式指令小写化    
def stanlow():
    global equa1
    equa1=equa1.lower()

#定义standelem函数去除算式指令中所含的空格    
def standelem():
    global equa1
    equa2=list(equa1)
    num=equa1.count(' ')
    for i in range(num):
        equa2.remove(' ')
        i+=1
    equa1=''.join(equa2)

#定义stanflo函数将除式浮点化    
def stanflo():
    i=equa1.find('/')
    global equa1
    while i!=-1:
        equa2=list(equa1)
        if i>0 and equa1[i-1].isdigit():
            equa2[i]='./'
        equa1=''.join(equa2)
        i=equa1.find('/',i+2,)

#定义stanpow函数将指数格式规范为Python算式的指数格式    
def stanpow():
    global equa1
    equa1=equa1.replace('^','**')

#定义stanmul函数将省略的乘号补回来     
def stanmul():
    i=equa1.find('(')
    global equa1
    while i!=-1 :
        equa2=list(equa1)
        if i>0 and ( equa1[i-1]==')' or equa1[i-1].isdigit() ) :
            equa2[i]='*('
        equa1=''.join(equa2)
        i=equa1.find('(',i+2,)

#定义stancomp将复数格式转为Python标准复数格式        
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
      
equa0=''
equa1=''
bool0=False
char='_'*60
os.system('cls')
calstart()