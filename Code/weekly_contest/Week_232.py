# coding   : utf-8 
# @Time    : 21/03/14 10:25
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : Week_232.py
# @Software: PyCharm


from typing import List

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        min_ = min(nums[:k + 1])
        min_idx = nums[:k + 1].index(min_)
        for i in range(k + 1):
            for j in range(k, n):
                min_ = min(min_, )
                res = max(min(nums[i:j + 1]) * (j - i + 1), res)
        return res

if __name__ == '__main__':
    solution = Solution()
    print(solution)