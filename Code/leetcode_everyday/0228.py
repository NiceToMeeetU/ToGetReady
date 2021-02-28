# coding   : utf-8 
# @Time    : 21/02/28 9:24
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0228.py
# @Software: PyCharm


from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        """
        如果数组是单调递增或单调递减的，那么它是单调的。
        如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。
        当给定的数组 A 是单调数组时返回 true，否则返回 false。

        :param A:
        :return:
        """
        # 第一时间想到的偷鸡解法
        # return sorted(A) == A or sorted(A, reverse=True) == A

        # 正儿八经应该用两个布尔变量遍历即可
        increase, decrease = True, True
        for i in range(len(A) - 1):
            if A[i] < A[i + 1]:
                decrease = False
            if A[i] > A[i + 1]:
                increase= False
            if not increase and not decrease:
                return False
        return True
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        val_set = set()
        p = ListNode(-1)
        p.next = head
        while p.next:
            if p.next.val in val_set:
                p.next = p.next.next
            else:
                val_set.add(p.next.val)
                p = p.next

        return head

    def isPalindrome(self, head: ListNode) -> bool:
        """
        回文链表
        要求O(n)时间O(1)空间
        :param head:
        :return:
        单向链表无法从后往前寻
        所以这个时候就要想到用快慢指针了
        """
        # 直接遍历入列表，倒序比较
        # res = []
        # while head:
        #     res.append(head.val)
        #     head = head.next
        # return res == res[::-1]

        slow = head
        fast = head.next
        while fast and fast.next:  # 注意快慢指针的循环方法
            slow = slow.next
            fast = fast.next.next
        # 此时找到了链表中心即slow.next
        # 链表翻转
        p1, p2 = slow.next, None
        while p1:
            p1.next, p2, p1 = p2, p1, p1.next
        # p2即后半段的翻转结果
        while head and p2:
            if head.val != p2.val:
                return False
            head = head.next
            p2 = p2.next
        return True

    def test(self):
        ans = self.isMonotonic([3,2,2,1])
        print(ans)

if __name__ == '__main__':
    solution = Solution()
    solution.test()