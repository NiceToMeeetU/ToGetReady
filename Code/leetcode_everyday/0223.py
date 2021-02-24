# coding   : utf-8 
# @Time    : 21/02/23 9:11
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0223.py
# @Software: PyCharm

from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        """First Try: 太麻烦了，未考虑len=1的特殊情况"""
        # total = 0
        # for c, g in zip(customers, grumpy):
        #     total += c if g == 0 else 0
        # ans = total
        # for i in range(len(customers) - X + 1):
        #     tmp = 0
        #     for j in range(i, i + X):
        #         tmp += customers[j] if grumpy[j] == 1 else 0
        #     ans = max(tmp + total, ans)
        # return ans
        n = len(customers)
        total = sum(c for c,g in zip(customers, grumpy) if g == 0)
        max_ = increase = sum(c*g for c, g in zip(customers[: X], grumpy[: X]))
        for i in range(X, n):
            increase += customers[i] * grumpy[i] - customers[i - X] * grumpy[i - X]
            max_ = max(max_, increase)
        return total + max_

    def m1052(self):
        # customers = [1, 0, 1, 2, 1, 1, 7, 5]
        # grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
        # X = 3
        customers = [8, 8]
        grumpy = [1, 0]
        X = 2
        ans = self.maxSatisfied(customers,grumpy,X)
        print(ans)

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_ = dict()
        for idx, num in enumerate(nums):
            if target - num in dict_:
                return [dict_[target - num], idx]
            dict_[num] = idx
        return []

    def e1(self):
        ans = self.twoSum([1,2,3,4,5], 4)
        print(ans)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for line in matrix:
        #     if target in line:
        #         return True
        # return False
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        left = 0
        right = m * n - 1
        while left < right:
            mid = (left + right) // 2
            i = mid // n
            j = mid % n
            if matrix[i][j] == target:
                return True
            elif matrix[i][j]  < target:
                left = mid + 1
            elif matrix[i][j]  > target:
                right = mid - 1
        return False


    def m74(self):
        self.searchMatrix()

    def restoreString(self, s: str, indices: List[int]) -> str:
        res = ["a"] * len(s)
        for i in range(len(s)):
            res[indices[i]] = s[i]
        return ''.join(res)

    def e1528(self):
        print(self.restoreString("codeleet", [4,5,6,7,0,2,1,3]))

    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        dict_ = dict()
        d = abs(max(arr) - min(arr))//(len(arr) - 1)
        for i in arr:
            dict_[i] = dict_.get(i, 0) + 1
            dict_[i + d] = dict_.get(i + d, 0) + 1
            dict_[i - d] = dict_.get(i - d, 0) + 1
        print(dict_)

    def e1502(self):
        self.canMakeArithmeticProgression([3,5,4])

if __name__ == '__main__':
    pass
    s = Solution()
    # s.m1052()
    # s.e1()
    # s.e1528()
    s.e1502()