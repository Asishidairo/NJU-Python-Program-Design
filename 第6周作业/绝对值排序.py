# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 21:19:04 2019

@author: 33400
"""

"""
题目描述
输入n(n<=100)个整数，按照绝对值从大到小排序后输出。题目保证对于每一个测试实例，所有的数的绝对值都不相等。

输入
首先输入一个整数代表有多少组，每组占一行，每行有若干个整数用空格彼此隔开

输出
对于每个每行的测试实例，输出排序后的结果，两个数之间用一个空格隔开（注意每行最后一个数的结尾也有空格）。每个测试实例占一行

样例输入
2
3 -4 2
0 1 2 -3

样例输出
-4 3 2
-3 2 1 0
"""

n=int(input())
for i in range(n):
    s=list(map(int,input().split()))
    s.sort(key=abs,reverse=True)
    s=list(map(str,s))
    print(" ".join(s))