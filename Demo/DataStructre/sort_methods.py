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
    def __init__(self, li):
        self.li = li
        pass

    def bubble_sort(self):
        pass

    def select_sort(self):
        pass

    def insert_sort(self):
        nums = copy.deepcopy(self.li)

        return nums


    @cal_time
    def quick_sort(self):
        def partition(data, left, right):
            tmp = data[left]

            return left

        def _quick_sort(data, left, right):
            mid = partition(data, left, right)

            return 1

        nums = copy.deepcopy(self.li)
        return _quick_sort(nums, 0, len(nums) - 1)


def test01():
    a = list(range(1, 9))
    random.shuffle(a)
    print(a)
    sorts = SortMethods(copy.deepcopy(a))
    res = sorts.quick_sort()

    return res


if __name__ == '__main__':
    test01()
