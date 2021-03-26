# coding   : utf-8 
# @Time    : 21/03/26 19:30
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : Ali_03266.py
# @Software: PyCharm



"""
现有n张卡牌排成一排，每一个卡牌上面有一个0或1
现在小明必须选择其中一个卡牌并移除掉，移除后，可以拿走任意长度的连续的全为1的卡牌
求所有可能的方案中，能拿走的最多的卡牌数

每一个文件输入第一行一个整数 T ， 代表T组测试数据
接下来T组，每一组每一行输入一个整数n 代表卡牌的数量
接下来输入n个数， a[i] 代表每一张卡牌的数字
数据保证每一个文件内的n的总和不超过最大范围

"""


import sys

def cards(nums):
    idx = 0
    tmp = []

    while idx != -1:
        try:
            idx = nums.index(0, idx + 1)
            tmp.append(idx)
        except ValueError:
            break
    tmp = [0] + tmp + [len(nums)]
    print(tmp)
    for i in range(len(tmp)):
        pass



if __name__ == '__main__':
    # test()
    T = int(sys.stdin.readline().strip())
    res = []
    for _ in range(T):
        n = int(sys.stdin.readline().strip())
        nums = list(map(int, sys.stdin.readline().strip().split()))
        ans = cards(n, nums)
        res.append(ans)

    for i in res:
        print(i)