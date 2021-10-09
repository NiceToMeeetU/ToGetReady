# coding   : utf-8 
# @Time    : 21/08/23 18:33
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0823_contribution.py
# @Software: PyCharm


# class Solution:
#     def teacherHelpMe(self, n, p, q, scores):
#         res = 0
#         scores.sort()
#         score_daily = 100
#         for i in range(n - 1, -1, -1):
#             if i < n - 1 and scores[i] < scores[i + 1]:
#                 score_daily -= 1
#             if p * score_daily + q * scores[i] >= 60 * 100:
#                 res += 1
#             else:
#                 break
#         return res
#
# if __name__ == '__main__':
#     solution = Solution()
#     n, p, q = 2, 20, 80
#     scores = [51, 50]
#     print(solution.teacherHelpMe(n,p,q,scores))

class Solution:
    def greatwall(self, n, m, x, k, a):
        res = 0
        tmp = sorted([[a[i], i] for i in range(n)])


        return res

if __name__ == '__main__':
    solution = Solution()
    n, m, x, k = 5, 2, 1, 2
    a = [4, 4, 2, 4, 4]
    ans = solution.greatwall(n, m, x, k, a)
    print(ans)