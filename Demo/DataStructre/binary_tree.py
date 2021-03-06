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
- 二叉搜索树相关
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

    def preorder_(self, root):
        if root:
            self.traversalpath.append(root.val)
            self.preorder_(root.left)
            self.preorder_(root.right)

    def inorder_(self, root):
        if root:
            self.inorder_(root.left)
            self.traversalpath.append(root.val)
            self.inorder_(root.right)

    def postorder_(self, root):
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
            for _ in range(level):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)
        return res

    def levelOrderRecursion(self, root: TreeNode):
        """
        层序遍历的递归实现
        """
        def bfs(node, level):
            if not node:
                return
            res[level - 1].append(node.val)
            if len(res) == level:
                res.append([])
            bfs(node.left, level + 1)
            bfs(node.right, level + 1)
        res = [[]]
        bfs(root, 1)
        return res[1:]

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

    def countNodes(self, root: TreeNode) -> int:
        """
        222. 完全二叉树的节点个数
        普通二叉树节点个数直接遍历解决，O(n)
        满二叉树节点个数求层深h，2^h - 1，O(logn)
        完全二叉树考虑其子树必然有一个满二叉树和完全二叉树
        所以不需要遍历，同样按深度求解即可
        """
        import math
        l, r = root, root
        ld, rd = 0, 0
        while l:
            l = l.left
            ld += 1
        while r:
            r = r.right
            rd += 1
        if ld == rd:
            return int(math.pow(2, rd)) - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1


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
        # return root

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
        L = inorder.index(root.val)  # 最关键的步骤，可用哈希表优化
        root.left = self.buildTreePreIn(preorder[1:L + 1], inorder[:L])
        root.right = self.buildTreePreIn(preorder[L + 1:], inorder[L + 1:])

        # return root

        # 再写一个带辅助函数哈希表优化的方法：
        def recur(root_idx, left, right):
            if left > right:
                return
            node = TreeNode(preorder[root_idx])
            i_ = dic[preorder[root_idx]]  # 查找其在中序遍历的位置
            node.left = recur(root_idx + 1, left, i_ - 1)
            node.right = recur(i_ - left + root_idx + 1, i_ + 1, right)
            return node

        dic = {}
        for i in range(len(inorder)):
            dic[inorder[i]] = i
        return recur(0, 0, len(inorder) - 1)

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
    # 实测迭代法快的多的多啊
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
        idx = 0
        for i in range(1, len(preorder)):
            preVal = preorder[i]
            node = stack[-1]
            if node.val != inorder[idx]:
                node.left = TreeNode(preVal)
                stack.append(node.left)
            else:
                while stack and stack[-1].val == inorder[idx]:
                    node = stack.pop()
                    idx += 1
                node.right = TreeNode(preVal)
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
            if right not in addedNodes:
                root.right = TreeNode(right)
                dq.append(root.right)
                addedNodes.add(right)
            return res


class BST:
    """
    二叉搜索树相关问题
    - 验证
    - 增删改查
    - 经典问题相比于普通二叉树的不同

       二叉搜索树定义：
    1、所有的左子树节点都比根节点小；
    2、所有的右子树节点都比根节点大；
    3、左右左子树、右子树本身都是二叉搜索树。

    不能只判断左节点右节点，而是要看整个子树
    反正不会做了就中序遍历
    """

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
        self.prev = None

        def helper1(node):
            if not node:
                return True
            if not helper1(node.left):
                return False
            if self.prev and self.prev.val >= node.val:
                return False
            self.prev = node
            return helper1(node.right)

        # return helper(root)

        # method 2，递归写法
        # 需要考率将阈值作为参数传递进去
        def helper(node: TreeNode, min_=float("-inf"), max_=float("inf")):
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

    def convertBST(self, root: TreeNode) -> TreeNode:
        """
        538. 把二叉搜索树转换为累加树
        给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），
        使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。
        提醒一下，二叉搜索树满足下列约束条件：
        节点的左子树仅包含键 小于 节点键的节点。
        节点的右子树仅包含键 大于 节点键的节点。
        左右子树也必须是二叉搜索树。

        递归法解决
        """
        self.sum_ = 0

        def inorder(node):
            if node:
                inorder(node.right)
                node.val += self.sum_
                self.sum_ = node.val
                inorder(node.left)

        inorder(root)
        return root

    def bstToGst(self, root: TreeNode) -> TreeNode:
        """
        1038. 把二叉搜索树转换为累加树
        迭代法解决
        二叉搜索树的累加那就 右中左遍历即可
        """
        stack = []
        node = root
        sum_ = 0
        while stack or node:
            while node:
                stack.append(node)
                node = node.right
            node = stack.pop()
            node.val += sum_
            sum_ = node.val
            node = node.left
        return root

    # BST的增删改查完全是一样的套路，判断大小后递归就好

    def searchBST(self, root: TreeNode, val: int):
        """
        700. 二叉搜索树的搜索
        基本套路
        """
        if not root:
            return None
        if root.val == val:
            return root
        elif root.val < val:
            return self.searchBST(root.right, val)
        elif root.val > val:
            return self.searchBST(root.left, val)

    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        """
        701. 二叉搜索树中的插入操作
        给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。
        返回插入后二叉搜索树的根节点。 输入数据 保证 ，新值和原始二叉搜索树中的任意节点值都不同。

        注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。
        你可以返回 任意有效的结果 。
        """
        if not root:
            return TreeNode(val)
        if root.val < val:  # 数太大了就插右子树
            root.right = self.insertIntoBST(root.right, val)
        elif root.val > val:  # 数太小了就插左子树
            root.left = self.insertIntoBST(root.left, val)
        return root

    def deleteNode(self, root: TreeNode, key: int):
        """
        450. 删除二叉搜索树中的节点
        给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，
        并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。
        一般来说，删除节点可分为两个步骤：
        首先找到需要删除的节点；
        如果找到了，删除它。
        说明： 要求算法时间复杂度为O(h)，h 为树的高度。

        同样的递归套路，弄清楚需要删除的节点的后序情况即可，0，1，2三种情况

        """
        if not root:
            return None
        if root.val < key:  # 在右子树上
            root.right = self.deleteNode(root.right, key)
            return root
        elif root.val > key:  # 在左子树上
            root.left = self.deleteNode(root.left, key)
            return root
        else:  # 关键来了，找到了节点位置
            # 分别判断左右子树是否存在就等于判断该节点是否有子树，包含了0的情况
            #
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                p = root.right
                while p.left:
                    p = p.left
                root.val = p.val
                root.right = self.deleteNode(root.right, p.val)
        return root


class Codec:
    """
    层序遍历的二叉树的序列化与反序列化
    """

    def serialize(self, root: TreeNode):
        """
        二叉树的序列化
        """
        # 迭代写法
        if not root:
            return "[]"
        res = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("null")
        return '[' + ",".join(res) + "]"
        # 卧槽居然没办法用递归实现




    def deserialize(self, strs):
        """
        二叉树的反序列化
        """
        if strs == "[]":
            return None
        # 不为空的话先把根节点建立起来
        vals, i = strs[1:-1].strip().split(','), 1
        root = TreeNode(int(val[0]))
        queue = [root]
        while queue:
            node = queue.pop(0)
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root
