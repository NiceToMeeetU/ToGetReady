# coding   : utf-8 
# @Time    : 21/08/20 19:42
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0820ali.py
# @Software: PyCharm


class Solution:
    def __init__(self, n):
        self.n = n
        self.max_num = 0
        self.p = list(range(n))

    def marathon(self, a, b):
        a, b = max(a, b), min(a, b)
        # 所有的合并到较大的a上
        if self.p[a] == b or self.p[b] == a:
            return self.max_num - ()





if __name__ == '__main__':
    n, m = list(map(int, input().strip().split()))
    solution = Solution(n)
    for _ in range(m):
        a, b = list(map(int, input().strip().split()))

        print(solution.marathon(a, b))
