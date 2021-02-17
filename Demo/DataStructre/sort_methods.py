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

    def __init__(self, nums_in):
        self.nums_in = nums_in

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
        nums = copy.deepcopy(self.nums_in)
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
        nums = copy.deepcopy(self.nums_in)
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
        nums = copy.deepcopy(self.nums_in)
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
        nums = copy.deepcopy(self.nums_in)
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
        分治策略
        """
        nums = copy.deepcopy(self.nums_in)

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

    @cal_time
    def heap_sort(self):
        """
        堆排序

        :return:
        """
        nums = copy.deepcopy(self.nums_in)
        n = len(nums)

        def sift(data, low, high):
            """
            堆的调整函数，
            :param data: 整数数组
            :param low: 堆根节点
            :param high: 堆最后一个叶节点
            :return:
            """
            i = low
            j = 2 * i + 1
            tmp = data[i]
            while j <= high:  # 构建一个大根堆
                if j < high and data[j] < data[j + 1]:  # 单独的if切换必要的左右子节点
                    j += 1

                if tmp < data[j]:  # 只要子节点比父节点大，就交换
                    data[i] = data[j]
                    i = j
                    j = 2 * i + 1
                else:  # tmp>=data[j]，j也已经到最下面了，说明已经是大根堆了
                    break
            # 跳出循环后i是某个可用节点，要么是已经到最后的叶节点使得j越界跳出，要么是tmp放这里可以使堆有效
            data[i] = tmp

        # 开始排序，1-建堆，2-取数

        for i in range(n // 2 - 1, -1, -1):  # (n-1)是最后一个子节点，(n-1-1)//2即最后一个有效父节点
            # 从最后一个有效父节点开始往上遍历，依次调整
            sift(nums, i, n - 1)

        for i in range(n - 1, -1, -1):
            # 取数，将大根堆的根节点依次挪到数组最后，不断缩短堆的顶
            nums[0], nums[i] = nums[i], nums[0]
            sift(nums, 0, i - 1)
        return nums

    @cal_time
    def heap_sort_inside(self):
        """
        python内置了heapq模块，可以快速建堆
        用堆实现的优先队列
        :return:
        """
        pass
        import heapq


class TopK:
    """
    TopK 问题
    所有方法都需要掌握：
    1、全局排序切片，O(nlogn+k)
    2、局部排序，O(n*k)
    3、堆方法，O(n*logk)
    4、分治法
    5、减治法
    6、随机法
    """

    def __init__(self, nums_in):
        self.nums_in = nums_in

    def heap_top_k(self, k):
        """
        堆排序解决TopK问题
        先选k个选择构建一个小根堆，然后遍历原数组更新小根堆，遍历完成即得
        :param k:
        :return:
        """
        pass


def test01():
    li1 = list(range(1, 100))
    random.shuffle(li1)
    print(li1)
    sorts = SortMethods(li1)
    ans = sorts.heap_sort()
    print(ans)


if __name__ == '__main__':
    test01()
