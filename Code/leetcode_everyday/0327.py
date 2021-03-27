# coding   : utf-8 
# @Time    : 21/03/27 9:17
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0327.py
# @Software: PyCharm


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """
        61. 旋转链表
        给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
        """
        if not head or not head.next:
            return head

        length = 1
        node = head
        while node.next:
            node = node.next
            length += 1

        print(f"{length = }")
        k = k % length

        if k == 0:
            return head

        node.next = head
        for _ in range(length - k -1):
            head = head.next
        res = head.next
        head.next = None
        return  res


if __name__ == '__main__':
    test = ListNode(1, ListNode(2,ListNode(3, ListNode(4, ListNode(5)))))
    k = 2
    solution = Solution()
    ans = solution.rotateRight(test, 2)





