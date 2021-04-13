# coding   : utf-8 
# @Time    : 21/04/13 9:14
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0413.py
# @Software: PyCharm


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        """
        求二叉搜索树树中任意不同节点值之间的最小差值
        :param root:
        :return:
        """
        res = []
        def inorder(node: TreeNode):
            if node:
                inorder(node.left)
                res.append(node.val)
                inorder(node.right)

        inorder(root)
        res = [res[i] - res[i - 1] for i in range(1, len(res))]
        return min(res)






