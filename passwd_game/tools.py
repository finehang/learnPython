#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random


def welcome():  # 欢迎模块
    print('★' * 25)
    print('欢迎游玩'.center(46, '*'))
    print('本游戏将随机生成六位不重复密码'.center(35, '*'))
    print('你有六次猜测机会'.center(42, '*'))
    print('请根据提示猜测'.center(43, '*'))
    print('游戏愉快!'.center(46, '*'))
    print('★' * 25)
    print('')
    print('')


def gen():  # 密码生成模块
    p = list(range(0, 10))
    random.shuffle(p)  # 打乱列表
    for i in range(0, 4):
        p.remove(random.choice(p))  # 从p列表中随机挑出一个数,并从p列表中去除
    print('密码已生成:******')
    return p


def guess():  # 猜测列表生成模块
    g = input('Guess Password\n')
    if g == '666666':
        print('hehe, Nice Try')  # 彩蛋^_^
    n = 1
    while n == 1:
        if len(g) != 6:  # 位数限制,不是6位则要求重新输入
            print('位数不对, try again!')
            g = input('Guess Again\n')
        else:
            a = 0
            for i in range(0, 6):  # 重复检查,有重复则要求重新输入
                a += g.count(g[i])  # 不重复请况下,每个元素出现次数之和最大为6
            if a > 7:  # 和大于7,则必定有重复
                print('禁止重复!')
                g = input('Guess Again\n')
            else:
                n = 0  # 位数为6且无重复结束循环
    g = [int(i) for i in g]  # 将字符串转化为g猜测列表
    return g


def check(p, g):  # 检测模块,接收p密码列表和g猜测列表
    i = 1
    while i <= 6:  # 限定次数,6次机会
        if p == g:  # 猜中
            for i in range(0, 10):
                print('Bingo! You Win!!'.center(50, '*'))  # 庆祝~
            print('The password is', p)  # 输出答案
            print('')
            print('')
            print('★' * 25)
            print('  MADE BY fanxiaohang   '.center(37, '★'))
            print('  DATE: 2020.07.18  '.center(35, '★'))
            print('Best wishes  for you'.center(35, '★'))
            print('★' * 25)
            print('')
            print('')
            return
        else:
            tips(g, p)  # 输出提示信息
            print('你还有%d次机会' % int(6 - i))
            if i == 6:  # i=6时,次数已用完,强行结束
                i = 7
            else:
                g = guess()  # 重新猜测
                i += 1
    else:
        print('The password is', p)  # 机会用完,结束检查
        print('密码已重置')


def tips(g, p):  # 提示模块
    for i in range(0, 6):
        if g[i] == p[i]:  # g表和p表逐位对比,相同输出正确
            print('第%d位:正确' % int(i + 1))  # 列表从0开始
        elif g[i] in p:  # 不同但p表存在
            print('第%d位:位置错误' % int(i + 1))
        else:  # 不同且p表也不存在
            print('第%d位:数字不存在' % int(i + 1))

