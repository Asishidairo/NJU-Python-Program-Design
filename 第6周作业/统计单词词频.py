# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 21:40:59 2019

@author: 33400
"""

"""
题目描述
从键盘输入一个英文句子，除单词和空白字符（包括空格和换行符等）外句子中只包含","、"."、" ' "、" " "和"!"几个标点符号，统计句子中包括的每个单词（将句中大写全部转换成小写）的词频并将结果保存在字典中，先按词频从小到到输出，再按键进行排序。

输入
This is a sentence a.

输出
is 1
sentence 1
this 1
a 2
"""
s=input()
for c in ",.\'\"!":
    s=s.replace(c," ")
s=s.lower().split()
d={}
for w in s:
    if w in d:
        d[w]+=1
    else:
        d[w]=1
for it in sorted(d.items(),key=lambda x:(x[1],x[0])):
    print(it[0],it[1])