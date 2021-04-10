# coding   : utf-8 
# @Time    : 21/04/10 18:53
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : JD_0410.py
# @Software: PyCharm

# import sys
# class Solution:
#     def trieSet(self, nums):
#         """
#         前缀集合的权值 = 前缀末尾下标与前缀集合中元素数量的乘积
#         :param nums: 整数数组
#         :return: 所有前缀集合的权值和
#         """
#         res = 0
#         sets = set()
#         j = 0
#         for i in range(1, len(nums) + 1):
#             if nums[i - 1] not in sets:
#                 j += 1
#             res += i*j
#             sets.add(nums[i - 1])
#             # print(f"{i=}, {j=}, {res=}")
#         return res
#
# if __name__ == '__main__':
#     solution = Solution()
#     n_ = int(sys.stdin.readline().strip())
#     nums_ = list(map(int, sys.stdin.readline().strip().split()))
#     ans = solution.trieSet(nums_)
#     print(ans)
#     # print(solution.trieSet([1,3,2,3,6]))


###################
# import sys
#
#
# class Solution:
#     def bigWatermelon(self, n, nums):
#         """
#         合成大西瓜
#         dp[n] = dp[n - 1] + 1 if nums[n] == stack_left[-1] or nums[n] == stack_right[-1] else 0
#         dp[0] = 0
#         dp[1] = 0
#
#         :param n: 序列长度
#         :param nums: 数组
#         :return: 最大得分
#         """
#         stack_left = [nums[0]]  # 让第一个数字直接落在左侧
#         stack_right = []
#         dp = [0] * n
#
#         for i in range(1, n):
#             if stack_left and stack_left[-1] == nums[i]:
#                 dp[i] = dp[i - 1] + 1
#             elif stack_right and stack_right[-1] == nums[i]:
#                 dp[i] = dp[i - 1] + 1
#             elif stack_left and i + 1 < n and stack_left[-1] == nums[i + 1]:
#                 stack_right.append(nums[i])
#             elif stack_right and i + 1 < n and stack_right[-1] == nums[i + 1]:
#                 stack_left.append(nums[i])
#             elif len(stack_left) < len(stack_right):
#                 stack_left.append(nums[i])
#             else:
#                 stack_right.append(nums[i])
#         return dp[-1]
#
#
#
# if __name__ == '__main__':
#     solution = Solution()
#     # n_ = int(sys.stdin.readline().strip())
#     # nums_ = list(map(int, sys.stdin.readline().strip().split()))
#     # ans = solution.bigWatermelon(nums_)
#     # print(ans)
#     print(solution.bigWatermelon(6, [1, 2, 3, 1, 2, 2]))


import sys
def regex(strs):
    res = ""


    return res

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    strs_in = []
    for _ in range(n):
        line = sys.stdin.readline().strip()
        strs_in.append(line)

    ans = regex(strs_in)
    print(ans)
