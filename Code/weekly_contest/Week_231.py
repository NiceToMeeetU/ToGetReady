# -*- coding: utf-8 -*-
# @Time    : 21/03/07 10:25
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : Week_231.py
# @Software: PyCharm


from typing import List
import collections


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        """
        给你一个二进制字符串 s ，该字符串 不含前导零 。

        如果 s 最多包含 一个由连续的 '1' 组成的字段 ，返回 true​​​ 。否则，返回 false 。
        :param s:
        :return:
        """
        # flag = False
        # res = False
        # for i in range(1, len(s)):
        #     if flag and s[i] =="1":
        #         res = True
        #     elif flag and s[i] =="0":
        #         if set(s[i:]) == {"0"}:
        #             return True
        #         else:
        #             return False
        #     if s[i] == "1":
        #         flag = True
        #     elif s[i] == "0":
        #         flag = False
        # return False

        # flag = False
        # for i in range(1, len(s)):
        #     if flag and s[i] =="1":
        #         res = True
        #     elif flag and s[i] =="0":
        #         if set(s[i:]) == {"0"}:
        #             return True
        #         else:
        #             return False
        #
        #     if s[i-1:i+1] == "11":
        #         flag = True
        #     else:
        #         flag = False
        # return flag
        for i in range(1, len(s)):
            if s[i] != "1":
                return set(s[i:]) == {"0"}
        return True

    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        """
        给你一个整数数组 nums ，和两个整数 limit 与 goal 。数组 nums 有一条重要属性：abs(nums[i]) <= limit 。
        返回使数组元素总和等于 goal 所需要向数组中添加的 最少元素数量 ，添加元素 不应改变 数组中 abs(nums[i]) <= limit 这一属性。
        注意，如果 x >= 0 ，那么 abs(x) 等于 x ；否则，等于 -x 。
        :param nums:
        :param limit:
        :param goal:
        :return:
        """
        sum_ = abs(goal - sum(nums))
        if sum_ == 0:
            return 0
        n = sum_//limit
        m = sum_%limit
        if m == 0:
            return n
        else:
            return 1 + n


if __name__ == '__main__':
    solution = Solution()
    print(solution.checkOnesSegment("11011"))
