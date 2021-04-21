# coding   : utf-8 
# @Time    : 21/04/18 15:00
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : NetEase_0418.py
# @Software: PyCharm


#
# class Solution:
#     def subArray(self, s, t):
#         res = len(t)
#         l1, l2 = len(s), len(t)
#         i, j = 0, 0
#         idx = [0] * l1
#
#         t_idx = dict()
#         for i, c in enumerate(t):
#             tmp = ord(c) - ord("a")
#             t_idx[tmp] = min(i, )
#             a
#         for i in range(l1):
#
#         while i < l1 and j < l2 and i + j < l1:
#             if s[i] < t[j]:
#                 res = max(res, l1 + l2 - i - j)
#                 break
#             j += 1
#
#         return res
#
#
# if __name__ == "__main__":
#     s = sys.stdin.readline().strip()
#     t = sys.stdin.readline().strip()
#     q = int(sys.stdin.readline().strip())
#     query = []
#     for _ in range(q):
#         i, j = list(map(int, sys.stdin.readline().strip().split()))
#         query.append([i, j])
#
#     s = "abcd"
#
#     solution = Solution()
#     for i, j in query:
#         ans = solution.subArray(s[i - 1:], t[j - 1:])
#         print(ans)
#
# s = "abcd"
# t = "adcb"
#
# t_idx = dict()
# for i,c in enumerate(t):
#     tmp = ord(c) - ord("a")
#     if tmp not in t_idx:
#         t_idx[tmp] = i
#
# s = [ord(c) - ord("a") for c in s]


import sys
import pandas as pd


class Solution:
    def task1(self, df_plays):


        return df_plays

if __name__ == '__main__':
    """
    ACM 模式需要自己读取测试用例输入。
    假定本题指定的输入格式如下：
    
    第一行输入一个整数n，表示后面有n条数据输入
    从第二行开始的n行，每一行为一条记录，分别是时间戳，玩家ID，新手节点ID，是否通过，节点用时。
    各字段用空格隔开
    """

    n = int(sys.stdin.readline().strip())
    raw_data = []
    for _ in range(n):
        line = sys.stdin.readline().strip().split()
        raw_data.append(line)
    test = """11:36:00	1	1001	TRUE	60
            12:36:00	1	1002	FALSE	30
            13:36:00	2	1001	TRUE	45
            14:36:00	2	1002	TRUE	23
            15:36:00	2	1003	TRUE	25
            16:36:00	2	1004	FALSE	14
            17:36:00	3	1001	TRUE	25
            18:36:00	3	1002	FALSE	36
            19:36:00	3	1003	FALSE	18
            20:36:00	3	1004	FALSE	26
            21:36:00	4	1001	FALSE	35
            22:36:00	4	1002	FALSE	29"""
    raw = [line.split() for line in test.split("\n")]

    data = pd.DataFrame(raw, columns=["timestramp", "player_id", "level_id", "pass", "time"])
    data["pass"] = data["pass"].astype(lambda x: False if x == "False" else True)


    data = data.astype({"timestramp": str, "player_id": int, "level_id": int, "pass": lambda x: False if x == "False" else True, "time": float})
    #
    # solution = Solution()
    # ans = solution.task1(data)
    # print(ans)






