# coding   : utf-8 
# @Time    : 21/04/03 15:41
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0403.py
# @Software: PyCharm


from typing import List


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        1143. 最长公共子序列
        不改变顺序，不需要连续
        :param text1:
        :param text2:
        :return:
        """
        m, n = len(text1), len(text2)
        pre = [0] * (n + 1)
        dp = [0] * (n + 1)
        for i in range(m):
            for j in range(1, n + 1):
                if text1[i] == text2[j - 1]:
                    dp[j] = pre[j - 1] + 1
                else:
                    dp[j] = max(pre[j], dp[j - 1])
                pre[j - 1] = dp[j - 1]
            pre[j] = dp[j]
        return dp[-1]

    def grayCode(self, n: int) -> List[int]:
        """
        89. 格雷编码
        格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。
        给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。即使有多个不同答案，你也只需要返回其中一种。
        格雷编码序列必须以 0 开头。

        回溯算法
        """
        res = []
        for i in range(1 << n):
            res.append(i ^ i >> 1)
        return res


import collections


class LRUCache(collections.OrderedDict):
    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)


class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUcache:
    def __init__(self, capacity: int):
        pass
        self.cap = capacity
        self.cache = dict()
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, key: int) -> int:
        pass
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = DLinkedNode(key, value)
            self.cache[key] = node
            self.addToHead(node)
            self.size += 1
            if self.size > self.cap:
                removed = self.removeTail()
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)


    def addToHead(self, node: DLinkedNode) -> Mone:
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node: DLinkedNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node: DLinkedNode) -> None:
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self) -> DLinkedNode:
        node = self.tail.prev
        self.removeNode(node)
        return node