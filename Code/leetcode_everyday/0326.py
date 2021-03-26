# coding   : utf-8 
# @Time    : 21/03/26 20:14
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0326.py
# @Software: PyCharm


from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        49. 字母异位词分组
        给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

        :param strs:
        :return:
        """
        res = []
        dic_c = dict()
        for s in strs:
            tmp = "".join(sorted(s))
            if tmp in dic_c:
                res[dic_c[tmp]].append(s)
            else:
                res.append([s])
                dic_c[tmp] = len(res) - 1
        return res

    def canJump(self, nums: List[int]) -> bool:
        """
        55. 跳跃游戏
        给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
        数组中的每个元素代表你在该位置可以跳跃的最大长度。
        判断你是否能够到达最后一个下标。

        从后往前遍历

        """
        gap = 1
        for j in range(len(nums) - 2, -1, -1):
            if nums[j] >= gap:
                gap = 1
            else:
                gap += 1
            if j == 0 and gap > 1:
                return False
        return True

    def uniquePaths(self, m: int, n: int) -> int:
        """
        62. 不同路径
        :param m:
        :param n:
        :return:
        """
        dp = [[0 for _ in range(n)]for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]



    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        64. 最小路径和

        给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小
        说明：每次只能向下或者向右移动一步。
        :param grid:
        :return:
        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + nums[i][j]
        base:
            dp[0][j] = dp[0][j - 1] + nums[0][j]
            dp[i][0] = dp[i - 1][0] + nums[i][0]
            dp[0][0] = nums[0][0]

        """
        m, n = len(grid), len(grid[0])
        # 第一次方法
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i == 0 and j > 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                if j == 0 and i > 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                elif i > 0 and j > 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        # return dp[m - 1][n - 1]

        # 原地修改
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        # return grid[m - 1][n - 1]

        # 评论区的好方法
        dp = [float('inf')] * (len(grid[0]) + 1)
        dp[1] = 0
        for row in grid:
            for idx, num in enumerate(row):
                dp[idx + 1] = min(dp[idx], dp[idx + 1]) + num
        return dp[-1]

    def decodeString(self, s: str) -> str:
        """
        394. 字符串解码
        给定一个经过编码的字符串，返回它解码后的字符串。
        编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
        你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
        此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
        """
        # s = [c.split("[") for c in s.split("]")]
        # print(s)
        # res = ""
        # for num, letter in s[:-1]:
        #     res += int(num) * letter
        # return res
        res = ""
        if not s[0].isnumeric():
            s = "1" + s
        i,j = 0, 1
        while j < len(s):
            if s[j].isnumeric() or j == len(s) - 1:
                res += int(s[i]) * s[i+1:j ].replace("[","").replace("]","")
                i = j
            j += 1
        return res





if __name__ == '__main__':
    solution = Solution()
    # ans = solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(solution.decodeString("3[a]2[bc]"), "aaabcbc")
    print(solution.decodeString("3[a2[c]]"), "accaccacc")
    print(solution.decodeString("2[abc]3[cd]ef"), "abcabccdcdcdef")
    print(solution.decodeString("abc3[cd]xyz"),  "abccdcdcdxyz")