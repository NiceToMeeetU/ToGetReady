# coding   : utf-8 
# @Time    : 21/04/30 17:13
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0430.py
# @Software: PyCharm

from typing import List

class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        res = []
        tmp = 0
        left, right = 1, 1
        while right <= target:
            if tmp == target:
                res.append(list(range(left, right)))
                left += 1
                right = left
                tmp = 0
            elif tmp < target:
                tmp += right
                right += 1
            elif tmp > target:
                tmp -= left
                left += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.findContinuousSequence(15))