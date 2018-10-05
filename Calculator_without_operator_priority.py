# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 22:58:16 2018

@author: SUBIN
"""

def add(x,y):
    return x+y

def minus(x,y):
    return x-y

def mult(x,y):
    return x*y

def divi(x,y):
    return x/y

def calculate(values):
    d=0
    x=0
    y=0
    z=""
    for c in range(len(values)):
        if(c%2==0 and d==0):
            x=values[c]
            d=d+1
        if(c%2==0 and d==2):
            y=values[c]
            d=d+1
        if(c%2!=0 and d==1):
            z=str(values[c])
            d=d+1
        if(c%2!=0 and d==3):
            if(z=="+"):
                x=add(x,y)
            elif(z=="-"):
                x=minus(x,y)
            elif(z=="*"):
                x=mult(x,y)
            elif(z=="/"):
                x=divi(x,y)
            z=str(values[c])
            d=2
    return x


calculator=input("식 입력 : ")

value=""
number=[]

for a in range(len(calculator)):
    if(calculator[a]!="+" and calculator[a]!="-" and calculator[a]!="*" and calculator[a]!="/" and calculator[a]!="="):
        value=value+str(calculator[a])
    elif(calculator[a]=="+" or calculator[a]=="-" or calculator[a]=="*" or calculator[a]=="/"):
        if(value!=""):
            value=int(value)
            number.append(value)
            number.append(calculator[a])
            value=""
        elif(value==""):
            print("ERROR")
            break;
    elif(calculator[a]=="="):
        if(value!=""):
            value=int(value)
            number.append(value)
            number.append(calculator[a])
            print("number=",number)
            print(calculator,calculate(number))
        elif(value==""):
            print("ERROR")
            break;