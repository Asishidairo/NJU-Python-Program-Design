# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 23:59:01 2019

@author: 33400
"""

"""
题目描述
求s=a+aa+aaa+aaaa+aa...a的值，其中a（键盘输入）是一个数字，例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加也由键盘输入控制。

输入
输入（由系统自动完成不需要人工输入）为一行，有两个整数由一个空格隔开，前一个数字代表题目中的a，另一个数字代表有几个数相加。

输出
输出题目中S的值

样例输入
2 5

样例输出
24690

提示
输入语句可使用如下方式：
a, n = [int(x) for x in input().split()]
"""

a,n=[int(x) for x in input().split()]
res,b=0,a
for i in range(n):
    res+=b
    b*=10
    b+=a
print(res)