# coding   : utf-8 
# @Time    : 21/03/26 19:03
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : Ali_0326.py
# @Software: PyCharm


"""
你与牛牛，牛妹一起去S国旅行，在目的地周围一共有n家酒店
这n家酒店之间通过 n - 1 条道路联通，每两家酒店之间存在一条唯一路径
由于你们每个人都有自己偏好的酒店，于是，你们决定各自选择酒店入住。
第二天一早，再到某一酒店集合，集合的可以不是三个人住的酒店
由于你很聪明，所选的集合点必定是的三个人抵达该酒店的距离之和最小
已知每个人的偏好酒店清单，并且每个人偏好的酒店被选择的概率相同
那么，第二天一早，三个人各自前往集合点的最短路径之和的期望是多少。
第一行 一个正整数 n 代表酒店个数
接下去 n - 1 行每行三个正整数，a, b, c， 代表a与b酒店之间的道路距离为c
最后三行，每行代表一位旅行者的偏好酒店清单，首先输入一个正整数k，然后是k个偏好酒店编号
"""


import sys

def bestHotel(n, paths, h1, h2, h3):
    res= 0



    return res

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    paths = []
    for _ in range(n - 1):
        tmp = list(map(int, sys.stdin.readline().strip().split()))
        paths.append(tmp)

    h1 = list(map(int, sys.stdin.readline().strip().split()))
    h2 = list(map(int, sys.stdin.readline().strip().split()))
    h3 = list(map(int, sys.stdin.readline().strip().split()))

    ans = bestHotel(n, paths, h1, h2, h3)
    print(ans)

