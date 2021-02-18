# coding   : utf-8 
# @Time    : 21/02/03 22:06
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 滑动窗口问题.py
# @Software: PyCharm


import bisect
from typing import List


class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        """
        滑动中位数问题
        :param nums: 整数数组
        :param k: 窗口大小
        :return: 每个窗口内的中位数
        """
        median = lambda a: (a[(len(a) - 1) // 2] + a[len(a) // 2]) / 2
        a = sorted(nums[:k])
        res = [median(a)]
        for i, j in zip(nums[:-k], nums[k:]):
            a.remove(i)
            a.insert(bisect.bisect_left(a, j), j)
            res.append(median(a))
        return res

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    """
    239题，用双端队列实现固定长度滑动窗口的最大值。
    :param nums:
    :param k:
    :return:
    """
    if not nums: return []
    window, res = [], []
    for i, x in enumerate(nums):
        if i >= k and window[0] <= i - k:
            window.pop(0)

        while window and nums[window[-1]] <= x:
            window.pop()

        window.append(i)

        if i >= k - 1:
            res.append(nums[window[0]])
    return res


a = [2,3,1,5,7,-1,234,5,3,2,5,6,8,6]
ans = maxSlidingWindow(a, 3)
