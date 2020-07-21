#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tools

# print(tools.__file__)
tools.welcome()  # 欢迎
n = 1
while n:
    password = tools.gen()  # 生成密码列表
    # print(password)  # 打印密码
    print('')
    guess = tools.guess()  # 生成猜测列表
    tools.check(password, guess)  # 检测
    n = int(input('play again? 1/0'))  # 是否重新玩
else:
    print('Bye!')  # 再见


