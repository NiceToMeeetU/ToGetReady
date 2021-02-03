# coding   : utf-8
# @Time    : 21/02/02 15:08
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : alpha.py
# @Software: PyCharm



class UnionFind:

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

    def connected(self, x, y):
        x, y = self.findset(x), self.findset(y)
        return x == y

class solution:
    def maxface(self, facmat):
        m,n = len(facmat), len(facmat[0])


