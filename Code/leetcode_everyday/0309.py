# coding   : utf-8 
# @Time    : 21/03/09 8:27
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0309.py
# @Software: PyCharm


from typing import List

class Solution:
    def removeDuplicates(self, S: str) -> str:
        """
        1047. 删除字符串中的所有相邻重复项
        给出由小写字母组成的字符串S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
        在 S 上反复执行重复项删除操作，直到无法继续删除。
        在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。
        """
        stack = []
        for s in S:
            if stack and s == stack[-1]:
                stack.pop()
            else:
                stack.append(s)
        return ''.join(stack)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        39. 组合总和
        给定一个无重复元素的数组candidates和一个目标数target，
        找出candidates中所有可以使数字和为target的组合。
        candidates中的数字可以无限制重复被选取。
        说明：
        所有数字（包括target）都是正整数。
        解集不能包含重复的组合。
        :param candidates:[2,3,6,7]
        :param target: 7
        :return:[[7],[2,2,3]]
        题目给定的元素有大小限制，应该可以直接暴力求解
        树的宽度有限，深度无限
        """
        # 按照动规 + 递归的简洁写法：
        if target < 1:
            return []
        ans = []
        for i in range(len(candidates)):
            if target == candidates[i]:
                ans.append([target])
            for j in self.combinationSum(candidates[i:], target - candidates[i]):
                ans.append([candidates[i]] + j)
        # 完全没看懂
        # return ans

        # 最简单的无剪枝的回溯算法
        res = []
        n = len(candidates)
        path = []
        def backtrack(idx, curSum):
            if idx == n or curSum > target:
                return
            elif curSum == target:
                # res.append(path[:]) # 切片与不切片，深浅拷贝问题，注意！
                res.append(path)
                print(f"{path =}, {path[:] =}，{res = }")
                return
            backtrack(idx + 1, curSum)
            if curSum + candidates[idx] <= target:
                path.append(candidates[idx])
                backtrack(idx, curSum + candidates[idx])
                path.pop()
        backtrack(0, 0)
        return res

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """
        216. 组合总和
        找出所有相加之和为n 的k个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
        说明：
        所有数字都是正整数。
        解集不能包含重复的组合。
        """
        # res = []
        # def backtrack(idx)



if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum([2,3,6,7],7))
