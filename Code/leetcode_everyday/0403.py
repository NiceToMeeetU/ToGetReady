# coding   : utf-8 
# @Time    : 21/04/03 15:41
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0403.py
# @Software: PyCharm


from typing import List

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        1143. 最长公共子序列
        不改变顺序，不需要连续
        :param text1:
        :param text2:
        :return:
        """
        m, n = len(text1), len(text2)
        pre = [0] * (n + 1)
        dp = [0] * (n + 1)
        for i in range(m):
            for j in range(1, n + 1):
                if text1[i] == text2[j - 1]:
                    dp[j] = pre[j - 1] + 1
                else:
                    dp[j] = max(pre[j], dp[j - 1])
                pre[j - 1] = dp[j - 1]
            pre[j] = dp[j]
        return dp[-1]



