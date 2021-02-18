# coding   : utf-8 
# @Time    : 21/02/16 11:34
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 链表遍历相关问题.py
# @Software: PyCharm


"""
链表的遍历的巧妙用法
"""


class ListNode:
    """
    常规链表定义
    """

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        leetcode 第2题
        给定两个非空链表，表示两个非负整数，每位数字逆序排列，求两数之和，相同形式返回
        """
        carry = 0
        # 定义两个同样的链表，一个作为最终提交的答案，一个用来向后遍历
        # 最后只要从这个头节点的next提交即可
        ans = p = ListNode(val=None)

        while l1 or l2 or carry:
            carry += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            p.next = ListNode(carry % 10)
            p = p.next
            carry //= 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return ans.next

    def reverseList(self, head: ListNode) -> ListNode:
        """
        206 反转链表
        画个图就明白了
        :param head:
        :return:
        """
        p1, p2 = head, None
        while p1:
            p1.next, p2, p1 = p2, p1, p1.next
        return p2


l5 = ListNode(5, None)
l4 = ListNode(4, l5)
l3 = ListNode(3, l4)
l2 = ListNode(2, l3)
l1 = ListNode(1, l2)

solution = Solution()

ans = solution.reverseList(l1)
print(ans)
