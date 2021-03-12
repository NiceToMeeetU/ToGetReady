# coding   : utf-8 
# @Time    : 21/03/12 8:47
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0312.py
# @Software: PyCharm


from typing import List


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        """
        331. 验证二叉树的前序序列化
        序列化二叉树的一种方法是使用前序遍历。当我们遇到一个非空节点时，
        我们可以记录下这个节点的值。如果它是一个空节点，我们可以使用一个标记值记录，例如 #。
        例如，上面的二叉树可以被序列化为字符串 "9,3,4,#,#,1,#,#,2,#,6,#,#"，其中 # 代表一个空节点。
        给定一串以逗号分隔的序列，验证它是否是正确的二叉树的前序序列化。
        编写一个在   不重构树   的条件下的可行算法。
        每个以逗号分隔的字符或为一个整数或为一个表示 null 指针的 '#' 。
        你可以认为输入格式总是有效的，例如它永远不会包含两个连续的逗号，比如"1,,3" 。
        """
        # 度的思路
        # degree = 1
        # for s in preorder.split(','):
        #     if degree == 0:
        #         return False
        #     if s == "#":
        #         degree -= 1
        #     else:
        #         degree += 1
        #     # return degree == 0
        #
        # stack = []
        # for s in preorder.split(","):
        #
        #     if s == "#":
        #         if stack[-1] == "#":
        #             stack.pop()
        #             stack.pop()
        #             stack.append("#")
        #         else:
        #             stack.append("#")
        #     else:
        #         stack.append(s)
        # return len(stack) == 1

        numCount, leafCount = 0, 0
        if preorder[-1] != "#":
            return False
        for s in preorder.split(",")[:-1]:
            if numCount < leafCount:
                return False
            if s == "#":
                leafCount += 1
            else:
                numCount += 1
        return numCount == leafCount

if __name__ == '__main__':
    solution = Solution()
    print(solution.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))