# coding   : utf-8 
# @Time    : 21/03/19 19:02
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : ali.py
# @Software: PyCharm


import sys
from math import sqrt


def prize(n, indexs):
    # res = float("inf")
    tmp = []
    for a in indexs:
        s = int(sqrt(a))
        tmp.append(min(abs(s ** 2 - a), abs((s + 1) ** 2 - a)))
    tmp.sort()
    return sum(tmp[:n // 2])


def card(n, a, b):
    res = float("inf")
    if n < 3:
        return -1

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            if a[i] <= a[j]:
                for k in range(j + 1, n):
                    if a[j] <= a[k]:
                        tmp = b[i] + b[j] + b[k]

                        print(f"{i = },{j=},{k=},{tmp=}")
                        # print(f"{b[i] =}, {b[j]= },{b[k] =}")
                        # print(f"{res=}")
                        res = min(res, tmp)
                    else:
                        continue

            else:
                continue
    return res if res > 0 else - 1


if __name__ == "__main__":
    # 读取第一行的n
    # n = int(sys.stdin.readline().strip())
    # ans = 0
    # for i in range(n):
    #     # 读取每一行
    #     line = sys.stdin.readline().strip()
    #     # 把每一行的数字分隔后转化成int列表
    #     values = list(map(int, line.split()))
    #     for v in values:
    #         ans += v
    # print(ans)
    n = 8
    a = [9, 8, 6, 7, 7, 2, 9, 2]
    b = [9, 1, 10, 8, 6, 4, 8, 6]
    print(card(n,a,b))
