# coding   : utf-8 
# @Time    : 21/02/26 10:20
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0226.py
# @Software: PyCharm


from typing import List


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        """
        1178-h
        外国友人仿照中国字谜设计了一个英文版猜字谜小游戏，请你来猜猜看吧。
        字谜的迷面 puzzle 按字符串形式给出，如果一个单词 word 符合下面两个条件，那么它就可以算作谜底：
        单词 word 中包含谜面 puzzle 的第一个字母。
        单词 word 中的每一个字母都可以在谜面 puzzle 中找到。
        例如，如果字谜的谜面是 "abcdefg"，那么可以作为谜底的单词有 "faced", "cabbage", 和 "baggage"；而 "beefed"（不含字母 "a"）以及 "based"（其中的 "s" 没有出现在谜面中）。
        返回一个答案数组 answer，数组中的每个元素 answer[i] 是在给出的单词列表 words 中可以作为字谜迷面 puzzles[i] 所对应的谜底的单词数目。

        :param words:["aaaa","asas","able","ability","actt","actor","access"]
        :param puzzles:["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
        :return:[1,1,3,2,4,0]
        直接暴力肯定是不行的，需要对字母信息进行压缩
        26个字母不管出现几次，我们使用的信息只有出现过或者没出现，那么用一个26位的二进制表示即可；
        python中的int是32位的，直接用来表示绰绰有余
        需要先搞明白二进制下的子集如何求
        """
        def subsets(li):
            ans = [""]
            for i in li:
                ans  = ans + [i + j for j in ans]
            return ans

        from collections import Counter
        freq = Counter()
        for word in words:
            mask = 0
            for letter in word:
                mask |= 1 << (ord(letter) - ord("a"))       # 使用移位计算快速完成字符哈希压缩
            freq[mask] += 1
        res = []
        for puzzle in puzzles:
            total = 0
            for perm in subsets(puzzle[1:]):
                mask = 1 << (ord(puzzle[0]) - ord("a"))
                for letter in perm:
                    mask |= 1 << (ord(letter) - ord("a"))
                total += freq[mask]
            res.append(total)
        return res





    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        78-m
        给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
        解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
        :param nums:[1,2,3]
        :return:[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
        子集问题，迭代、递归、回溯应该都掌握
        """
        res = [[]]
        for num in nums:
            res = res + [[num] + i for i in res]
        return res



    def test(self):
        ans = self.findNumOfValidWords(["aaaa", "asas", "able", "ability", "actt", "actor", "access"],
                                       ["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"])
        # ans = self.subsets([1,2,3])
        print(ans)

if __name__ == '__main__':
    solution = Solution()
    solution.test()