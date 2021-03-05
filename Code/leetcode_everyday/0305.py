# coding   : utf-8 
# @Time    : 21/03/05 11:02
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0305.py
# @Software: PyCharm


from typing import List
import collections


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next_: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next_


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
        给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
        百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，
        最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
        向上回溯找祖先
        """
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        if not right:
            return left
        return root

    def reverseList(self, head: ListNode) -> ListNode:
        """
        递归反转列表
        :param head:
        :return:
        """
        if not head or not head.next:
            return head
        res = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return res

    def reverseListToN(self, head: ListNode, n: int):
        """
        反转从head为起点的n个节点
        """
        nonlocal successor
        if n == 1:
            successor = head.next
            return head
        res = self.reverseListToN(head.next, n - 1)
        head.next.next = head
        head.next = successor
        return res

    def reverseBetween(self, head: ListNode, left, right):
        """
        92 反转从m到n的链表
        依然是递归的思想
        """
        if left == 1:
            return self.reverseListToN(head, right)
        head.next = self.reverseBetween(head, left - 1, right - 1)
        return head


class ListNode(object):
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


if __name__ == '__main__':
    pass
