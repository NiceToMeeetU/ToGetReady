# coding   : utf-8 
# @Time    : 21/03/28 9:04
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : Microsoft_0328.py
# @Software: PyCharm

import random


def solution(D, C, P):
    """
    :param D: K-th object's distance from the player.
    :param C: K-th object's processing power cost required to render it
    :param P: most processing power
    :return: the maximum number of objects that can be rendered with the Distance, Cost, Power given.
    Time complexity: O(nlogn^2)
    Space complexity: O(1)
    这种写法需要做两重排序，时间复杂度太高，
    """
    # Merge D and C to sort them.
    # We choose the object with smaller cost when the distance is same.
    if len(C) != len(D):
        print("Please check parameters.")
    DC = sorted(zip(D, C), key=lambda x: (x[0], x[1]))
    for i in range(len(DC)):
        P -= DC[i][1]
        if P < 0:
            return i
    return len(DC)


# import numpy as np
#
# D = np.random.randint(1, 1000000000, size=100000)
# C = np.random.randint(1, 1000000000, size=100000)
# P = 4561214635
# ans = solution(D, C, P)
# print(ans)


def solution2(A, M):
    """
    计划使用【鸽巢原理】配合【动态规划】求解
    :param A: 数组
    :param M: 需要取模的值
    :return: 满足条件的最大子数组长度
    所有的两两组合都需要遍历一遍，所以时间复杂度上O(n^2)需要重点关注
    构造辅助数组空间换时间！
    """
    n = len(A)
    # 构造辅助数组 B, 其中：b_1 = a_1 - a_2,..., b_i-1 = a_i-1 - a_i
    # 这样，原数组A中任意两数之差 a_i - a_j ( 1<= i,j <= n) 可以表示成B中d第i个到第j-1个元素的连续求和

    B = [A[i] - A[i + 1] for i in range(n - 1)]
    print(B)
    # 利用动态规划求解
    # dp: n * n
    # dp[i][j] 表示第i个点到第j个点的距离对 M 取余是否为零
    dp = [[False for _ in range(n)] for _ in range(n)]

    res = dict()
    for i in range(n):
        for j in range(i + 1, n):
            if (A[i] - A[j]) % M == 0:
                res[i] = res.get(i, 0) + 1
                res[j] = res.get(j, 0) + 1


    max_val = max(res.values())
    return sum


A = [-3,-2,1,0,8,7,1]
M = 3
ans = solution2(A, M)