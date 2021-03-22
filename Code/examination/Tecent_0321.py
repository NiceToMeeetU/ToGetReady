# coding   : utf-8 
# @Time    : 21/03/21 20:05
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : Tecent_0321.py
# @Software: PyCharm




"""
#coding=utf-8
# 本题为考试单行多行输入输出规范示例，无需提交，不计分。
import sys
for line in sys.stdin:
    a = line.split()
    print(int(a[0]) + int(a[1]))


import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        for v in values:
            ans += v
    print(ans)

"""
import sys
import math

def paymen(n, usage):
    res = [20]
    if n < 2:
        return [20]
    t0 = usage[0]
    count_100 = 1
    count_1000 = 0
    bag_50 = False
    for idx, time in enumerate(usage[1:]):
        if time - t0 <= 100:
            if count_100 < 2:
                res.append(20)
            elif count_100 == 2:
                res.append(10)
                bag_50 = True
            elif count_100 > 2:
                res.append(0)
            count_100 += 1
        elif time - t0 <= 1000:
            if count_1000 < 3:
                res.append(20)
            if count_1000 == 3:
                if bag_50:
                    res.append(10)
                else:
                    res.append(20)
            if count_1000 > 3:
                res.append(0)
            count_1000 += 1
        else:
            count_100 = 0
            count_1000 = 0
            t0 = time
            bag_50 = False
    return res

def stairs(n,u,v,s,t,m):
    """
    x + 2y = n  => x = n - 2y
    sx + ty^2 <= m  => s(n-2y) + ty^2 <=m
    ux + vy = u(n-2y) + vy
    考高中题也太嗨了吧
    """
    if v - 2*u == 0:
        return u * n
    # t*y^2 - 2*s*y + s*n - m <= 0
    # 开口向上，直接求两个根即可
    delta = math.sqrt((-2*s)**2 - 4*t*(s*n-m))

    if v - 2* u> 0:
        y = max(0, (2*s - delta)/(2*t))
        return (v -2*u)*y +u*n
    elif v -2*u <0:
        y = (2*s + delta)/(2*t)
        return (v -2*u)*y +u*n


if __name__ == '__main__':
    # n_in = int(sys.stdin.readline().strip())
    # usage_in = list(map(int, sys.stdin.readline().strip().split()))
    # ans = paymen(n_in, usage_in)
    # for i in ans:
    #     print(i)
    print(stairs(17,3,1,7,6,199))