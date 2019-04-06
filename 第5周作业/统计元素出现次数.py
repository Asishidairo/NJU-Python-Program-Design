# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 00:03:04 2019

@author: 33400
"""

"""
题目描述
利用Python中的random模块生成1000个0到100之间的随机整数，并统计每个元素的出现次数。为了保持测试数据的一致性，代码中利用random模块生成1000个数据时需要像如下形式：
import random
random.seed(0)
x=[random.randint(0,100) for i in range(1000)]
请在编写代码时按照上面的方式生成数据

输入
无

输出
输出每种元素的统计个数，每行一个按照元素从小到大的顺序从上到下输出，中间用一个空格隔开。输出格式（非内容）如下：
0 3
1 5
...
表示元素0出现3次，1出现5次等等。
"""

import random
random.seed(0)
x=[random.randint(0,100) for i in range(1000)]
for i in range(101):
    print(i,x.count(i))