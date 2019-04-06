# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 23:34:30 2019

@author: 33400
"""

"""
题目描述
输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。

输入
输入是一行，有多个整数，每个整数之间用空格隔开。

输出
输出元素交换过的列表。

样例输入
1 2 3 7 9 8

样例输出
[9, 2, 3, 7, 8, 1]
"""

s=input().split(' ')
s=list(map(int,s))
i=s.index(max(s))
s[0],s[i]=s[i],s[0]
j=s.index(min(s))
s[-1],s[j]=s[j],s[-1]
print(s)