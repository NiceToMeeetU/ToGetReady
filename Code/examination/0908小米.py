# -*- coding: utf-8 -*-
# @Time    : 21/09/08 18:56
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0908小米.py
# @Software: PyCharm

# class Solution:
#     def func(self):
#         pass
#
#
# if __name__ == '__main__':
#     solution = Solution()
#     a = list(map(int, input().strip().split()))




"""
s='adfeqfqwefqwerwenrqwerwqerasfdsf'
将 s的字符从小到大排序，并且去重(即每个相同字符只保留一个)

"""


class Solution:
    def bubblesort(self, nums):
        # method 1
        # return sorted(list(set(s)))

        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums
        # method 2

if __name__ == '__main__':
    solution = Solution()
    s = [1,2,4,1,4,5,5]
    ans = solution.bubblesort(s)
    print(ans)