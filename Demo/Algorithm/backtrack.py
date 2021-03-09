# coding   : utf-8 
# @Time    : 21/03/09 11:03
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : backtrack.py
# @Software: PyCharm


"""
回溯算法
本质就是暴力，只要有递归就会有回溯
难、效率低下，最多加个剪枝优化一下，但很多情况下不得不用：
- 组合问题：N个数里面按一定规则找出k个数的集合
- 排列问题：N个数按一定规则全排列，有几种排列方式
- 切割问题：一个字符串按一定规则有几种切割方式
- 子集问题：一个N个数的集合里有多少符合条件的子集
- 棋盘问题：N皇后，解数独等等

可用回溯法解决的问题都可以抽象为树形结构。
回溯法珏姐的都是在集合中递归查找子集：
- 集合的大小构成树的宽度；
- 递归的深度构成树的深度；

如果解决一个问题有多个步骤，每一个步骤有多个方法，又要求列出所有可行结果;
要多层嵌套循环遍历，但又不能确定嵌套的深度的；
一般使用回溯

回溯模板框架：

def backtracking(* params):
    if 终止条件:
        存放结果
        return
    for 选择本层集合中元素，树中节点孩子的数量即集合的大小:
        处理节点
        backtrack(路径, 选择列表)  # 递归
        回溯，撤销处理结果

---

result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return

    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择


"""
from typing import List

class Solution:
    """
    经典回溯问题罗列
    """
    def fullConbine(self, nums: List[int]):
        """
        数组全排列问题
        """
        res = []
        def backtrack(nums_, path):
            if len(path) == len(nums_):
                res.append(path)
                return
            for i in range(len(nums_)):
                if nums_[i] in path:
                    continue
                path.append(nums_[i])
                backtrack(nums_, path)
                path.pop(-1)
        backtrack(nums, [])
        return res



    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        77. 组合
        给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
        直接暴力无法求解的问题，因为要写k层循环遍历
        """
        # 基本写法，未剪枝：
        res = []
        def backtrack(idx, tmp):
            if len(tmp) == k:
                res.append(tmp)
                return
            # for j in range(idx, n + 1):
            # 因为实际上不需要遍历到那么后面，所以剪枝
            # 效果明显 400ms -> 56 ms
            for j in range(idx, n - (k - len(tmp) -1)+ 1): # 剪枝优化的关键
                backtrack(j + 1, tmp + [j])
        backtrack(1, [])
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.fullConbine([2,3,2,12,4]))
    # print(solution.combine(10,4))