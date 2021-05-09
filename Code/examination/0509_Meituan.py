# coding   : utf-8 
# @Time    : 21/05/09 9:59
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0509_Meituan.py
# @Software: PyCharm


import sys


def func(x, a, b, n):  # 改名字
    res = 0
    if n == 0:
        return 0
    # if a == b:
    #     return x + a * n

    status_practice = [x - a if x > a else 0] + [0] * (n - 1)  # 第i天练习的状态值
    status_rest = [x + b] + [0] * (n - 1)  # 第i天休息的状态值

    gain_practice = [x] + [0] * (n - 1)  # 第i天练习的收益
    gain_rest = [0] * n     # 第i天休息的收益


    for i in range(1, n):
        status_practice[i] = max(status_rest[i - 1] - a, status_practice[i - 1] - a)
        status_rest[i] = max(status_rest[i - 1] + b, status_practice[i - 1] + b)
        gain_rest[i] = max(gain_rest[i - 1], gain_practice[i - 1])
        gain_practice[i] = max(gain_rest[i - 1], gain_practice[i - 1]) + max(status_rest[i], status_practice[i])
        gain[i] = max()

    print(f"{status_practice = }")
    print(f"{status_rest = }")
    print(f"{gain_rest = }")
    print(f"{gain_practice = }")
    return max(gain_rest[-1], gain_practice[-1])


if __name__ == '__main__':
    # t = int(sys.stdin.readline().strip())
    # for _ in range(t):
    #     x, a, b, n = list(map(int, sys.stdin.readline().strip().split()))
    #     ans = func(x, a, b, n)
    #     print(ans)
    print(func(10,5,5,3))
