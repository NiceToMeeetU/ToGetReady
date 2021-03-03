# coding   : utf-8 
# @Time    : 21/03/03 9:27
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : binary_tree.py
# @Software: PyCharm


"""
二叉树的基本学习
- 树的遍历
- 递归解决问题
"""

import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Traverse:
    """
    - 二叉树遍历
        深度优先搜索 —— 栈
            前序遍历
            中序遍历
            后序遍历
        广度优先搜索 —— 队列
            层序遍历
    """

    def preorderTraversalRecursion(self, root: TreeNode):
        """
        二叉树的前序遍历，递归法

        """
        res = []

        def helper(node):
            if not node:
                return

            res.append(node.val)  # 遍历过程内需要的具体操作

            helper(node.left)
            helper(node.right)

        helper(root)
        return res

    def inorderTraversalRecursion(self, root: TreeNode):
        """
        二叉树的中序遍历，递归法
        """
        res = []

        def helper(node):
            if not node:
                return
            helper(node.left)
            res.append(node.val)
            helper(node.right)

        helper(root)
        return res

    def postorderTraversalRecursion(self, root: TreeNode):
        """
        二叉树的后序遍历，递归法
        """
        res = []

        def helper(node):
            if not node:
                return
            helper(node.left)
            helper(node.right)
            res.append(node.val)

        helper(root)
        return res

    # 递归法时间空间都是O(n)，在调用递归函数的顺序上体现遍历顺序
    # 迭代法需要维护栈。时间空间也都是O(n)

    def preorderTraversalIteration0(self, root: TreeNode):
        """
        二叉树的前序遍历，迭代法
        迭代法实现二叉树遍历需要自己构建栈
        前序遍历那就先压入右侧再压入左侧
        """
        # 自己写的方法一，不够直观
        res = []
        stack = [root]
        while stack:
            tmp = pop()
            if not tmp:
                continue
            res.append(tmp.val)  # 具体的遍历任务
            stack.append(tmp.right)
            stack.append(tmp.left)
        return res

    def preorderTraversalIteration(self, root: TreeNode):
        """
        二叉树的前序遍历，迭代法
        """
        res = []
        stack = []
        node = root
        while stack or node:
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return res

    def inorderTraversalIteration(self, root: TreeNode):
        """
        二叉树的中序遍历，迭代法
        """
        res = []
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res

    def postorderTraversalIteration(self, root: TreeNode):
        """
        二叉树的后序遍历，迭代法
        """
        res = []
        stack = []
        node = root
        prev = None
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if not node.right or node.right == prev:
                res.append(node.val)
                prev = node
                node = Node
            else:
                stack.append(node)
                node = node.right

        return res

    def levelOrder(self, root: TreeNode):
        """
        层序遍历
        每一层全部放入一个队列内即可，从上一层遍历的过程即把下一层的所有节点放入队列
        """
        res = []
        if not root:
            return res
        queue = collections.deque([root])
        while queue:
            level = len(queue)  # 第N层最多有N个节点
            tmp = []
            for i in range(level):
                curNode = queue.popleft()
                tmp.append(curNode.val)
                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)
            res.append(tmp)
        return res


class RecursionProblem:
    """
    递归是解决树的相关问题最有效最常用的方法
    深刻把握住递归是数的基本特性的原则
    通常有两种解决方案：
        自顶而下    Top-Down
            先访问节点，再递归调用函数将值传向子节点
            可以认为是一种前序遍历

            def top_down(root, params):
                return specific value for null node
                update the answer if needed
                left_ans = top_down(root.left, left_params)
                right_ans = top_down(root.right, right_params)
                return the answer if needed

        自底而上    Buttom-Up
            首先对所有子节点递归调用函数，然后根据返回值和根节点本身的值得到答案。
            可以认为是一种后序遍历

            return specific value for null node
            left_ans = bottom_up(root.left)			// call function recursively for left child
            right_ans = bottom_up(root.right)		// call function recursively for right child
            return answers                           // answer <-- left_ans, right_ans, root.val

    遇到问题时思考：
    1、能确定一些参数，从该节点自身解决出发寻找答案吗？
    2、可以使用这些参数和节点本身的值来决定说明应该是传递给它子节点的参数吗？

    """

    def maxDepth(self, root: TreeNode) -> int:
        """
        求树的最大深度
        """
        # DFS 后序遍历深度优先搜索
        # if not root:
        #     return 0
        # return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

        # BFS 层序遍历广度优先搜索
        if not root:
            return 0
        res = 0
        queue = [root]
        while queue:
            tmp = []
            for node in queue:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            queue = tmp
            res += 1
        return res


    def isSymmetric(self, root: TreeNode) -> bool:
        """
        给定一个二叉树，检查它是否是镜像对称的。
        递归和迭代的写法必然会有很多的共通之处

        """
        # 第一遍写成了判断形状，其实题目是要求值和结构，垃圾写法，撂过
        if not root:
            return True
        queue = collections.deque([root])
        while queue:
            level = len(queue)
            tmp = []
            for i in range(level):
                curNode = queue.popleft()
                if curNode.left:
                    queue.append(curNode.left)
                    tmp.append(curNode.left.val)
                else:
                    tmp.append(None)
                if curNode.right:
                    queue.append(curNode.right)
                    tmp.append(curNode.right.val)
                else:
                    tmp.append(None)
            if tmp != tmp[::-1]:
                return False
        # return True
        #####
        # 迭代
        if not root or not (root.left or root.right): # 涉及对称的条件方法，直接判断是否平衡
            return True
        queue_ = [root.left, root.right]
        while queue_:
            left = queue_.pop(0)
            right = queue_.pop(0)
            if not (left or right):
                continue
            if not (left and right):
                return False
            if left.val != right.val:
                return False

            # 关键来了，依次按顺序放入队列
            queue_.append(left.left)
            queue_.append(right.right)
            queue_.append(left.right)
            queue_.append(right.left)

        # return True

        # 递归
        def helper(left, right):
            if not (left or right):     # 两个节点都为空
                return True
            if not (left and right):    # 两个节点只有一个为空
                return False
            if left.val != right.val:
                return False
            # 这里极其容易错，注意！
            return helper(left.left, right.right) and helper(left.right, right.left)

        return helper(root, root)



