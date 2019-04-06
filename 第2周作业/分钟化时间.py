# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 09:56:49 2019

@author: 33400
"""

"""
题目描述
编写程序，从键盘输入分钟数（例如1000000），输出这些分钟代表多少年零多少天零多少小时零多少分钟。为了简化问题，假设一年有365天。输出格式为：xxyears xxdays xxhours xxmins

输入
10000000

输出
19years 9days 10hours 40mins

样例输入
10000000

样例输出
19years 9days 10hours 40mins

提示
输出时可使用print('{}years {}days {}hours {}mins'.format(x,y,z,w))。
"""

mins = int(input())
years = mins//(60*24*365)
mins %= 60*24*365
days = mins//(60*24)
mins %= 60*24
hours = mins//(60)
mins %= 60
print('%dyears %ddays %dhours %dmins'%(years,days,hours,mins))