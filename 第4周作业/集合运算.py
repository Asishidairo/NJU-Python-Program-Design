"""
题目描述
设有集合A和B:
A={'red','blue','yellow','green','white','black'}
B={'green','purple','yellow','pink'}
求这两个集合的并集、差集（两种情况都要输出，先A-B）、交集和对称差分，并按ASCII码顺序，分行输出。

输入
无

输出
['black', 'blue', 'green', 'pink', 'purple', 'red', 'white', 'yellow']
['black', 'blue', 'red', 'white']
['pink', 'purple']
['green', 'yellow']
['black', 'blue', 'pink', 'purple', 'red', 'white']

样例输出
['black', 'blue', 'green', 'pink', 'purple', 'red', 'white', 'yellow']
​['black', 'blue', 'red', 'white']​
['pink', 'purple']
['green', 'yellow']
['black', 'blue', 'pink', 'purple', 'red', 'white']​

提示
以列表的形式输出
"""

A={'red','blue','yellow','green','white','black'}
B={'green','purple','yellow','pink'}
print(sorted(A|B))
print(sorted(A-B))
print(sorted(B-A))
print(sorted(A&B))
print(sorted(A^B))
