# coding   : utf-8 
# @Time    : 21/09/04 10:58
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 小红书.py
# @Software: PyCharm



# class Solution:
#     def resort(self, h):
#         n = len(h)
#         h.sort()
#         x = []
#         y = []
#         res = 0
#         i = 0
#         j = n - 2
#         x.append(h[-1])
#         y.append(h[-1])
#         while i < j:
#             x.append(h[i])
#             x.append(h[j])
#             if i + 1 > j - 1:  # 避免重复插入
#                 break
#             y.append(h[i + 1])
#             y.append(h[j - 1])
#             j -= 2
#             i += 2
#         if i == j:
#             if abs(h[j] - x[-1]) > abs(h[j] - y[-1]):
#                 x.append(h[j])
#             else:
#                 y.append(h[j])
#         for i in range(0, len(x) - 1):
#             res += abs(x[i] - x[i + 1])
#         for i in range(0, len(y) - 1):
#             res += abs(y[i] - y[i + 1])
#         return res
#
#
# if __name__ == '__main__':
#     solution = Solution()
#     n = int(input().strip())
#     a = list(map(int, input().strip().split()))
#     ans = solution.resort(a)
#     print(ans)


import numpy as np

res = []
for _ in range(1000000):
    a = np.random.random()
    b = np.random.random()
    res.append(abs(a - b))
print(np.average(res))