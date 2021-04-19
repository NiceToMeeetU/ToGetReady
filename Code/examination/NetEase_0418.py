# coding   : utf-8 
# @Time    : 21/04/18 15:00
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : NetEase_0418.py
# @Software: PyCharm


import sys

#
# class Solution:
#     def subArray(self, s, t):
#         res = len(t)
#         l1, l2 = len(s), len(t)
#         i, j = 0, 0
#         idx = [0] * l1
#
#         t_idx = dict()
#         for i, c in enumerate(t):
#             tmp = ord(c) - ord("a")
#             t_idx[tmp] = min(i, )
#             a
#         for i in range(l1):
#
#         while i < l1 and j < l2 and i + j < l1:
#             if s[i] < t[j]:
#                 res = max(res, l1 + l2 - i - j)
#                 break
#             j += 1
#
#         return res
#
#
# if __name__ == "__main__":
#     s = sys.stdin.readline().strip()
#     t = sys.stdin.readline().strip()
#     q = int(sys.stdin.readline().strip())
#     query = []
#     for _ in range(q):
#         i, j = list(map(int, sys.stdin.readline().strip().split()))
#         query.append([i, j])
#
#     s = "abcd"
#
#     solution = Solution()
#     for i, j in query:
#         ans = solution.subArray(s[i - 1:], t[j - 1:])
#         print(ans)

s = "abcd"
t = "adcb"

t_idx = dict()
for i,c in enumerate(t):
    tmp = ord(c) - ord("a")
    if tmp not in t_idx:
        t_idx[tmp] = i

s = [ord(c) - ord("a") for c in s]