# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 23:18:11 2019

@author: 33400
"""

"""
题目描述
利用公式C= 5/9×(F-32) 将华氏温度转换成摄氏温度，并产生一张华氏0～300度与对应的摄氏温度之间的对照表（每隔30度输出一次）

输入
无

输出
0 -300华氏度与其对应的摄氏度,一行输出一组华氏度与摄氏度, 华氏度在前,摄氏度在后, 每隔30度输出一次,小数点后保留6位.

样例输出
0 -17.777778
30 -1.111111
60 15.555556
90 32.222222
......
"""

for F in range(0,301,30):
    C= 5/9*(F-32)
    print(F,"%.6f"%C)