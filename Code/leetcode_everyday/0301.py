# coding   : utf-8 
# @Time    : 21/03/01 8:12
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0301.py
# @Software: PyCharm


from typing import List

class NumArray:
    """
    给定一个整数数组  nums，求出数组从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点。
    实现 NumArray 类：
    NumArray(int[] nums) 使用数组 nums 初始化对象
    int sumRange(int i, int j) 返回数组 nums 从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点（也就是 sum(nums[i], nums[i + 1], ... , nums[j])）
    """
    def __init__(self, nums: List[int]):
        self.nums = nums
        tmp = 0
        self.sums = []
        for i in self.nums:         # 写这什么垃圾方法
            tmp += i
            self.sums.append(tmp)
        # 实在一点
        self._sums = [0]
        for num in nums:
            self._sums.append(self._sums[-1] + num)

    def sumRange(self, i: int, j: int) -> int:
        # if j < i:
        #     return 0
        # return self.sums[j] - self.sums[i] + self.nums[i]
        return self._sums[j + 1] - self._sums[i]


if __name__ == '__main__':
    obj = NumArray([-2, 0, 3, -5, 2, -1])
    print(obj.sums)
    print(obj.sumRange(0,2))
    print(obj.sumRange(2,5))
    print(obj.sumRange(0,5))