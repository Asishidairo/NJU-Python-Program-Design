# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 23:22:07 2019

@author: 33400
"""

"""
题目描述
输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

输入
输入为一行字符

输出
输出统计各种种类字符的个数，第一行输出英文字母的个数，第二行输出空格的个数，第三行输出数字字符的个数，第四行输出其他字符的个数

样例输入
a 1?

样例输出
1
1
1
1
"""

s=input()
a,b,c,d=0,0,0,0
for ch in s:
    if ch.isalpha():
        a+=1
    elif ch.isspace():
        b+=1
    elif ch.isdigit():
        c+=1
    else:
        d+=1
print(a,b,c,d,sep='\n')