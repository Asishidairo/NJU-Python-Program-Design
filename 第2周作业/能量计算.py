# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 10:06:41 2019

@author: 33400
"""

"""
题目描述
编写程序，输入水的质量以及水的初始温度和最终温度，计算并输出将水从初始温度加热到最终温度所需的能量。
计算能量的公式为：
Q=M*(最终温度-初始温度)*4184
其中M是以千克为单位的水的质量，温度以摄氏度为单位，能量以焦耳为单位。

输入
50 10 100

输出
18828000.0

样例输入
10 50 100

样例输出
2092000.0

提示
输入可使用x = input().split()
m = float(x[0])
fint = float(x[1])
orit = float(x[2])
再将每一个元素转换成float类型
"""

x = input().split()
m = float(x[0])
fint = float(x[1])
orit = float(x[2])
energy = m * (orit - fint) * 4184
print(energy)