# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 21:05:12 2019

@author: 33400
"""

"""
题目描述
采用递推法计算sinx幂级数展开式的近似值，当通项绝对值小于10-8时停止累加，保留1位小数。
sinx=x/1-x3/3!+x5/5!-x7/7!…

输入
在程序中用x = float(input())表示输入，x由系统自动输入（无需人工输入）

样例输入
3.1415926

样例输出
0.0
"""

res=0
x=float(input())
term=x
i=1
while abs(term)>1e-8:
    res+=term
    term*=-x*x/(i+1)/(i+2)
    i+=2
print("%.1f"%res)