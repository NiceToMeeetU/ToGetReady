# coding   : utf-8 
# @Time    : 21/03/04 8:41
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0304.py
# @Software: PyCharm


from typing import List
import bisect


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        n = len(envelopes)
        # E = sorted(envelopes, key=lambda x:(x[0], - x[1]))
        envelopes.sort(key=lambda x:(x[0], - x[1]))
        f = [envelopes[0][1]]
        for i in range(1, n):
            tmp = envelopes[i][1]
            if tmp > f[-1]:
                f.append(tmp)
            else:
                index = bisect.bisect_left(f, tmp)
                f[index] = tmp
        return len(f)

if __name__ == '__main__':
    pass