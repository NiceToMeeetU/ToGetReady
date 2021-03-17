# coding   : utf-8 
# @Time    : 21/03/17 8:57
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0317.py
# @Software: PyCharm


from typing import List


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        114. 不同的子序列
        造物弄人啊
        dp[i][j] = dp[i-1][j-1]
        :param s:
        :param t:
        :return:
        """
        m, n = len(s), len(t)
        if m < n:
            return 0
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m):
            dp[i][0] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if j > i:
                    continue
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[m][n]


    def longestPalindrome(self, s: str) -> str:
        """
        5. 最长回文子串
        dp[i,j] = dp[i-1, j+1] ^ (s[i]==s[j])
            dp[i,i] = True
            dp[i,i+1] = s[i] == s[i+1]
        """
        # n^2超时DP
        # n = len(s)
        # dp = [[False] * n for _ in range(n)]
        # res = ""
        # for l in range(n):
        #     for i in range(n):
        #         j = i + l
        #         if j >= n:
        #             break
        #         if l == 0:
        #             dp[i][j] = True
        #         elif l == 1:
        #             dp[i][j] = s[i] == s[j]
        #         elif l > 1:
        #             dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
        #
        #         if dp[i][j] and l + 1 > len(res):
        #             res = s[i:j + 1]
        # return res
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = s[0]
        if n < 2:
            return s
        for i in range(n):
            dp[i][i] = True
        for j in range(1, n):
            for i in range(0, j):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    elif j - i >= 3:
                        dp[i][j] = dp[i + 1][j - 1]

                if dp[i][j] and j - i + 1 > len(res):
                    res = s[i:j + 1]
        return res

    def maxArea(self, height: List[int]) -> int:
        """
        11. 盛最多水的容器
        """
        n = len(height)
        i, j = 0, n - 1
        res = 0
        while i < j:
            tmp = min(height[i], height[j]) * (j - i)
            res = max(tmp, res)
            if height[i] < height[j]:
                i += 1
            elif height[i] >= height[j]:
                j -= 1

        return res

    def letterCombinations(self, digits: str) -> List[str]:
        """
        17. 电话号码的字母组合
        DFS, 回溯
        """
        if not digits:
            return []
        dic = {2: "abc", 3: "def", 4: "ghi", 5: "jkl",
               6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}

        def backtrack(comb, digit):
            if len(digit) == 0:
                res.append(comb)
            else:
                for c in dic[digit[0]]:
                    backtrack(comb + c, digit[1:])

        res = []
        backtrack("", digits)
        return res

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        19. 删除链表的倒数第 N 个结点
        先后指针，先指针走了n步后，后指针出发，然后一起走
        :param head:
        :param n:
        :return:
        """
        ans = ListNode(-1)
        ans.next = head
        if not head or not head.next:
            return
        first, second = head, head
        for _ in range(n):
            first = first.next
        if not first:
            return head.next
        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next
        return ans.next

    def generateParenthesis(self, n: int) -> List[str]:
        """
        22. 括号生成
        又特么回溯，溯尼玛啊
        :param n:
        :return:
        """

    def flatten(self, root: TreeNode) -> None:
        """
        114. 二叉树展开为链表
        给你二叉树的根结点 root ，请你将它展开为一个单链表：
        展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，
        而左子指针始终为 null 。
        展开后的单链表应该与二叉树 先序遍历 顺序相同。

        原地遍历有点要命
        """
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)

        tmp = root.right
        root.right = root.left
        root.left = None
        while root.right:
            root = root.right
        root.right = tmp


    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        4. 寻找两个正序数组的中位数
        :param nums1:
        :param nums2:
        :return:
        """
        m, n = len(nums1), len(nums2)


if __name__ == '__main__':
    solution = Solution()
    print(solution)
