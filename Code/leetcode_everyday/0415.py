# coding   : utf-8 
# @Time    : 21/04/15 11:19
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0415.py
# @Software: PyCharm


class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        求n次幂
        递归分治
        """
        if n == 0:
            return 1
        elif n < 0:
            return self.myPow(x, -n)

        if n % 2:
            return x * (self.myPow(x, n - 1))
        else:
            return self.myPow(x * x, n // 2)

    def nyPow1(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        res = 1
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res