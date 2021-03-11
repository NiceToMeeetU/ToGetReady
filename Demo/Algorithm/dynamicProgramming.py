# coding   : utf-8 
# @Time    : 21/03/10 10:54
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : dynamicProgramming.py
# @Software: PyCharm


"""
动态规划问题
一种算法思想：若要解一个给定问题，我们需要解其不同部分（即子问题），再根据子问题的解以得到原问题的解。
- 子问题与原问题的关系 对应最优子结构问题
- 子问题之间的关系  对应重复子问题


考虑能否将问题规模缩小：
- 数组上常用思路：
    - 每次减少一半
    - 每次减少一个

问题解法从三个方向考虑选择：
- 递归
- top-down 记忆化
- bottom-up 迭代

动态规划和其他算法的区别
- 动态规划有子问题【重复】出现，分治的子问题不会重复出现
- 贪心：每一步的最优解一定包含上一步的最优解，上一步之前的最优解无需记录
- 动态规划：全局最优解中一定包含某个局部最优解，但不一定包含上一步的局部最优解，因此需要记录之前的所有的局部最优解

　　算法        分治      动规        贪心
适用类型        通用      优化        优化
　子问题     每个都不同   有很多重复    只有一个
最优子结构   没有要求      必须满足    必须满足
子问题数     全部都要解   全部都要解  只解一个



"""

from typing import List


class Stock:
    """
    买卖股票问题
    """

    def maxProfit(self, prices: List[int]) -> int:
        """
        121. 买卖股票的最佳时机
        k = 1
        """
        # 一次遍历
        minPrice = int(1e9)
        maxProfit = 0
        for p in prices:
            maxProfit = max(maxProfit, p - minPrice)
            minPrice = min(minPrice, p)
        # return maxProfit

        # 初步动规
        dp = [[0, 0]] * len(prices)
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], -prices[i])
        # return dp[-1][0]

        # 空间优化动规
        n = len(prices)
        dp_i_0 = 0
        dp_i_1 = float("-inf")
        for i in range(n):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, -prices[i])
        return dp_i_0

    def maxProfit2(self, prices: List[int]) -> int:
        """
        122. 买卖股票的最佳时机Ⅱ
        k = inf
        """
        dp = [[0, 0]] * len(prices)
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        # return dp[-1][0]

        # 优化一下
        n = len(prices)
        dp_i_0 = 0
        dp_i_1 = float("-inf")
        for i in range(n):
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, tmp - prices[i])
        return dp_i_0

    def maxProfit3(self, prices: List[int]) -> int:
        """
        123. 买卖股票的最佳时机Ⅳ
        k = 2
        """
        max_k = 2
        n = len(prices)
        dp = [[[0, 0]] * (max_k + 1)] * n
        for i in range(n):
            for k in range(max_k + 1):
                if i > 0:
                    dp[i][k][0] = max()
                else:   # base case
                    dp[0][k][0] = 0
