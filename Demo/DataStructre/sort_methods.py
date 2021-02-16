# coding   : utf-8 
# @Time    : 21/02/16 19:23
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : sort_methods.py
# @Software: PyCharm


import random
from _TOOL import cal_time
import copy


class SortMethods:
    """
    手写排序算法
    为利于不同方法对比，每种方法先设置对待排序数组的深拷贝
    """

    def __init__(self, int_list):
        self.int_list = int_list

    @cal_time
    def bubble_sort(self):
        """
        冒泡排序
        遍历整数数组，如果前面的数比后面的大，则交换两个数
        代码关键：趟，无序区范围
        前面无序，后面有序
        存在问题：
            若数组本身有序，会浪费时间
        """
        nums = copy.deepcopy(self.int_list)
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums

    @cal_time
    def bubble_sort_better(self):
        """
        冒泡排序可以优化的点：
        如果一趟中完全没有发生交换，说明数组已经有序，可直接break
        """
        nums = copy.deepcopy(self.int_list)
        exchange = False
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    exchange = True
            if not exchange:
                return nums
        return nums

    @cal_time
    def select_sort(self):
        """
        选择排序
        一趟中最小的数放首位，多趟循环
        注意有序区和无序区
        """
        nums = copy.deepcopy(self.int_list)
        for i in range(len(nums)):
            min_loc = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min_loc]:
                    min_loc = j
            if min_loc != i:
                nums[i], nums[min_loc] = nums[min_loc], nums[i]
        return nums

    @cal_time
    def insert_sort(self):
        """
        插入排序
        每次迭代从无序区挑一个数放入有序区的合适位置
        """
        nums = copy.deepcopy(self.int_list)
        for i in range(1, len(nums)):
            tmp = nums[i]
            j = i - 1
            while j >= 0 and tmp < nums[j]:
                nums[j + 1] = nums[j]
                j = j - 1
            nums[j + 1] = tmp
        return nums

    @cal_time
    def quick_sort(self):
        """
        快速排序
        """
        nums = copy.deepcopy(self.int_list)

        def partition(li, left, right):
            tmp = li[left]
            while left < right:
                while left < right and li[right] >= tmp:
                    right -= 1
                li[left] = li[right]
                while left < right and li[left] <= tmp:
                    left += 1
                li[right] = li[left]
            li[left] = tmp
            return left

        def _quick_sort(li, left, right):
            """
            排序内迭代函数，直接按照形参传递
            :param li:
            :param left:
            :param right:
            :return:
            """
            if left < right:
                mid = partition(li, left, right)
                _quick_sort(li, left, mid - 1)
                _quick_sort(li, mid + 1, right)

        _quick_sort(nums, 0, len(nums) - 1)
        return nums


def test01():
    li1 = list(range(1, 1000))
    random.shuffle(li1)
    print(li1)
    sorts = SortMethods(li1)
    ans1 = sorts.bubble_sort()
    print(ans1)
    ans2 = sorts.insert_sort()
    print(ans2)


if __name__ == '__main__':
    test01()
