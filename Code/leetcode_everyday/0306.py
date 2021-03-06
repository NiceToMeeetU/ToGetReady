# coding   : utf-8 
# @Time    : 21/03/06 8:45
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0306.py
# @Software: PyCharm


"""
循环问题乘二解决
今日连续单调栈
"""

from typing import List
import collections


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        503
        给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），
        输出每个元素的下一个更大元素。数字 x 的下一个更大的元素是按数组遍历顺序，
        这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。
        如果不存在，则输出 -1。
        :param nums: [1, 2, 1]
        :return: [2, -1, 2]
        直接暴力求解是O(n^2)时间复杂度，不可接受
        需要用一种结构来存储
        哈希表？
        栈？
        循环问题直接将列表乘以二即可处理

        典型单调栈问题
        """
        n = len(nums)
        res = [-1] * n
        stack = []
        for idx, num in enumerate(nums * 2):
            while stack and num > nums[stack[-1]]:
                res[stack.pop()] = num
            if idx < n:
                stack.append(idx)
        return res

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        496
        给你两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。
        请你找出 nums1 中每个元素在 nums2 中的下一个比其大的值。
        nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1
        """
        dict_res = {k: -1 for k in nums2}
        stack = []
        for idx, num in enumerate(nums2):
            while stack and num > nums2[stack[-1]]:
                dict_res[nums2[stack.pop()]] = num
            stack.append(idx)
            print(f"{idx =}, {stack = }, {dict_res = }")

        return [dict_res[k] for k in nums1]

    def nextGreaterElement556(self, n: int) -> int:
        """
        556
        给你一个正整数 n ，请你找出符合条件的最小整数，其由重新排列 n 中存在的每位数字组成，
        并且其值大于 n 。如果不存在这样的正整数，则返回 -1 。
        注意 ，返回的整数应当是一个 32 位整数 ，如果存在满足题意的答案，但不是 32 位整数 ，同样返回 -1 。
        """
        s = list(map(int, str(n)))
        length = len(s)
        index = length - 2
        while index >= 0:  # 寻找第一个比后面数字小的数字s[index]
            if s[index] < s[index + 1]:
                break
            index -= 1
        if index < 0:  # 如果不存在，则元素按降序排列，返回-1
            return -1
        for j in range(length - 1, index, -1):  # 寻找最后一个比s[index]大的数字s[j]
            if s[j] > s[index]:
                break
        s[index], s[j] = s[j], s[index]  # s[j]与s[index]交换，并将s[index+1:]从小到大排序
        res = int(''.join(map(str, s[:index + 1] + sorted(s[index + 1:]))))
        return -1 if res > (1 << 31) - 1 else res  # 检查是否越界

    def dailyTemperatures(self, T: List[int]) -> List[int]:
        """
        739
        请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：
        要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。
        例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，
        你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。
        提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，
        都是在 [30, 100] 范围内的整数。
        """
        res = [0] * len(T)
        stack = []
        for i, t in enumerate(T):
            while stack and t > T[stack[-1]]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return res


if __name__ == '__main__':
    pass
    solution = Solution()
    print(solution.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
