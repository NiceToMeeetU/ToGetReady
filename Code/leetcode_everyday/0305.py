# coding   : utf-8 
# @Time    : 21/03/05 11:02
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0305.py
# @Software: PyCharm


from typing import List
import collections

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        117. 填充每个节点的下一个右侧节点指针
        给定一个(完美）二叉树

        struct Node {
          int val;
          Node *left;
          Node *right;
          Node *next;
        }
        填充它的每个 next 指针，让这个指针指向其下一个右侧节点。
        如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
        初始状态下，所有 next 指针都被设置为 NULL。
        """
        # 完美二叉树的话直接遍历即可
        if not root:
            return root
        leftmost = root
        while leftmost.left:
            head = leftmost
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left
        # return root

        # 普通二叉树按照层序遍历方法解决：
        # 可以考虑通过在上一层为下一层提前设定链表的方式来将空间n -> 1
        if not root:
            return root
        queue = collections.deque([root])
        while queue:
            level = len(queue)
            tmp = None
            for i in range(level):
                curNode = queue.popleft()
                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)
                if i != 0:
                    tmp.next = curNode
                tmp = curNode
        return root


    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """

        :param root:
        :param p:
        :param q:
        :return:
        """
if __name__ == '__main__':
    pass
