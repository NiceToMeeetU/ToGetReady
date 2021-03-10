# coding   : utf-8 
# @Time    : 21/03/10 8:45
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0310.py
# @Software: PyCharm


from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        300. 最长递增子序列
        给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
        子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。
        例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
        """
        if not nums:
            return 0
        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def climb(self, n: int) -> int:
        """
        70. 爬楼梯问题
        一次只能爬一步或者两步，一共n阶台阶
        转移方程 f(i) = f(i - 1) + f(i - 2)
        """
        dp = {1: 1, 2: 2}
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    def minSwap(self, A: List[int], B: List[int]) -> int:
        """
        801. 使序列递增的最小交换次数
        我们有两个长度相等且不为空的整型数组A和B。
        我们可以交换A[i]和B[i]的元素。
        注意这两个元素在各自的序列中应该处于相同的位置。
        在交换过一些元素之后，数组A和B都应该是严格递增的
        （数组严格递增的条件仅为A[0] < A[1] < A[2] < ... < A[A.length - 1]）。
        给定数组A和B，请返回使得两个数组均保持严格递增状态的最小交换次数。
        假设给定的输入总是有效的。
        :param A:
        :param B:
        :return:
        每次交换应该只跟当前这个点相关，之前的不用动？

        """
        dp = [[0, 0]] * len(A)
        dp[0][0] = 0
        dp[0][1] = 1
        for i in range(1, len(A)):
            # 可能的情况
            # - 已经各自有序
            # - 存在交叉
            # - 既有序，也交叉
            if A[i - 1] < A[i] and B[i - 1] < B[i]:
                if A[i - 1] < B[i] and B[i - 1] < A[i]:
                    dp[i][0] = min(dp[i-1][0], dp[i-1][1])
                    dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + 1
                else:
                    dp[i][0] = dp[i -1][0]

    def calculate(self, s: str) -> int:
        """
        224. 基本计算器
        实现一个基本的计算器来计算一个简单的字符串表达式 s 的值。
        :param s:
        :return:
        """



if __name__ == '__main__':
    pass
