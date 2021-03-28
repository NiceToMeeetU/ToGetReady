# coding   : utf-8 
# @Time    : 2021/3/27 12:56
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : NetEase_0327.py
# @Software: PyCharm

#coding=utf-8
# 本题为考试单行多行输入输出规范示例，无需提交，不计分。
# import sys
# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))
#
#
#
# import sys
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     ans = 0
#     for i in range(n):
#         # 读取每一行
#         line = sys.stdin.readline().strip()
#         # 把每一行的数字分隔后转化成int列表
#         values = list(map(int, line.split()))
#         for v in values:
#             ans += v
#     print(ans)
#
#


import sys

class TreeNode:
    def __init__(self, val = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deserialize(strs):
    if strs == "[]":
        return None
    vals, i = strs[1:-1].strip().split(","), 1
    root = TreeNode(int(vals[0]))
    queue = [root]
    while queue and i < len(vals):
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

def pathSum(root, target):
    if not root:
        return []
    res = []
    stack = [([root.val]), root]
    while stack:
        tmp, node = stack.pop()
        if not node.right and not node.left and sum(tmp) == target:
            return tmp
        if node.left:
            stack.append((tmp + [node.left.val]), node.left)
        if node.right:
            stack.append((tmp + [node.right.val]), node.right)
    return







if __name__ == '__main__':
    # line = sys.stdin.readline().strip()
    # target = int(sys.stdin.readline().strip())
    line = "[3,1,5,2,4,4,1]"
    target = 8
    node = deserialize(line)
    ans = pathSum(node, target)
    print("[" + ",".join([str(i) for i in ans]) + "]")
