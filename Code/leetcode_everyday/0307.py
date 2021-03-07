# coding   : utf-8 
# @Time    : 21/03/07 14:38
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0307.py
# @Software: PyCharm


from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def partition(self, s: str) -> List[List[int]]:
        """
        131
        给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
        返回 s 所有可能的分割方案。
        """
        res = []

        def backtrack(ss: str, tmp: List):
            if not ss:
                res.append(tmp)
            for i in range(len(ss)):
                if ss[:i + 1] == ss[i::-1]:
                    backtrack(ss[i + 1:], tmp + [ss[:i + 1]])

        backtrack(s, [])
        return res

    def isValidBST(self, root: TreeNode) -> bool:
        """
        98 验证二叉搜索树
        二叉搜索树定义：
        1、所有的左子树节点都比根节点小；
        2、所有的右子树节点都比根节点大；
        3、左右左子树、右子树本身都是二叉搜索树。

        不能只判断左节点右节点，而是要看整个子树
        """

        # method 1，通过中序遍历树，判断前后是否始终保持升序
        # self.prev = None
        # def helper(node):
        #     if not node:
        #         return True
        #     if not helper(node.left):
        #         return False
        #     if self.prev and self.prev.val >= node.val:
        #         return False
        #     self.prev = node
        #     return helper(node.right)
        # return helper(root)

        # method 2，递归写法
        # 需要考率将阈值作为参数传递进去
        def helper(node: TreeNode, min_ = float("-inf"), max_= float("inf")):
            if not node:
                return True
            if node.val <= min_ or node.val >= max_:
                return False
            if not helper(node.left, min_, node.val):
                return False
            if not helper(node.right, node.val, max_):
                return False
            return True
        return helper(root)


    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        235、二叉搜索树的最近公共祖先
        """
        # 回顾普通二叉树最近公共祖先的求法
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        if not right:
            return left
        # return root

        # 但是二叉搜索树有数值关系，可以直接利用上简化问题
        # 只要两个两个节点与该根节点的相对大小关系不同，那么其必然位于不同的左右子树上
        if p.val < root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        # return root

        # 同样可以采用迭代的方法做
        while root:
            if p.val < root.val > q.val:
                root = root.left
            elif p.val > root.val < q.val:
                root = root.right
            else:
                return root


    # 16:38 专注刷完流到搜索二叉树问题
    # 二叉查找树（英语：Binary Search Tree），也称为 二叉搜索树、有序二叉树（Ordered Binary Tree）或排序二叉树（Sorted Binary Tree），是指一棵空树或者具有下列性质的二叉树：
    # 若任意节点的左子树不空，则左子树上所有节点的值均小于它的根节点的值；
    # 若任意节点的右子树不空，则右子树上所有节点的值均大于它的根节点的值；
    # 任意节点的左、右子树也分别为二叉查找树；
    # 没有键值相等的节点。
    # 二叉查找树相比于其他数据结构的优势在于查找、插入的时间复杂度较低。为 O(\log n)O(logn)。二叉查找树是基础性数据结构，用于构建更为抽象的数据结构，如集合、多重集、关联数组等。
    # 二叉查找树的查找过程和次优二叉树类似，通常采取二叉链表作为二叉查找树的存储结构。中序遍历二叉查找树可得到一个关键字的有序序列，一个无序序列可以通过构造一棵二叉查找树变成一个有序序列，构造树的过程即为对无序序列进行查找的过程。每次插入的新的结点都是二叉查找树上新的叶子结点，在进行插入操作时，不必移动其它结点，只需改动某个结点的指针，由空变为非空即可。搜索、插入、删除的复杂度等于树高，期望 O(\log n)O(logn)，最坏 O(n)O(n)（数列有序，树退化成线性表）。
    # 虽然二叉查找树的最坏效率是 O(n)O(n)，但它支持动态查询，且有很多改进版的二叉查找树可以使树高为 O(\log n)O(logn)，从而将最坏效率降至 O(\log n)O(logn)，如 AVL 树、红黑树等。
    def convertBiNode(self, root: TreeNode) -> TreeNode:
        """
        面试题 17.12. BiNode
        二叉树数据结构TreeNode可用来表示单向链表（其中left置空，right为下一个链表节点）。
        实现一个方法，把二叉搜索树转换为单向链表，要求依然符合二叉搜索树的性质，转换操作应是原址的，也就是在原始的二叉搜索树上直接修改。
        返回转换后的单向链表的头节点。
        """
        # if root:
        #     self.convertBiNode(root.left)
        #     if root.left:
        #         root.left.left = None
        #         root.left.right = root
        #         root.left = None
        #     self.convertBiNode(root.right)
        # return root

        # 迭代法
        head = TreeNode()
        pre = head # 设置一个前序节点用于不断遍历
        cur = root
        stack = []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            cur.left = None
            pre.right = cur
            pre = cur
            cur = cur.right
        # return head.right

        # 递归法
        def inorder_(node):
            if node:
                inorder_(node.left)
                node.left = None
                self.p.right = node
                self.p = node
                inorder_(node.right)
        head = TreeNode()
        self.p = head
        self.inorder_(root)

        return head.right

    def convertBST(self, root: TreeNode) -> TreeNode:
        """
        538. 把二叉搜索树转换为累加树
        给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），
        使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。
        提醒一下，二叉搜索树满足下列约束条件：
        节点的左子树仅包含键 小于 节点键的节点。
        节点的右子树仅包含键 大于 节点键的节点。
        左右子树也必须是二叉搜索树。
        """
