# coding   : utf-8 
# @Time    : 21/03/02 9:14
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0302.py
# @Software: PyCharm

from typing import List


class NumMatrix:
    """
    给定一个二维矩阵，计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2)。
    上图子矩阵左上角 (row1, col1) = (2, 1) ，右下角(row2, col2) = (4, 3)，该子矩形内元素的总和为 8。
    """

    def __init__(self, matrix: List[List[int]]):
        self.m = matrix
        self.sums = [[0] for _ in range(len(self.m))]
        for i in range(len(self.m)):
            for num in self.m[i]:
                self.sums[i].append(self.sums[i][-1] + num)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for i in range(row1, row2 + 1):
            res += self.sums[i][col2 + 1] - self.sums[i][col1]
        return res


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        """
        1109
        这里有n个航班，它们分别从 1 到 n 进行编号。
        我们这儿有一份航班预订表，表中第i条预订记录bookings[i] = [j, k, l]意味着我们在从 j到 k的每个航班上预订了 l个座位。
        请你返回一个长度为 n 的数组answer，按航班编号顺序返回每个航班上预订的座位数。
        :param bookings:[[1,2,10],[2,3,20],[2,5,25]]
        :param n:5
        :return:[10,55,45,25,25]

        """
        diff = Difference([0] * n)
        for j, k, l in bookings:
            diff.increament(j - 1, k - 1, l)

        return diff.result()


class Difference:
    """
    构建差分数组，用于前缀和等类似问题，区间快速增减
    差分数组的主要适用场景是频繁对原始数组的某个区间的元素进行增减。
    """

    def __init__(self, nums: List[int]):
        """
        用原始数组做初始化，直接构建出差分数组
        原始数组：[1,2,5,2,6,8,0,3]
        差分数组：[1,1,3,-3,4,2,-8,3]
        :param nums:
        """
        self.n = len(nums)
        self.diff = [nums[0]]
        for idx in range(1, self.n):
            self.diff.append(nums[idx] - nums[idx - 1])

    def increament(self, i, j, val):
        """
        依次增加[i.j]区间内的元素
        原始数组nums[i,j]元素都 +m
        相当于差分数组的 diff[i] += 3, diff[j+1] -= 3即可
        :param i:
        :param j:
        :param val:
        :return:
        """
        self.diff[i] += val
        if j + 1 < self.n:  # 若j+1>n说明是对i之后的都加m，所以后面就不用动了
            self.diff[j + 1] -= val

    def result(self):
        """
        从差分数组回到原始数组：
        原始数组：[1,2,5,2,6,8,0,3]
        差分数组：[1,1,3,-3,4,2,-8,3]
        差分数组的前缀和就是原数组
        """
        res = [0]
        for d in self.diff:
            res.append(res[-1] + d)
        return res[1:]


if __name__ == '__main__':
    # m = [[3, 0, 1, 4, 2],
    #      [5, 6, 3, 2, 1],
    #      [1, 2, 0, 1, 5],
    #      [4, 1, 0, 1, 7],
    #      [1, 0, 3, 0, 5]]
    # obj = NumMatrix(m)
    # print(obj.sumRegion(2, 1, 4, 3))
    # print(obj.sumRegion(1, 1, 2, 2))
    # print(obj.sumRegion(1, 2, 2, 4))
    solution = Solution()
    print(solution.corpFlightBookings([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5))
