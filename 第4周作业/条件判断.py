"""
题目描述
输入一个测验成绩，根据下面的标准，输出他的评分成绩（A-F）。 A: 90–100 B: 80–89 C: 70–79 D: 60–69 F: <60 

输入
从标准输入流读入一个整数

输出
输出一个字符表示该成绩所属于的等级

样例输入
85

样例输出
B
"""

x=int(input())
if x<60:
    print('F')
elif x<70:
    print('D')
elif x<80:
    print('C')
elif x<90:
    print('B')
elif x<101:
    print('A')
