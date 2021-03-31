# coding   : utf-8 
# @Time    : 21/03/31 10:11
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : Subsets.py
# @Software: PyCharm

"""
子集问题，回溯的模板一套流
"""

class Solution:
    def subsets1(self, nums: List[int]) -> List[List[int]]:
        """
        通过系统库函数完成子集任务
        """
        import itertools
        res = []
        for i in range(len(nums) + 1):
            # for tmp in itertools.combinations(nums, i):
            #     res.append(tmp)
            res.extend(list(itertools.combinations(nums, i)))
            res.extend(list(itertools.combinations_with_replacement(nums, i)))
        return res

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        """
        通过迭代完成子集任务
        """
        res = [[]]
        for num in nums:
            res = res + [[num] + tmp for tmp in res]
        return res

    def subsets3(self, nums: List[int]) -> List[List[int]]:
        """
        通过递归完成子集任务
        """
        res = []
        n = len(nums)
        def backtrack(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                backtrack(j + 1, tmp + [nums[j]])
        backtrack(0, [])
        return res