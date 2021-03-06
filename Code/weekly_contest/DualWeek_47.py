# coding   : utf-8 
# @Time    : 21/03/06 22:29
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : DualWeek_47.py
# @Software: PyCharm


from typing import List
import collections


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        """
        给你两个整数 x 和 y ，表示你在一个笛卡尔坐标系下的 (x, y) 处。同时，在同一个坐标系下给你一个数组 points ，
        其中 points[i] = [ai, bi] 表示在 (ai, bi) 处有一个点。
        当一个点与你所在的位置有相同的 x 坐标或者相同的 y 坐标时，我们称这个点是 有效的 。
        请返回距离你当前位置 曼哈顿距离 最近的 有效 点的下标（下标从 0 开始）。
        如果有多个最近的有效点，请返回下标 最小 的一个。如果没有有效点，请返回 -1 。
        两个点 (x1, y1) 和 (x2, y2) 之间的 曼哈顿距离 为 abs(x1 - x2) + abs(y1 - y2)
        :param x:
        :param y:
        :param points:
        :return:
        """
        min_ = float('inf')
        res = float('inf')
        print(f"{x=}, {y=}")
        for idx, (a, b) in enumerate(points):
            print(f"{idx = }, {a = }, {b = }")
            if a == x or b == y:
                md = abs(x - a) + abs(y - b)
                if md < min_:
                    min_ = md
                    res = idx
                elif md == min_:
                    res = min(res, idx)
            print(f"{min_ = }, {res = }")
        return res

    def checkPowersOfThree(self, n: int) -> bool:
        """
        5681. 判断一个数字是否可以表示成三的幂的和
        给你一个整数 n ，如果你可以将 n 表示成若干个不同的三的幂之和，请你返回 true ，否则请返回 false 。
        对于一个整数 y ，如果存在整数 x 满足 y == 3x ，我们称这个整数 y 是三的幂。
        :param n:
        :return:
        """
        while n > 1:
            if n % 3 == 0:
                n //= 3
                continue
            elif (n - 1) % 3 == 0:
                n = (n - 1) // 3
                continue
            else:
                return False
        return True

    def beautySum(self, s: str) -> int:
        """
        5682. 所有子字符串美丽值之和
        一个字符串的 美丽值 定义为：出现频率最高字符与出现频率最低字符的出现次数之差。

        比方说，"abaacc" 的美丽值为 3 - 1 = 2 。
        给你一个字符串 s ，请你返回它所有子字符串的 美丽值 之和。
        """
        # 暴力求解必然不行
        # res = 0
        # for i in range(len(s)):
        #     for j in range(i, len(s)+1):
        #         tmp = s[i:j]
        #         counts = collections.Counter(tmp).most_common()
        #         try:
        #             res += counts[0][1] - counts[-1][1]
        #         except IndexError:
        #             continue
        #         print(f"{tmp = }, {counts = }, {res =}")
        # return res
        res = 0
        for i in range(len(s)):
            counts = {}
            for j in range(i, len(s)):
                counts[s[j]] = counts.get(s[j], 0) + 1
                res += max(counts.values()) - min(counts.values())
        return res

    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        """
        5683. 统计点对的数目
        给你一个无向图，无向图由整数 n  ，表示图中节点的数目，和 edges 组成，其中 edges[i] = [ui, vi] 表示 ui 和 vi 之间有一条无向边。同时给你一个代表查询的整数数组 queries 。
        第 j 个查询的答案是满足如下条件的点对 (a, b) 的数目：
        a < b
        cnt 是与 a 或者 b 相连的边的数目，且 cnt 严格大于 queries[j] 。
        请你返回一个数组 answers ，其中 answers.length == queries.length 且 answers[j] 是第 j 个查询的答案。
        请注意，图中可能会有 重复边 。
        :param n:
        :param edges:
        :param queries:
        :return:
        """
if __name__ == '__main__':
    solution = Solution()
    # print(solution.nearestValidPoint(3, 4, [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]))
    # print(solution.checkPowersOfThree(12))
    print(solution.beautySum("aabcb"))
