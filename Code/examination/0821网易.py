# coding   : utf-8 
# @Time    : 21/08/21 15:43
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0821网易.py
# @Software: PyCharm


# class Solution:
# def median(self, arr):
#     # 利用小根堆处理
#     heapnum = len(arr) // 2 + 1
#     heap = arr[:heapnum + 1]
#     for i in range(len(heap) // 2 - 1, -1, -1):
#         self.modif_heap(i, heap)
#     for j in range(heapnum + 1, len(arr)):
#         if arr[j] > heap[0]:
#             heap[0] = arr[j]
#             self.modif_heap(0, heap)
#     return heap[1] if len(arr) % 2 == 1 else float((heap[0] + min(heap[1], heap[2])) / 2)
#
# def modif_heap(self, parent, heap):
#     child = 2 * parent + 1
#     while len(heap) > child:
#         if child + 1 < len(heap):
#             child += 1
#         if heap[parent] <= heap[child]:
#             break
#         heap[parent], heap[child] = heap[child], heap[parent]
#         parent, child = child, child * 2 + 1

# 2
# class Solution:
#     def find_stars(self, star_names, article):
#         res = 0
#         star_names_dict = dict()
#         for name in star_names:
#             l = len(name)
#             star_names_dict[l] = star_names_dict.get(l, dict())
#             star_names_dict[l][name] = 0
#         name_len = sorted(list(star_names_dict.keys()))
#         for i in range(len(article)):
#             for l in name_len:
#                 if article[i:i + l] in star_names_dict[l]:
#                     res += 1
#         return res
#
#
# if __name__ == "__main__":
#     star_names = input().strip().split(" ")
#     article = input().strip()
#     solution = Solution()
#     print(solution.find_stars(star_names, article))
#

# import math
#
# class Solution:
#     def __init__(self, K):
#         self.K = K
#
#     def mysoftmax(self, logits):
#         sum_softmax = 0
#         max_logits = logits[0]
#         ans = 0
#         for i in range(self.K):
#             exps = math.exp(logits[i])
#             sum_softmax += exps
#             if logits[i] >= max_logits:
#                 ans = i
#                 max_logits = logits[i]
#                 p = exps
#
#
#         return ans, float(p / sum_softmax)
#
#
# if __name__ == '__main__':
#     N, K = list(map(int, input().strip().split()))
#     solution = Solution(K)
#     for _ in range(N):
#         logits = list(map(float, input().strip().split()))
#
#         pred, proba = solution.mysoftmax(logits)
#
#         print(f"{pred} {proba:0.6f}")
#
#
# #
#
#
#
# class Solution:
#     def papers(self, ages):
#         res = 0
#         n = len(ages)
#
#
#         return res
#
# if __name__ == '__main__':
#     ages = list(map(int, input().strip().split()))
#     solution = Solution()
#     print(solution.papers(ages))


#
# class Solution:
#     def pandas(self, n, d):
#         res = 0
#         d = sorted(d)
#         for i in d:
#             res += n // d
#             n = n % d
#
#
#         return res
#
# if __name__ == '__main__':
#     solution = Solution()
#     n, *d = list(map(int, input().strip().split()))
#     print(solution.pandas(n, a, b, c))




# class Solution:
#     def zhongyong(self, nums0, nums1):
#         nums0.sort()
#         min_1, max_1 = min(nums1), max(nums1)
#         l0 = len(nums0)
#         i, j = 0, l0 - 1
#         while i < j:
#             if nums0[i] > min_1:
#                 break
#             i += 1
#         while j > i:
#             if nums0[j] < max_1:
#                 break
#             j -= 1
#         return len(nums1) + j - i + 1
#
#
# if __name__ == '__main__':
#     n = int(input().strip())
#     nums0, nums1 = [], []
#     for _ in range(n):
#         x, y = list(map(int, input().strip().split()))
#         if y == 0:
#             nums0.append(x)
#         elif y == 1:
#             nums1.append(x)
#     solution = Solution()
#     print(solution.zhongyong(nums0, nums1))

from collections import  Counter
class Solution:
    def mostItems(self, query, items):
        res = []
        for idx, line in enumerate(items):
            score = 0
            #counts = dict(Counter(line))
            for q in query:
                if q in line:
                    #score += counts.get(q, 0)
                    score += 1
            res.append((line, score, idx))
        res = sorted(res, key=lambda x: (-x[1], x[2], x[0]), reverse=False)
        return res


if __name__ == '__main__':
    solution = Solution()
    # query = input().strip()
    # items = []
    # while True:
    #     line = input()
    #     if not line:
    #         break
    #     items.append(line)

    query = "全国新冠疫苗接种剂次超9亿"
    items = [
        "国家卫健委:全国新冠疫苗接种超8亿剂次",
        '超9亿剂次！1分钟看疫苗接种“中国速度”',
        '新冠病毒疫苗第二剂次接种“宁迟勿早”',
        '全国新冠疫苗接种剂次超7亿',
        '全国新冠疫苗接种超5亿剂次',
        '广东新冠病毒疫苗接种突破4000万剂次稳居全国第一',
        '[新闻直播间] 国家卫健委 全国各地累计接种新冠疫苗超9亿剂次',
        '（一起苗苗苗） 长沙新冠病毒疫苗接种突破300万剂次',
        '全国累计报告接种新冠疫苗超3.80亿剂次',
        '超3亿剂次！全国新冠疫苗接种加速推进谁在努力'
    ]
    ans = solution.mostItems(query, items)
    i = 0
    # while i < 5:
    #     print(ans[i][0])
    #     i += 1
    for i in ans:
        print(i[0], i[1], i[2])