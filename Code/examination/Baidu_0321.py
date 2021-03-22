# coding   : utf-8 
# @Time    : 21/03/21 17:55
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : Baidu_0321.py
# @Software: PyCharm


from typing import List
import sys


def maxBoyMarix(m: int, n: int, mat: List[List[str]]) -> int:
    """
    找出 m * n 矩阵中最大的仅包含 “M” 的子方阵
    """
    # res = 1
    # for i in range(m):
    #     for j in range(n):
    #         if mat[i][j] == "M":
    #             tmp = []
    #             tmp_count = 1
    #             mat[i][j] = 'A'  # already computed
    #             tmp.append([i, j])
    #
    #             while len(tmp) > 0:
    #                 x, y = tmp.pop(0)
    #                 for new_x, new_y in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]:
    #                     if 0 <= new_x <= m and 0 <= new_y <=n and mat[new_x][new_y] == "M":
    #                         tmp_count += 1
    #                         mat[new_x][new_y] = "A"
    #                         tmp.append([new_x, new_y])
    #             res = max(res, tmp_count)
    # return res
    res = 1
    for i, l in enumerate(mat):
        for j, p in enumerate(l):
            cur = 0
            queue = [(i, j)]
            while q:
                cur_i, cur_j = queue.pop(0)
                if cur_i < 0 or cur_j < 0 or cur_i == m or cur_j == n or mat[cur_i][cur_j] != "M":
                    continue
                mat[cur_i][cur_j] = "A"



if __name__ == '__main__':
    m_in, n_in = list(map(int, sys.stdin.readline().strip().split()))
    mat_in = []
    for _ in range(m_in):
        lines = sys.stdin.readline().strip()
        tmp = [i for i in lines]
        mat_in.append(tmp)
    # ans = maxBoyMarix(m_in, n_in, mat_in)
    # print(ans)

