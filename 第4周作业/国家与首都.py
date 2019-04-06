"""
题目描述
自行创建字典储存国家与首都对，如下（可增加不可删减）：
国家名            首都
China              Beijing
America          Washington
Japan             Tokyo
Canada           Ottawa
Thailand         Bangkok
Norway          Oslo
Germany        Berlin
France           Paris
编写程序输入一个国家名后，显示该国家的首都，首都首字母需大写。

输入
China

输出
Beijing

样例输入
China

样例输出
Beijing
"""

x={'China':'Beijing','America':'Washington','Japan':'Tokyo','Canada':'Ottawa',
   'Thailand':'Bangkok','Norway':'Oslo','Germany':'Berlin','France':'Paris'}
y=input()
print(x[y].title())
