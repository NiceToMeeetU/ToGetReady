# coding   : utf-8 
# @Time    : 21/03/30 10:39
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0330.py
# @Software: PyCharm


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """
        25. K 个一组翻转链表
        给你一个链表，每k个节点一组进行翻转，请你返回翻转后的链表。

        k是一个正整数，它的值小于或等于链表的长度。

        如果节点总数不是k的整数倍，那么请将最后剩余的节点保持原有顺序。

        进阶：

        你可以设计一个只使用常数额外空间的算法来解决此问题吗？
        你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

        :param head:
        :param k:
        :return:
        base case 不太好处理
        """
        if not head or not head.next:
            return head

        n1, n2 = head, head
        for _ in range(k):
            if not n2:
                return head
            n2 = n2.next
        # n1 起， n2 止
        res = None
        while n1 != n2:
            n1.next, tmp, n1 = tmp, n1, n1.next
        head.next = self.reverseKGroup(n2, k)
        return res

    def reorderList(self, head: ListNode) -> None:
        """
        132. 重排链表
        前后交叉重排
        :param head:
        :return:
        先把后半段反转，然后遍历合并？
        """
        # slow, fast = head, head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next

        # tmp = None
        # while slow:
        #     slow.next, tmp, slow = tmp, slow, slow.next
        #
        # p1, p2 = head, tmp
        # while p1 and p2:
        #     # 合并两个链表
        #     p1.next = p2
        #     tmp = p2.next
        #     p2.next = p1.next
        #     p1 = p1.next
        #     p2 = tmp
        # return head

        def findMiddle(head_: ListNode):
            """
            找到链表的中点
            """
            slow, fast = head_, head_
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def reverse(head_: ListNode):
            """
            反转链表
            """
            p1, p2 = head_, None
            while p1:
                p1.next, p2, p1 = p2, p1, p1.next
            return p2

        def merge(n1: ListNode, n2: ListNode):
            """
            交替合并两个链表
            """
            # 递归的写法不太友好
            if not n1:
                return n2
            if not n2:
                return n1
            tmp1 = n1.next
            tmp2 = n2.next
            n1.next = n2
            n2.next = merge(tmp1, tmp2)

            return n1

            # 重写个迭代的
            while not n1 and not n2:
                tmp1 = n1.next
                tmp2 = n2.next
                n1.next = n2
                n1 = tmp1
                n2.next = n1
                n2 = tmp2
                # 放大招
                n1,n2,n1.next,n2.next = n1.next, n2.next, n2, n1


        mid = findMiddle(head)
        l1 = head
        l2 = mid.next
        mid.next = None
        l2 = reverse(l2)
        merge(l1, l2)

