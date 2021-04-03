# coding   : utf-8 
# @Time    : 21/04/02 11:27
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0402.py
# @Software: PyCharm


from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        接雨水
        :param height:
        :return:
        """
        n = len(height)
        if n <=2:
            return 0
        res = 0
        left, right = 0, n - 1
        max_left, max_right = 0, 0
        while left <= right:
            if max_left < max_right:
                res += max(0, max_left - height[left])
                max_left = max(max_left, height[left])
                left += 1
            else:
                res += max(0, max_right - height[right])
                max_right = max(max_right, height[right])
                right -= 1
        return res

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        除自身以外数组的乘积
        :param nums:
        :return:
        左右乘，要求时间O(n)，空间O(1)
        """
        n = len(nums)
        left, right = 1, 1
        res = [1] * n
        for i in range(n):
            res[i] *= left
            left *= nums[i]

            res[n - 1 - i] *= right
            right *= nums[n - 1 - i]
        return res
