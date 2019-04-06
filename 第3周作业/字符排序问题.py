"""
题目描述
编写程序，将给定的字符串序列，按照字符ASCII码顺序从小到大排序后输出。

输入
aABcd

输出
ABacd

样例输入
aABcd

样例输出
ABacd
"""

string = input()
print(''.join(sorted(string)))