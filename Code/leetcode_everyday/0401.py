# coding   : utf-8 
# @Time    : 21/04/01 8:17
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0401.py
# @Software: PyCharm


import math


class Solution:
    def clumsy(self, N: int) -> int:
        """
        通常，正整数 n 的阶乘是所有小于或等于 n 的正整数的乘积。例如，factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1。
        相反，我们设计了一个笨阶乘 clumsy：在整数的递减序列中，我们以一个固定顺序的操作符序列来依次替换原有的乘法操作符：
        乘法(*)，除法(/)，加法(+)和减法(-)。
        例如，clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1。然而，这些运算仍然使用通常的算术运算顺序：
        我们在任何加、减步骤之前执行所有的乘法和除法步骤，并且按从左到右处理乘法和除法步骤。
        另外，我们使用的除法是地板除法（floor division），所以10 * 9 / 8等于11。这保证结果是一个整数。
        实现上面定义的笨函数：给定一个整数 N，它返回 N 的笨阶乘。

        什么垃圾题
        """

        res = 0
        tmp = 1
        loop = 0
        for num in range(N, 0, -1):
            if loop == 0:
                tmp *= num
            elif loop == 1:
                tmp *= num
            elif loop == 2:
                tmp = tmp // num
                tmp =  sign * tmp
            loop = (loop + 1) % 4
            res += tmp
            tmp = 1
        return res

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        347. 前 K 个高频元素
        给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
        """
        # 直接想到的排序法，虽然能跑通，但实际考察的是堆
        # dic = dict()
        # for num in nums:
        #     dic[num] = dic.get(num, 0) + 1
        # dic = sorted(dic.items(), key=lambda x:x[1], reverse=True)
        # res = [i[0] for i in dic[:k]]
        # return res

        # 前K大值，用小根堆
        import collections
        import heapq
        dic = collections.Counter(nums)
        heap = []
        res= []
        for num, freq in dic.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            else:
                if heap[0][0] < freq:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (freq, num))
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res

if __name__ == '__main__':
    solution = Solution()
    print(solution.clumsy(10))
