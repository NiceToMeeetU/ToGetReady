# coding   : utf-8 
# @Time    : 21/03/25 15:10
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0325.py
# @Software: PyCharm


from typing import List


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


class Solution:
    def deleteDuplicate(self, head: ListNode) -> ListNode:
        """
        有序链表去重
        :param head:
        :return:
        """

        if not head or not head.next:
            return head
        head.next = self.deleteDuplicate(head.next)
        if head.val == head.next.val:
            head = head.next
        return head

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        82. 删除排序链表中的重复元素 II
        存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除链表中所有存在数字重复情况的节点，
        只保留原始链表中没有重复出现的数字。返回同样按升序排列的结果链表

        已排序则不需要使用哈希集合，直接遍历即可
        """

        if not head or not head.next:
            return head
        res = ListNode(-1, head)
        curNode = res
        while curNode.next and curNode.next.next:
            if curNode.next.val == curNode.next.next.val:
                tmp = curNode.next.val
                while curNode.next and curNode.next == tmp:
                    curNode.next = curNode.next.next
            else:
                curNode = curNode.next
        return res.next

    def longestConsecutive(self, nums: List[int]) -> int:
        """
        128. 最长连续序列
        给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
        进阶：你可以设计并实现时间复杂度为O(n) 的解决方案吗？
        :param nums:
        :return:
        又特么字符串动态规划
        哦不
        是字符串并查集
        厚礼蟹
        用哈希表存储每个端点值对应连续区间的长度
            若数已在哈希表中：跳过不做处理
            若是新数加入：
            取出其左右相邻数已有的连续区间长度 left 和 right
            计算当前数的区间长度为：cur_length = left + right + 1
            根据 cur_length 更新最大长度 max_length 的值
            更新区间两端点的长度值
        """
        if not nums:
            return 0
        nums = list(set(nums))
        nums.sort()
        res = 1
        i = 1
        while i < len(nums):
            tmp = 1

            while i < len(nums) and nums[i] - nums[i - 1] == 1:
                tmp += 1
                i += 1
            i += 1
            res = max(tmp, res)
        # return res

        # 暴力居然可以通过
        # 继续考虑O(n)方法
        hashLength = dict()
        res = 0
        for num in nums:
            if num not in hashLength:
                left = hashLength.get(num - 1, 0)
                right = hashLength.get(num + 1, 0)
                curLength = left + right + 1

                res = max(res, curLength)

                hashLength[num] = curLength
                hashLength[num - left] = curLength
                hashLength[num + right] = curLength
        return res

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        48. 旋转图像
        n × n 二维数组 原地 顺时针旋转90°
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(1, n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for l in range(n):
            matrix[l] = matrix[l][::-1]
        return

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        39. 组合总和
        :param candidates:
        :param target:
        :return:
        """
        res = []
        n = len(candidates)
        path = []

        def backtrack(idx, curSum):
            if idx == n or curSum > target:
                return
            elif curSum == target:
                res.append(path[:])
                return
            backtrack(idx + 1, curSum)
            if curSum + candidates[idx] <= target:
                path.append(candidates[idx])
                backtrack(idx, curSum + candidates[idx])
                path.pop()

        backtrack(0, 0)
        return res

    def binarySearch(self, nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            elif target == nums[mid]:
                return True
        return False

    def search(self, nums: List[int], target: int) -> int:
        """
        33. 搜索旋转排序数组
        O(logn)
        二分法处理
        """
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid

            if nums[0] <= nums[mid]:  # mid在左侧有序数组上
                if nums[0] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # mid在右侧有序数组上
                if nums[mid] < target <= nums[-1]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

    def generateParenthesis(self, n: int) -> List[str]:
        """
        22. 括号生成
        :param n:
        :return:
        """
        # 回溯法
        res = []
        def backtrack(s, left, right):
            if len(s) == 2 * n:
                res.append("".join(s))
                return

            if left < n:
                s.append("(")
                backtrack(s, left + 1, right)
                s.pop()

            if right < left:
                s.append(")")
                backtrack(s, left, right + 1)
                s.pop()
        backtrack([], 0, 0)
        # return res

        # 动态规划法
        dp = [[] for _ in range(n + 1)]
        dp[0] = [""]
        for i in range(1, n + 1):
            for p in range(i):
                for k1 in dp[p]:
                    for k2 in dp[i - 1 - p]:
                        dp[i].append(f"({k1}){k2}")
        return dp[n]


if __name__ == '__main__':
    solution = Solution()
    # print(solution.longestConsecutive([100, 1, 300, 2, 3, 4]))
    print(solution.search([4, 5, 6, 7, 0, 1, 2], 0) == 4)
    print(solution.search([4, 5, 6, 7, 0, 1, 2], 3) == -1)
