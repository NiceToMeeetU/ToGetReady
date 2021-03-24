# coding   : utf-8 
# @Time    : 21/03/10 10:54
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : DynamicProgramming.py
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
        123. 买卖股票的最佳时机Ⅲ
        k = 2
        """
        max_k = 2
        n = len(prices)
        dp = [[[0, 0]] * (max_k + 1)] * n

        for i in range(n):
            for k in range(max_k + 1):
                if i > 0:
                    dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                    dp[i][k][1] = max(dp[i - 1][k - 1][1], dp[i - 1][k - 1][0] - prices[i])

                else:  # base case
                    dp[0][k][0] = 0
                    dp[0][k][1] = -prices[0]
        # return max(dp[-1][-1][0]

        # 骚气强行转移状态法
        n = len(prices)
        dp0 = 0
        dp1 = -prices[0]
        dp2 = float("-inf")
        dp3 = float("-inf")
        dp4 = float("-inf")
        for i in range(n):
            dp1 = max(dp1, - prices[i])
            dp2 = max(dp2, dp1 + prices[i])
            dp3 = max(dp3, dp2 - prices[i])
            dp4 = max(dp4, dp3 + prices[i])
        return max(dp0, dp2, dp4)

    def maxProfit4(self, prices: List[int]) -> int:
        """
        188. 买卖股票的最佳时机 IV
        限制为 k 笔交易
        """
        pass

    def maxProfit5(self, prices: List[int]) -> int:
        """
        含冻结期
        """
        n = len(prices)
        dp_i_0 = 0
        dp_i_1 = float("-inf")
        dp_pre_0 = 0
        for i in range(n):
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_0 + prices[i])
            dp_i_1 = max(dp_i_1, dp_pre_0 - prices[i])
            dp_pre_0 = tmp
        return dp_i_0


class HouseRobber:
    """
    三道打家劫舍问题
    """

    def rob1(self, nums: List[int]) -> int:
        """
        198. 打家劫舍
        你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，
        影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
        如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
        给定一个代表每个房屋存放金额的非负整数数组，
        计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
        :param nums:[1,2,3,1]
        :return:4
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        """
        # 初级动规
        if not nums:
            return 0

        n = len(nums)
        if n <= 2:
            return max(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        # return max(dp[-1], dp[-2])
        """
        N = len(nums)
        dp = [0] * (N + 1)
        dp[0] = 0
        dp[1] = nums[0]
        for j in range(2, N + 1):
            dp[j] = max(dp[j - 1], dp[j - 2] + nums[i]
        return dp[-1]
        
        先不要想着去优化结构，把基本的结构弄出来再说。
        """

        # 优化空间复杂度，滚动数组
        if not nums:
            return 0
        n = len(nums)
        if n <= 2:
            return max(nums)
        left = nums[0]
        right = max(nums[0], nums[1])
        for num in nums[2:]:
            left, right = right, max(left + num, right)
        return right

    def rob2(self, nums: List[int]) -> int:
        """
        213. 打家劫舍 II
        你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。
        这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。
        同时，相邻的房屋装有相互连通的防盗系统，
        如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
        给定一个代表每个房屋存放金额的非负整数数组，
        计算你 在不触动警报装置的情况下 ，能够偷窃到的最高金额。
        :param nums:[1,2,3,1]
        :return:4
        最后一个和第一个不能同时偷
        分情况讨论？
        """
        # 来，先来个憨憨写法试一下，max(helper(nums[1:]), helper(nums[:-1]))
        # 憨憨方法成功
        if not nums:
            return 0
        n = len(nums)
        if n < 2:
            return max(nums)
        dp1 = [0] * n
        dp2 = [0] * n
        dp1[0] = 0
        dp2[0] = nums[0]
        dp1[1] = nums[1]
        dp2[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i])
            dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i])
        return amx(dp1[-1], dp2[-2])

    def rob3(self, root: TreeNode) -> int:
        """
        337. 打家劫舍 III
        在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。
        这个地区只有一个入口，我们称之为“根”。 除了“根”之外，
        每栋房子有且只有一个“父“房子与之相连。一番侦察之后，
        聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。
        如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

        计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。
        层序遍历？
        """

        def postorderTraversal(node):
            if not node:
                return [0, 0]
            left = postorderTraversal(node.left)
            right = postorderTraversal(node.right)
            robHere = left[1] + right[1] + node.val
            notRobHere = max(left[0], left[1]) + max(right[0], right[1])
            return [robHere, notRobHere]

        res = postorderTraversal(root)
        return max(res[0], res[1])

    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right


class SubSum:
    """
    子数组求和类问题
    """
    def subSum(self, nums: List[int], s: int) -> int:
        """
        求和为目标值的子数组的数量，动规基本操作
        :param nums:
        :param s:
        :return:
        """
        dp = [0] * (s + 1)
        dp[0] = 1
        for num in nums:
            for i in range(s, num - 1, -1):
                dp[i] += dp[i - num]
        return dp[s]
