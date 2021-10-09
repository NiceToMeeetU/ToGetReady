# coding   : utf-8 
# @Time    : 21/09/12 9:53
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0912字节.py
# @Software: PyCharm


# class Solution:
#     def scores(self, nums):
#         if not nums:
#             return 0
#         n = len(nums)
#         if n == 1:
#             return nums[0][1]
#         res = 0
#         nums = sorted(nums, key=lambda x: (x[0], -x[1]))
#         i, j = 0, 1
#         start = 0
#         while j < n:
#             if nums[j][0] == nums[i][0]:
#                 start += 10
#                 res += nums[i][1]
#             if nums[j][0] - nums[i][0] >= 10:
#                 res += nums[i][1]
#                 i = j
#                 j
#
#
#
#
#         return res
#
#
# if __name__ == '__main__':
#     solution = Solution()
#     N = int(input().strip())
#     nums_ = []
#     for _ in range(N):
#         nums_.append(list(map(int, input().strip().split())))
#
#     nums_ = [[20,5], [30,10], [25, 8], [15,15]]
#     print(solution.scores(nums_))


# import math
#
# res = 0
# for i in range(0, 100):
#     res +=  i / (2**i)
#
# print(res)


# import numpy as np
#
# a = np.repeat(np.arange(5).reshape([1, -1]), 10, axis = 0) + 10.0
# b = np.random.randint(5,size=a.shape)
# c = np.argmin(a*b, axis = 1)
# b = np.zeros(a.shape)
# b[np.arange(b.shape[0]), c] = 1
# print(b)
#
#
# def factorial_1(n):
#     """
#     递归求阶乘
#     """
#     if n == 0:
#         return 1
#     elif n < 0:
#         print("负数不可计算阶乘")
#         return
#     else:
#         return n * factorial_1(n - 1)
#
# def factorial_2(:
#     """
#     迭代求阶乘
#     """
#     res = 1
#     if n < 0:
#         print("负数不可计算阶乘")
#         return
#     for i in range(n):
#         res *= n
#
#     return res
#
# def factorial_3(n):
#     """直接求"""
#     import math
#     return math.factorial(n)
#