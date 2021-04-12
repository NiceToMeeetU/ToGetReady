# coding   : utf-8 
# @Time    : 21/04/12 8:19
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0412.py
# @Software: PyCharm

from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """
        179.最大数
        给定一组非负整数，重新排列每个数的顺序，每个数不可不可拆分
        使之组成一个最大的整数
        返回一个字符串
        :param nums:
        :return:
        """
        from functools import cmp_to_key
        compare = cmp_to_key(lambda a,b : 1 if a + b < b + a else -1)
        res = "".join(sorted(map(str, nums), key=compare)).lstrip("0")
        return res or "0"
