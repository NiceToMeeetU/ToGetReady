# coding   : utf-8 
# @Time    : 21/02/03 22:06
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 滑动窗口问题.py
# @Software: PyCharm


import bisect



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
