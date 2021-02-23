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

if __name__ == '__main__':
    pass
    s = Solution()
    s.m1052()