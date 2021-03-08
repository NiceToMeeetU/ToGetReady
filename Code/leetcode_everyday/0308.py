# coding   : utf-8 
# @Time    : 21/03/08 8:33
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0308.py
# @Software: PyCharm


from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCut(self, s: str) :
        """
        132. 分割回文串Ⅱ
        给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。
        返回符合要求的 最少分割次数 。
        :param s:
        :return:
        """
        n = len(s)
        g = [[True] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                g[i][j] = (s[i] == s[j]) and g[i + 1][j - 1]

        f = [float("inf")] * n
        for i in range(n):
            if g[0][i]:
                f[i] = 0
            else:
                for j in range(i):
                    if g[j + 1][i]:
                        f[i] = min(f[i], f[j] + 1)
        return f[n - 1]


    def kthSmallest(self, root: TreeNode, k:int):
        """
        230. 二叉搜索树中第K小的元素
        :param root:
        :param k:
        :return:
        不要只想着中序出结果
        """
        stack = []
        node = root
        while True:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            k -= 1
            if not k:
                return node.val
            node = node.right