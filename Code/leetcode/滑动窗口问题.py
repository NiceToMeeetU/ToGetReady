# coding   : utf-8 
# @Time    : 21/02/03 22:06
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 滑动窗口问题.py
# @Software: PyCharm





class Solution:
    import bisect
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        median = lambda a: (a[(len(a) - 1) // 2] + a[len(a) // 2]) / 2
        a = sorted(nums[:k])
        res = [median(a)]
        for i, j in zip(nums[:-k], nums[k:]):
            a.remove(i)
            a.insert(bisect.bisect_left(a, j), j)
            res.append(median(a))
        return res
