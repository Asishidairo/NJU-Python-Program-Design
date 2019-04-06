"""
题目描述
给出一个字符串，字符串中可能包含'A'-'Z','a'-'z',' '(空格)等字符。输出字母a（包括大小写）出现的次数。

输入
abc&ABC

输出
2

样例输入
abc&ABC

样例输出
2

提示
输入将由oj自动完成，可用string = input()表示
"""

string = input()
print(string.count('a')+string.count('A'))