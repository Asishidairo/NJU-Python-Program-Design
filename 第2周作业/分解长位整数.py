# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 09:37:40 2019

@author: 33400
"""

"""
题目描述
编写程序，输出一个9位的长整数，将其分解为三个三位的基本整数并输出，其中个、十、百位为一个整数，千、万、十万位为一个整数，百万、千万、亿位为一个整数。例如123456789分解成123、456、789。三个整数分行输出。

输入
123456789

输出
123
456
789

样例输入
123456789

样例输出
123
456
789
"""

num = input()
num = str(num)
print(num[:3])
print(num[3:6])
print(num[6:])