# coding   : utf-8 
# @Time    : 21/03/20 15:57
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : Meituan_0320.py
# @Software: PyCharm


import sys


def duty(n, m, a):
    yesterday, today = 1, 2
    # m = m % n
    # if m == 1:
    #     return yesterday
    # elif m == 2:
    #     return today
    # elif m == 0:
    #     m = n
    for i in range(2, m):
        tomorrow = a[today - 1][yesterday - 1]
        print(i+ 1, tomorrow)
        yesterday, today = today, tomorrow

    return tomorrow


if __name__ == '__main__':
    # tmp = list(map(int, sys.stdin.readline().strip().split()))
    # n_in, m_in = tmp[0], tmp[1]
    # a_in = []
    # for _ in range(n_in):
    #     lines = list(map(int, sys.stdin.readline().strip().split()))
    #     a_in.append(lines)

    n_in = 3
    m_in = 50
    # a_in = [[0, 3, 2], [3, 0, 3], [2, 1, 0]]
    a_in = [[0, 3, 2], [3, 0, 1], [2, 1, 0]]
    ans = duty(n_in, m_in, a_in)
    print(ans)
