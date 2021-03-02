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
if __name__ == '__main__':

    m = [[3, 0, 1, 4, 2],
         [5, 6, 3, 2, 1],
         [1, 2, 0, 1, 5],
         [4, 1, 0, 1, 7],
         [1, 0, 3, 0, 5]]
    obj = NumMatrix(m)
    print(obj.sumRegion(2, 1, 4, 3))
    print(obj.sumRegion(1, 1, 2, 2))
    print(obj.sumRegion(1, 2, 2, 4))
