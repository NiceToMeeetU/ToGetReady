# coding   : utf-8 
# @Time    : 21/04/29 19:00
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : TME_0429.py
# @Software: PyCharm

#
import sys
from collections import Counter


class Solution:
    def employee(self, nums: list[int]) -> int:
        ns = Counter(nums)
        for i, j in sorted(dict(ns).items(), key = lambda x:x[0]):
            if j == 1:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution()
    n = int(sys.stdin.readline().strip())
    nums_ = list(map(int, sys.stdin.readline().strip().split()))
    ans = solution.employee(nums_)
    print(ans)

##########################################################

import sys


class Solution:
    def countries(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    s = grid[i][j]
                    grid[i][j] = -1
                    tmp = [[i, j]]
                    while len(tmp) > 0:
                        x, y = tmp.pop(0)
                        for new_x, new_y in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]:
                            if 0 <= new_x < n and 0 <= new_y < m and grid[new_x][new_y] == s:
                                tmp.append([new_x, new_y])
                                grid[new_x][new_y] = -1
                    res += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    n_, m_ = list(map(int, sys.stdin.readline().strip().split()))
    grid_ = []
    for _ in range(n_):
        grid_.append(list(map(int, sys.stdin.readline().strip())))
    ans = solution.countries(grid_)
    print(ans)


import sys




if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        n = int(sys.stdin.readline().strip())
