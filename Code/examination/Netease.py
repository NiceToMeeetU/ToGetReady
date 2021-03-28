# coding   : utf-8 
# @Time    : 2021/3/27 16:07
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : Netease.py
# @Software: PyCharm


import sys

def manjian(T, y, prices):
    """
    找出数组中子数组的和，使其大于T，找满足条件的最小值
    :param T:
    :param y:
    :param prices:
    :return:
    """
    n = len(prices)
    prices.sort()
    res = []
    path = []
    bingo = []
    def backtrack(idx, curSum) :
        if curSum == T:
            bingo.append(T)
            return
        for i in range(idx, n):
            if curSum < T <= curSum + prices[i]:
                res.append(curSum+prices[i])
                break
            if idx < i and prices[i - 1] == prices[i]:
                continue
            path.append(prices[i])
            backtrack(i + 1, curSum + prices[i])
            path.pop(-1)
    backtrack(0,0)
    if bingo:
        return T - y
    else:
        return min(res) - y



if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())
    y = int(sys.stdin.readline().strip())
    prices = list(map(int, sys.stdin.readline().strip().split()))
    ans = manjian(T, y, prices)
    prices(ans)
