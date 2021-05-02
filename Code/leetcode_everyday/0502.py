# coding   : utf-8 
# @Time    : 21/05/02 13:18
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0502.py
# @Software: PyCharm


from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        n = len(wall)
        m = sum(wall[0])
        if m == 1:
            return n
        path_dic = dict()
        for line in wall:
            tmp = 0
            if len(line) == 1:
                continue
            for i in line[:-1]:
                tmp += i
                path_dic[tmp] = path_dic.get(tmp, 0) + 1
        print(path_dic)
        return n - max(path_dic.values())  if path_dic else n

if __name__ == '__main__':
    solution = Solution()
    wall = [[1,1],[2],[1,1]]
    print(solution.leastBricks(wall))