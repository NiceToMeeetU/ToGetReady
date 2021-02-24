# coding   : utf-8 
# @Time    : 21/02/24 10:06
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0224.py
# @Software: PyCharm


from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
        请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。
        :param intervals: [[1,3],[2,6],[8,10],[15,18]]
        :return: [[1,6],[8,10],[15,18]]
        """


    def m56(self):
        print(self.merge([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]))


if __name__ == '__main__':
    s = Solution()
