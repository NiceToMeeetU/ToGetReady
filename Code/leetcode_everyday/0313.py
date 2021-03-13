# coding   : utf-8 
# @Time    : 21/03/13 10:02
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0313.py
# @Software: PyCharm


from typing import  List


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashset = []


    def add(self, key: int) -> None:
        if not self.contains(key):
            self.hashset.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.hashset.remove(key)


    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        for i in self.hashset:
            if i == key:
                return True
        return False


class NSum:
    """
    N-Sum问题系统来一遍
    问题分类为找一个和找不重复的所有。
    """
    def twoSum1(self, nums, target) -> List[int]:
        """
        无序的数组找一个直接用哈希表
        """
        dic = dict()
        for num in nums:
            if num in dic:
                return [num, dic[num]]
            dic[target - num] = num
        return []

    def threeSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        三数之和，返回所有可能的不重复的结果
        """
        res, n = [], len(nums)
        if n < 3: return res
        nums.sort()
        for p1 in range(n):
            if p1 > 0 and nums[p1] == nums[p1 - 1]:
                continue
            p3 = n - 1
            t = target - nums[p1]
            for p2 in range(p1 + 1, n):
                if p2 > p1 + 1 and nums[p2] == nums[p2 -1]:
                    continue
                while p2 < p3 and nums[p2] + nums[p3] > t:
                    p3 -= 1
                if p2 == p3:
                    break
                if nums[p2] + nums[p3] == t:
                    res.append([nums[p1], nums[p2], nums[p3]])
        return res

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        四数之和，返回所有可能的不重复的结果
        """
        res, n = set(), len(nums)
        if n < 4:
            return []
        nums.sort()
        for p1 in range(n):
            if p1 > 0 and nums[p1] == nums[p2]:
                continue
            for p2 in range(p1 + 1, n):
                if p2 > p1 + 1 and nums[p2] == nums[p2 - 1]:
                    continue
                p4 = n - 1
                t = target - nums[p1] - nums[p2]
                for p3 in range(p2 + 1, n):
                    if p3 > p2 + 1 and nums[p3] == nums[p3 - 1]:
                        continue
                    while p3 < p4 and nums[p3] + nums[p4] > t:
                        p4 -= 1
                    if p3 == p4:
                        break
                    if nums[p3] + nums[p4] == t:
                        res.add({nums[p1], nums[p2], nums[p3], nums[p4]})

        return [list(i) for i in res]


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        110. 平衡二叉树
        :param root:
        :return:
        """
        # 自顶而下 top-down
        def maxDepth(node):
            if not node:
                return 0
            return max(maxDepth(node.left), maxDepth(node.right)) + 1
        if not root:
            return True
        # return abs(maxDepth(root.left) - maxDepth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

        # 自底而上 bottom-up
        def height(node):
            if not node:
                return 0
            leftHeight = height(node.left)
            rightHeight = height(node.right)
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1
            else:
                return max(leftHeight, rightHeight) + 1
        return height(root) >= 0

