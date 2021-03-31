# coding   : utf-8 
# @Time    : 21/03/31 9:44
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0331.py
# @Software: PyCharm

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        78. 子集
        无重复
        """
        res = [[]]
        for num in nums:
            res = res + [[num] + i for i in res]
        return res

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        90. 子集 II
        给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
        解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。
        """
        dic = dict()
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        res = [[]]
        for i, v in dic.items():
            tmp = res.copy()
            for j in res:
                tmp.extend(j + [i]*(k+1) for k in range(v))
            res = tmp
        return res

