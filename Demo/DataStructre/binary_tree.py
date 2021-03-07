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

    遍历基操
         1
       2   3
     4  5 6  7
    preorder:   1 2 4 5 3 6 7   根左右
    inorder:    4 2 5 1 6 3 7   左根右
    postorder:  4 5 2 6 7 3 1   左右根
    除开根节点以外的部分一定是左右对应的

    03.07 重写极简版递归基操
    """
    def __init__(self):
        self.traversalpath = []

    def preorder_(self,root):
        if root:
            self.traversalpath.append(root.val)
            self.preorder_(root.left)
            self.preorder_(root.right)
    def inorder_(self,root):
        if root:
            self.inorder_(root.left)
            self.traversalpath.append(root.val)
            self.inorder_(root.right)
    def postorder_(self,root):
        if root:
            self.postorder_(root.left)
            self.postorder_(root.right)
            self.traversalpath.append(root.val)

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
        101
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
        if not root or not (root.left or root.right):  # 涉及对称的条件方法，直接判断是否平衡
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
        def helper(left_, right_):
            if not (left_ or right_):  # 两个节点都为空
                return True
            if not (left_ and right_):  # 两个节点只有一个为空
                return False
            if left_.val != right_.val:
                return False
            # 这里极其容易错，注意！
            return helper(left_.left, right_.right) and helper(left_.right, right_.left)

        return helper(root, root)

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        """
        112 路径总和
        """
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum == root.val
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)


class ReBuild:
    """
    逆向遍历基操
         1
       2   3
     4  5 6  7
    preorder:   1 2 4 5 3 6 7   根左右
    inorder:    4 2 5 1 6 3 7   左根右
    postorder:  4 5 2 6 7 3 1   左右根
    除开根节点以外的部分一定是左右对应的
    前序的首位必然是根节点，末位必然是最右下角的子树
    中序的首位必然是最左下角的子树，末位必然是最右下角的子树
    后序的首位必然是最左下角的子树，末位必然是根节点
    根节点在中序遍历结果中把整棵树分成了左右树
    没有中序遍历的话，前序遍历的[1]是根节点的左节点，
    该节点在后序遍历中是左侧子树最后一个遍历到的
    还是离不开递归思想

    1、找根节点
    2、确定左右子树节点数
    3、递归
    """

    def buildTreeInPost(self, inorder: List[int], postorder: List[int]):
        """
        从中序与后序遍历序列构造二叉树
        根据一棵树的中序遍历与后序遍历构造二叉树。
        注意:
        你可以假设树中没有重复的元素。
        :param inorder:[9,3,15,20,7]
        :param postorder:[9,15,7,20,3]
        :return:

        """
        if not postorder:
            return None
        root = TreeNode(postorder[-1])
        L = inorder.index(root.val)  # 最关键的步骤，可用哈希表优化
        root.left = self.buildTree(inorder[:L], postorder[:L])
        root.right = self.buildTree(inorder[L + 1:], postorder[L:-1])
        return root

    def buildTreePreIn(self, preorder: List[int], inorder: List[int]):
        """
        根据一棵树的前序遍历与中序遍历构造二叉树。
        :param preorder:
        :param inorder:
        :return:
        """
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        L = inorder.index(root.val)  # 最关键的步骤
        root.left = self.buildTreePreIn(preorder[1:L + 1], inorder[:L])
        root.right = self.buildTreePreIn(preorder[L + 1:], inorder[L + 1:])
        return root

    # 按照同样的index查找根节点位置从而确定左右子树数量的思路无法解决前后遍历的重建，换思路！
    # 其实也还是可以的
    def buildTreePrePost(self, preorder: List[int], postorder: List[int]):
        """
        根据一棵树的前序遍历与后序遍历构造二叉树。
        如果没有中序的遍历，那么就不能明确左右子树的数量
        前序遍历的[1]是根节点的左节点，
        该节点在后序遍历中是左侧子树最后一个遍历到的
        由此即可以确定左子树的数量
        """
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        L = postorder.index(preorder[1]) + 1  # 最关键的步骤
        root.left = self.buildTreePrePost(preorder[1:L + 1], postorder[:L])
        root.right = self.buildTreePrePost(preorder[L + 1:], postorder[L: -1])
        return root

    # 递归法写完，同样地再来一遍迭代方法加强理解
    def buildTreePreIn_(self, preorder: List[int], inorder: List[int]):
        """
        迭代法从前序中序遍历重建二叉树
        1、用栈和指针重建二叉树，初始栈中存放根节点，指针指向中序遍历的第一个节点；
        2、依次枚举前序遍历[1:]所有节点，
                如果index恰好指向栈顶节点，则不断弹出栈顶节点并向右移动index，并将当前节点作为最后一个弹出的节点的右儿子；
                如果index和栈顶节点不同，则将当前节点作为栈顶节点的做儿子；
        3、最后将当前节点入栈。
        """
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        stack = [root]
        inorderIndex = 0
        for i in range(1, len(preorder)):
            preorderVal = preorder[i]
            node = stack[-1]
            if node.val != inorder[inorderIndex]:
                node.left = TreeNode(preorderVal)
                stack.append(node.left)
            else:
                while stack and stack[-1].val == inorder[inorderIndex]:
                    node = stack.pop()
                    inorderIndex += 1
                node.right = TreeNode(preorderVal)
                stack.append(node.right)
        return root

    def buildTreePrePost_(self, preorder: List[int], postorder: List[int]):
        """
        迭代法从前序后序遍历中重建二叉树
        不写了，抄一个基于队列的迭代方法
        """
        addedNodes = set(preorder[0])
        dq = collections.deque([preorder[0]])
        res = dq[0]
        pre2id = {node: idx for idx, node in enumerate(preorder)}
        post2id = {node: idx for idx, node in enumerate(postorder)}
        n = len(preorder)
        while len(addedNodes) < n:
            root = dq.popleft()
            in_pos, post_pos = pre2id[root.val], post2id[root.val]
            left, right = preorder[min(in_pos + 1, n - 1)], postorder[post_pos - 1]
            if left not in addedNodes:
                root.left = TreeNode(left)
                dq.append(root.left)
                addedNodes.add(left)
            if right not in  addedNodes:
                root.right = TreeNode(right)
                dq.append(root.right)
                addedNodes.add(right)
            return res




