"""
题目描述
创建一个字典，键保存用户名'dazhuang'，密码为'233'，用户名和密码对不限于此，但必须包括上述键值对。设计一个登录检查程序，只有用户名和密码都正确的用户才能登录，登录成功则显示'Yes!’,登录失败则显示‘Wrong!'

输入
dazhuang,233

输出
Yes!

样例输入
dazhuang,233

样例输出
Yes!
"""

data={'dazhuang':'233'}
a=input().split(',')
name=a[0]
pwd=a[1]
if name in data and data[name]==pwd:
    print('Yes!')
else:
    print('Wrong!')
