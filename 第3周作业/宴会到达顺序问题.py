"""
题目描述
小张举办生日宴会，请帮助小张编写一段程序，由外部输入所有出席宴会的好友的姓名包括小王、小李、小赵、小钱等，并将姓名存到一个列表中。宴会结束后，如果想知道小王是第几个到达宴会的客人，请输出该数字。

输入
xiaozhang,xiaowang,xiaoli,datou,erbao

输出
2

样例输入
xiaozhang,xiaowang,xiaoli,datou,erbao

样例输出
2

提示
请用lst = input().split(',')表示输入
"""

s = input().split(',')
print(s.index('xiaozhang')+1)