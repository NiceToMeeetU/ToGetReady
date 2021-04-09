# coding   : utf-8 
# @Time    : 21/04/05 10:45
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0405.py
# @Software: PyCharm


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """

        :param word1:
        :param word2:
        :return:
        """
        dic = dict()

