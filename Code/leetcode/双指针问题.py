# coding   : utf-8 
# @Time    : 21/02/05 11:12
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 双指针问题.py
# @Software: PyCharm


"""
双指针通常用于求子串等，本质是滑动窗口
只是很多问题不会直接把题意写明白，需要绕个弯找到本质，转换为双指针问题
"""
from typing import List

def dualpointmodel(nums,maxs):
    """
    双指针问题的通用模板
    :param nums: 数组
    :param maxs: 限制条件
    :return:
    """
    n = len(nums)
    i, j = 0, 0     # 定义双指针，构建闭区间
    sums = 0        # 用于计算子区间特性
    res = 0         # 存储最终结果
    # 开始循环
    while j < n:
        sums += nums[j]
        while sums > maxs:
        # while "不满足限制条件":
            sums -= nums[i]
            i += 1  # 左指针在内被动移动
        res = max(res, j-i+1)
        j += 1      # 右指针在外主动移动
    return res

def minSubArrayLen( s: int, nums: List[int]) -> int:
    """
    不要过于死扣模板
    本题是求满足和>=目标值的最小长度子串，所以内层循环正好跟模板相反，是满足条件后移动左指针
    :param s:
    :param nums:
    :return:
    """
    if not nums:
        return 0

    n = len(nums)
    i, j = 0, 0
    sums = 0
    res = n + 1
    while j < n:
        sums += nums[j]
        while sums >= s:
            res = min(res, j - i + 1)
            sums -= nums[i]
            i += 1
        j += 1
    return 0 if res == n + 1 else res