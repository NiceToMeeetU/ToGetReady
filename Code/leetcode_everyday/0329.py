# coding   : utf-8 
# @Time    : 21/03/29 19:17
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0329.py
# @Software: PyCharm

from typing import List


class Solution:
    def decodeString(self, s: str) -> str:
        """
        394. 字符串解码
        给定一个经过编码的字符串，返回它解码后的字符串。
        编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
        你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
        此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像3a或2[4]的输入。
        :param s:
        :return:
        """
        res = ""
        num = 0
        stack = []

        for c in s:
            if c.isnumeric(dsa ):
                num = num * 10 + int(c)
            elif c == "[":
                stack.append((res, num))
                res, num = "", 0
            elif c.isalpha():
                res += c
            elif c == "]":
                str_tmp, num_tmp = stack.pop()
                res += str_tmp + res * num_tmp
        return res

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        581. 最短无序连续子数组
        给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

        请你找出符合题意的 最短 子数组，并输出它的长度。
        """
        n = len(nums)
        i, j = 0, 1
        res = 0
        while nums[i] < nums[j]:
            i += 1
            j = i + 1

        i, j = n - 2, n - 1
        while nums[i] < nums[j]:
            i -= 1
            j


    def numTrees(self, n: int) -> int:
        """
        96. 不同的二叉搜索树
        给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
        :param n:
        :return:
        """
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]

solution2 = Solution()
solution2.decodeString("dasd ")

if __name__ == '__main__':
    solution = Solution()
    print(solution.decodeString("3[a2[c]]"))
