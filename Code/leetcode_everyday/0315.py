# coding   : utf-8 
# @Time    : 21/03/15 8:09
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0315.py
# @Software: PyCharm

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        54. 顺时针输出螺旋矩阵
        :param matrix:
        :return:
        """
        m, n = len(matrix), len(matrix[0])
        res = []
        i, j = 0, 0
        left, right, up, down = 0, 0, 0, 0
        while len(res) < m * n:
            for j in range(left, n - right):
                res.append(matrix[i][j])
            up += 1
            for i in range(up, m - down):
                res.append(matrix[i][j])
            right += 1
            for j in range(n - right - 1, left - 1, -1):
                res.append(matrix[i][j])
            down += 1
            for i in range(m - down - 1, up - 1, -1):
                res.append(matrix[i][j])
            left += 1
        return res[:m * n]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        139. 单词拆分
        给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，
        判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
        """
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s)):
            for j in range(i + 1, n + 1):
                if dp[i] and (s[i:j] in wordDict):
                    dp[j] = True
        return dp[n]

    def findNumberOfLIS(self, nums: List[int]) -> int:
        """
        最长递增子序列的个数
        what the fuck!
        :param nums:
        :return:
        """
        n = len(nums)
        if n <= 1:
            return n
        length = [0] * n
        count = [1] * n
        for j, num in enumerate(nums):
            for i in range(j):
                if nums[i] < nums[j]:
                    if length[i] >= length[j]:
                        length[j] = 1 + length[i]
                        count[j] = count[i]
                    elif length[i] + 1 == length[j]:
                        count[j] += count[i]
        longest = max(length)
        return sum(c for i,c in enumerate(count) if length[i] == longest)


    def maxProduct(self, nums: List[int]) -> int:
        """
        乘积最大子数组
        :param nums:
        :return:
        """
        minF = nums[0]
        maxF = nums[0]
        res = nums[0]
        for num in nums:
            minTmp, maxTmp = minF, maxF
            maxF = max(maxTmp * num, max(num, minTmp * num))
            minF = min(minTmp * num, min(num, maxTmp * num))
            res = max(maxF, res)
        return res

    def findDuplicate(self, nums: List[int]) -> int:
        """
        287. 寻找重复数
        给定一个包含 n + 1 个整数的数组 nums ，
        其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。
        假设 nums 只有 一个重复的整数 ，找出 这个重复的数 。
        """
        slow, fast = 0, 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slov == fast:
                fast = 0
                while nums[slow] != nums[fast]:
                    fast = nums[fast]
                    slow = nums[slow]
                return nums[slow]



if __name__ == '__main__':
    solution = Solution()
    print(solution.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
