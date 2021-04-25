# coding   : utf-8 
# @Time    : 21/04/22 17:12
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0422.py
# @Software: PyCharm


from typing import List


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        """
        给一个 m * n 的矩阵和一个整数，找出并返回矩阵内部矩形区域内不超过k的最大数值和
        :param matrix:
        :param k:
        :return:
        """
        import bisect
        row, col = len(matrix), len(matrix[0])
        res = float("-inf")
        for left in range(col):
            sums = [0] * row
            for right in ramge(left, col):
                for j in range(row):
                    sums[j] += matrix[j][right]
                lst = [0]
                cur = 0
                for num in sums:
                    cur += num
                    loc = bisect.bisect_left(lst, cur - k)
                    if loc < len(lst):
                        res = max(cur - lst[loc], res)
                    bisect.insort(lst, cur)
        return res


if __name__ == '__main__':
    solution = Solution()
    m = [[1, 2, 3], [3, 4, 2], [-3, 2, 0], [-1, 0, 3], [-4, 2, 1]]
    k = 4
    ans = solution.maxSumSubmatrix(m, k)
    print(ans)
