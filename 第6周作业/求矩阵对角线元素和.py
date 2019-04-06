# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 21:32:26 2019

@author: 33400
"""

"""
题目描述
求矩阵的两对角线上的元素之和

输入
矩阵的行数N 
和一个N*N的整数矩阵a[N][N](N<=10)

输出
所输矩阵的两对角线上的元素之和

样例输入
3
1 2 3 
4 5 6 
7 8 9

样例输出
25
"""

n=int(input())
m=0
for k in range(n):
    s=input().split()
    if k==n-1-k:
        m+=int(s[k])
    else:
        m+=int(s[k])+int(s[n-1-k])
print(m)