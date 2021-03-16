# coding   : utf-8 
# @Time    : 21/03/16 11:13
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0316.py
# @Software: PyCharm


from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        """
        260. 只出现一次的数字 III
        给定一个整数数组nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。
        找出只出现一次的那两个元素。你可以按 任意顺序 返回答案。
        进阶：你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？
        """
        import functools
        tmp = functools.reduce(lambda x,y: x^ y, nums)
        div = 1
        while tmp & div == 0:
            div <<= 1
        res1, res2 = 0, 0
        for num in nums:
            if num & div:
                res1 ^= num
            else:
                res2 ^= num
        return [res1, res2]

    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        59. 螺旋矩阵 II
        给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，
        且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
        """
        res = [[0 for _ in range(n)] for _ in range(n)]
        i,j = 0, 0
        left, right, up, down = 0, 0, 0, 0
        k = 1
        while k <= n**2:
            for j in range(left, n-right):
                res[i][j] = k
                k += 1
            up += 1
            for i in range(up, n - down):
                res[i][j] = k
                k += 1
            right += 1
            for j in range(n - right -1, left - 1, -1):
                res[i][j] = k
                k += 1
            down += 1
            for i in range(n - down - 1, up - 1, -1):
                res[i][j] = k
                k += 1
            left += 1
        return res


    def maxProduct(self, nums:List[int]) -> int:
        """
        152. 乘积最大子数组
        """
        res = nums[0]
        minF = nums[0]
        maxF = nums[0]
        for num in nums[1:]:
            minTemp = minF
            maxTemp = maxF
            minF = min(minTemp * num, min(num, maxTemp * num))
            maxF = max(maxTemp * num, max(num, minTemp * num))
            res = max(maxF, res)
        return  res