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
    def inside_sort(self):
        """
        python内置排序API
        """
        nums = copy.deepcopy(self.nums_in)
        return sorted(nums)

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
        从左到右，从小到大
        """
        nums = copy.deepcopy(self.nums_in)

        def partition(li, left, right):
            tmp = li[left]
            while left < right:
                while left < right and li[right] >= tmp:  # 右侧的小元素放到左侧
                    right -= 1
                li[left] = li[right]
                while left < right and li[left] <= tmp:  # 左侧的大元素放到右侧
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
        从小到大排序构建大根堆
        从大到小排序构建小根堆
        """
        nums = copy.deepcopy(self.nums_in)
        n = len(nums)

        def _siftdown(data, low, high):
            """
            向下调整函数，
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

        for idx in range(n // 2 - 1, -1, -1):  # (n-1)是最后一个子节点，(n-1-1)//2即最后一个有效父节点
            # 从最后一个有效父节点开始往上遍历，依次调整
            _siftdown(nums, idx, n - 1)

        for idx in range(n - 1, -1, -1):
            # 取数，将大根堆的根节点依次挪到数组最后，不断缩短堆的顶
            nums[0], nums[idx] = nums[idx], nums[0]
            _siftdown(nums, 0, idx - 1)
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
        nums = copy.deepcopy(self.nums_in)
        heapq.heapify(nums)
        res = [heapq.heappop(nums) for _ in range(len(nums))]
        return res

    @cal_time
    def merge_sort(self):
        """
        归并排序
        先考虑有序的两个数组如何归并
        :return:
        """
        nums = copy.deepcopy(self.nums_in)
        n = len(nums)
        def _merge(data, left, mid, right):
            i = left
            j = mid + 1
            tmp = []
            while i <= mid and j <= right:
                if data[i] < data[j]:
                    tmp.append(data[i])
                    i += 1
                else:
                    tmp.append(data[j])
                    j += 1
            while i <= mid:
                tmp.append(data[i])
                i += 1
            while j <= right:
                tmp.append(data[j])
                j += 1

            data[left: right+1] = tmp

        def _merge_sort(data, left, right):
            if left < right:
                mid = (left + right) // 2
                _merge_sort(data, left, mid)
                _merge_sort(data, mid + 1, right)
                _merge(data, left, mid, right)

        _merge_sort(nums, 0, n - 1)
        return nums

    @cal_time
    def shell_sort(self):
        """
        简单选择gap的希尔排序示意
        实际就是将插入排序加入了gap因素
        :return:
        """
        nums = copy.deepcopy(self.nums_in)
        d = len(nums) // 2
        while d >= 1:
            for i in range(d, len(nums)):
                tmp = nums[i]
                j = i - d
                while j >= 0 and tmp < nums[j]:
                    nums[j + d] = nums[j]
                    j -= d
                nums[j + d] = tmp

            d //= 2
        return nums


    @cal_time
    def count_sort(self, max_count = 100):
        """
        计数排序
        即字面意思，构建一个O(n)的map映射，统计各个元素的出现次数
        必须提前知道数的大小范围，且限制数据类型，空间浪费太多
        :return:
        """
        nums = copy.deepcopy(self.nums_in)
        counts = [0 for _ in range(max_count)]
        for val in nums:
            counts[val] += 1
        nums.clear()
        for idx, x in enumerate(counts):
            for i in range(x):
                nums.append(idx)
        return nums

    @cal_time
    def bucket_sort(self, n = 100, max_num = 10000):
        """
        桶排序
        严重取决于数据分布
        :return:
        """
        nums = copy.deepcopy(self.nums_in)
        buckets = [[] for _ in range(n)]
        for val in nums:
            i = min(val // (max_num//n), n - 1)
            buckets[i].append(val)
            for j in range(len(buckets[i]) - 1, 0, -1):
                if buckets[i][j] < buckets[i][j - 1]: # 直接在桶内排序
                    buckets[i][j], buckets[i][j-1] = buckets[i][j-1], buckets[i][j]
                else:
                    break
        res = []
        for bin in buckets:
            res.extend(bin)
        return res


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

    def __init__(self, nums_in, k):
        self.nums_in = nums_in
        self.k = k

    def qsort_top_k(self):
        """
        全局快排后取切片
        :return:
        """
        pass

    @cal_time
    def heap_top_k(self):
        """
        堆排序解决TopK问题
        先选k个选择构建一个小根堆，然后遍历原数组更新小根堆，遍历完成即得
        """
        pass
        nums = copy.deepcopy(self.nums_in)
        n = len(nums)

        def _upsift(data, low, high):
            i = low
            j = 2 * i + 1
            tmp = data[i]
            while j <= high:
                if j < high and data[j] > data[j + 1]:
                    j += 1

                if tmp > data[j]:
                    data[i] = data[j]
                    i = j
                    j = i * 2 + 1
                else:
                    break
            data[i] = tmp

        heap_nums = nums[:self.k]

        # 构建k个元素的大根堆
        for idx in range(self.k // 2 - 1, -1, -1):
            _upsift(heap_nums, idx, self.k - 1)
        # 此时栈顶已经是这k个元素的最大值了
        # 遍历剩余n-k的原数组，只要比堆顶大就加入，否则略过
        for idx in range(self.k, n):
            if nums[idx] > heap_nums[0]:
                heap_nums[0] = nums[idx]
                _upsift(heap_nums, 0, self.k - 1)

        # 按照从大到小输出结果
        for idx in range(self.k - 1, -1, -1):
            heap_nums[0], heap_nums[idx] = heap_nums[idx], heap_nums[0]
            _upsift(heap_nums, 0, idx - 1)

        return heap_nums


def test01():
    li1 = list(range(1, 10000))
    random.shuffle(li1)
    # print(li1)
    sorts = SortMethods(li1)
    ans0 = sorts.inside_sort()
    # ans1 = sorts.quick_sort()
    # ans2 = sorts.heap_sort()
    # ans3 = sorts.merge_sort()
    # ans4 = sorts.shell_sort()
    ans5 = sorts.bucket_sort(100, 10000)
    print(ans5[:20])
    # print(ans4)

if __name__ == '__main__':
    test01()
