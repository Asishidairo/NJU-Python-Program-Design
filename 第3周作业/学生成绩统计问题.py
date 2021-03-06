"""
题目描述
列表中存放了某次考试学生的考试成绩，请编写程序分别求出不及格学生和甲等（大于85）学生的平均成绩。（数据中肯定存在各一名成绩为85和60的学生，结果分行输出且保留两位小数）

输入
85,55,93,75,56,47,67,90,24,88,60

输出
45.50
90.33

样例输入
85,55,93,75,56,47,67,90,24,88,60

样例输出
45.50
90.33
"""

s = list(eval(input()))
bad = list(filter(lambda x:x<60,s))
print('%.2f'%(sum(bad)/len(bad)))
good = list(filter(lambda x:x>85,s))
print('%.2f'%(sum(good)/len(good)))