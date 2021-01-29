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

    def connected(self, x, y):
        x, y = self.findset(x), self.findset(y)
        return x == y


class Solution:
    """
    并查集相关题目合集
    """
    @staticmethod
    def minimunEffortPath(heights):
        """
        01.29-每日一题，最小体力消耗路径
        :param heights:
        :return:
        """
        m, n = len(heights), len(heights[0])
        edges = list()
        for i in range(m):
            for j in range(n):
                iden = i * n + j
                if i > 0:
                    edges.append((iden - n, iden, abs(heights[i][j] - heights[i - 1][j])))
                if j > 0:
                    edges.append((iden - 1, iden, abs(heights[i][j] - heights[i][j - 1])))
        edges.sort(key=lambda e: e[2])

        uf = UnionFind(m * n)
        ans = 0
        for x, y, v in edges:
            uf.unite(x, y)
            if uf.connected(0, m * n - 1):
                ans = v
                break
        return ans


if __name__ == '__main__':
    pass
    solution = Solution()
    solution.minimunEffortPath()