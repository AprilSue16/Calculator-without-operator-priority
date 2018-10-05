# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 16:36:18 2018

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

def calculate(values):#리스트번호가 짝수이면 숫자, 홀수이면 연산자임을 이용
    d=0#숫자와 연산자 계산이 어떻게 이루어져야 되는지 구분하기 위해 사용
    x=0#숫자를 집어넣기 위해 초기화
    y=0#숫자를 집어넣기 위해 초기화
    z=""#연산자를 집어넣기 위해 초기화
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


calculator=input("input : ") #식 입력받기

value="" #문자열 공백으로 초기화
number=[] #리스트 초기화

for a in range(len(calculator)):
    if(calculator[a]!="+" and calculator[a]!="-" and calculator[a]!="*" and calculator[a]!="/" and calculator[a]!="="):#연산자가 아닌지 판별
        value=value+str(calculator[a])#문자열에 추가
    elif(calculator[a]=="+" or calculator[a]=="-" or calculator[a]=="*" or calculator[a]=="/"):#연산자인지 판별
        if(value!=""):#문자열이 공백이 아닐 때
            value=int(value)#문자열을 정수형으로 변환
            number.append(value)#리스트에 숫자를 입력
            number.append(calculator[a])#리스트에 연산자를 입력
            value=""#문자열을 공백으로 초기화
        elif(value==""):#문자열이 공백일 때
            print("ERROR")
            break;
    elif(calculator[a]=="="):#"="인지 판별
        if(value!=""):#문자열이 공백이 아닐 때
            value=int(value)#문자열을 정수형으로 변환
            number.append(value)#리스트에 숫자를 입력
            number.append(calculator[a])#리스트에 연산자"="을 입력
            print("number=",number)
            print(calculator,calculate(number))#식을 계산하는 함수
        elif(value==""):#문자열이 공백일 때
            print("ERROR")
            break;
            
            
            