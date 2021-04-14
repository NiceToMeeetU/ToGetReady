# coding   : utf-8 
# @Time    : 21/04/14 10:19
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0414.py
# @Software: PyCharm


import collections


class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.isword = False


class Trie:
    """
    208. 实现Trie前缀树

    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curNode = self.root
        for w in word:
            curNode = curNode.children[w]
        curNode.isword = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curNode = self.root
        for w in word:
            curNode = curNode.children.get(w)
            if not curNode:
                return False
        return curNode.isword

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curNode = self.root
        for w in prefix:
            curNode = curNode.children.get(w)
            if not curNode:
                return False
        return True

class Trie1:
    """
    不用字典，直接数组构建前缀树
    """
    def __init__(self):
        self.chlidren = [None] * 26
        self.isword = False

    def searchPrefic(self, prefic: str):
        node = self
        for c in prefic:
            c = ord(c) - ord('a')
            if not node.chlidren[c]:
                return None
            node = node.chlidren[c]
        return node

    def insert(self, word: str) -> None:
        node = self
        for w in word:
            w = ord(w) - ord("a")
            if not node.chlidren[w]:
                node.chlidren[w] = Trie1()
            node = node.chlidren[w]
        node.isword = True


    def search(self, word: str) -> bool:
        node = self.searchPrefic(word)
        return node is not None and node.isword

    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefic(prefix) is not None
