# coding   : utf-8 
# @Time    : 21/03/22 15:14
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0324.py
# @Software: PyCharm


from typing import List


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


if __name__ == '__main__':
    solution = Solution()
    print(solution.nextPermutation([3,2,1]))