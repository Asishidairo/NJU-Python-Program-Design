# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 00:13:16 2019

@author: 33400
"""

"""
题目描述
要求输出国际象棋棋盘。国际象棋（chess）棋盘为正方形，有64个黑白（深色与浅色）相同的格子组成；如下图：

输入
无

输出
输出国际象棋棋盘，白色方格用空格代替，黑色方格用字符 * 代替。
"""

k=0
for i in range(8):
    k^=1
    for j in range(8):
        k^=1
        if k:
            print('*',end='')
        else:
            print(' ',end='')
    print()