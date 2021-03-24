# coding   : utf-8 
# @Time    : 21/03/22 15:14
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0324.py
# @Software: PyCharm


from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        先找出最大的索引 k 满足 nums[k] < nums[k+1]，如果不存在，就翻转整个数组；
        再找出另一个最大索引 l 满足 nums[l] > nums[k]；
        交换 nums[l] 和 nums[k]；
        最后翻转 nums[k+1:]。
        """
        for k in range(len(nums) - 2, -1, -1):
            if nums[k] < nums[k + 1]:
                # do something
                for l in range(len(nums) - 1, -1, -1):
                    if nums[l] > nums[k]:
                        nums[l], nums[k] = nums[k], nums[l]
                        break
                nums = nums[:k + 1] + nums[-1:k:-1]
                return
        nums = nums[::-1]
        return

    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return
        ans = ListNode(-1)
        ans.next = head
        node = ans
        while node and node.next:
            if node.next.val == val:
                if node.next.next:
                    node.next = node.next
                else:
                    node.next = None
            node = node.next
        return ans.next

    def sortList(self, head: ListNode) -> ListNode:
        """
        链表排序
        1、top-down
        找到链表的中点，以中点为分界，将链表拆分成两个子链表。寻找链表的中点可以使用快慢指针的做法，
        快指针每次移动 22 步，慢指针每次移动 11 步，当快指针到达链表末尾时，慢指针指向的链表节点即为链表的中点。
        对两个子链表分别排序。
        将两个排序后的子链表合并，得到完整的排序后的链表。可以使用「21. 合并两个有序链表」的做法，将两个有序的子链表进行合并。

        2、bottom-up
        用 \textit{subLength}subLength 表示每次需要排序的子链表的长度，初始时 \textit{subLength}=1subLength=1。

        每次将链表拆分成若干个长度为 \textit{subLength}subLength 的子链表（最后一个子链表的长度可以小于 \textit{subLength}subLength），按照每两个子链表一组进行合并，合并后即可得到若干个长度为 \textit{subLength} \times 2subLength×2 的有序子链表（最后一个子链表的长度可以小于 \textit{subLength} \times 2subLength×2）。合并两个子链表仍然使用「21. 合并两个有序链表」的做法。

        将 \textit{subLength}subLength 的值加倍，重复第 2 步，对更长的有序子链表进行合并操作，直到有序子链表的长度大于或等于 \textit{length}length，整个链表排序完毕
        :param head:
        :return:
        """

        def mergeSort(head_: ListNode, tail: ListNode) -> ListNode:
            if not head_:
                return head_
            if head_.next == tail:
                head_.next = None
                return head_
            slow, fast = head_, head_
            while fast != tail:
                slow = slow.next
                fast = fast.next
                if fast != tail:
                    fast = fast.next
            mid = slow
            return merge(mergeSort(head_, mid), mergeSort(mid, tail))

        def merge(node1: ListNode, node2: ListNode):
            """
            递归合并有序链表
            :param node1:
            :param node2:
            :return:
            """
            if node1 and node2:
                if node1.val > node2.val:
                    node1, node2 = node2, node1
                node1.next = merge(node1.next, node2)
            return node1 or node2

        # return mergeSort(head, None)

        # bottom-up
        def mergeList(l1, l2):
            """
            迭代合并有序链表的方法
            :param l1:
            :param l2:
            :return:
            """
            dumphead = ListNode(-1)
            temp0, temp1, temp2 = dumphead, l1, l2
            while temp1 and temp2:
                if temp1.val <= temp2.val:
                    temp0.next = temp1
                    temp1 = temp1.next
                else:
                    temp0.next = temp2
                    temp2 = temp2.next
                temp0 = temp0.next

            if temp1:
                temp0.next = temp1
            elif temp2:
                temp0.next = temp2
            return dumphead.next

        if not head:
            return head
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        ans = ListNode(-1, head)
        subLength = 1
        while subLength < length:
            pre, h = ans, ans.next
            while h:
                h1, i = h, subLength
                while i and h:
                    h = h.next
                    i -= 1
                if i:
                    break

                h2, i = h, subLength
                while i and h:
                    h = h.next
                    i -= 1
                c1, c2 = subLength, subLength - i
                while c1 and c2:
                    if h1.val < h2.val:
                        pre.next, h1 = h1, h1.next
                        c1 -= 1
                    else:
                        pre.next, h2 = h2, h2.next
                        c2 -= 1
                    pre = pre.next

                pre.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0:
                    pre = pre.next
                    c1 -= 1
                    c2 -= 1
                pre.next = h
            subLength *= 2
        return ans.next

    def mergeKLists(self, lists: List[ListNode]):
        """
        23. 合并K个升序链表
        :param lists:
        :return:
        """
        def mergeTwo1(l1, l2):
            """
            递归合并有序链表
            """
            if l1 and l2:
                if l1.val > l2.val:
                    l1, l2 = l2, l1
                l1.next = mergeTwo(l1.next, l2)
            return l1 or l2

        def mergeTwo2(l1, l2):
            """
            迭代合并有序链表
            """
            res = ListNode(-1)
            t0, t1, t2 = res, l1, l2
            while t1 and t2:
                if t1.val <= t2.val:
                    t0.next, t1 = t1, t1.next
                else:
                    t0.next, t2 = t2, t2.next
                t0 = t0.next
            if t1:
                t0.next = t1
            elif t2:
                t0.next = t2
            return res.next

        # 合并K个，分而治之？
        n = len(lists)
        if n == 0:
            return lists
        if n == 1:
            return lists[0]

        tmp = mergeTwo2(lists[0], Lists[1])
        for i in range(2, n):
            tmp = mergeTwo2(tmp, lists[i])
        return tmp



if __name__ == '__main__':
    solution = Solution()
    print(solution.nextPermutation([3, 2, 1]))
