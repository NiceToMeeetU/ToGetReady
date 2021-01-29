# coding   : utf-8 
# @Time    : 21/01/29 9:40
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 并查集问题.py
# @Software: PyCharm


class UnionFind:
    """
    并查集通用模板
    """

    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.n = n
        self.setCount = n

    def findset(self, x):
        if self.parent == x:
            return x
        self.parent[x] = self.findset(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        x, y = self.findset(x), self.findset(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1
        return True

    def connected(self,x ,y):
        x, y = self.findset(x), self.findset(y)
        return x == y



class Solution:
    """
    并查集相关题目合集
    """
    def minimunEffortPath(self, heights):
        """
        01.29-每日一题，最小体力消耗路径
        :param heights:
        :return:
        """
        