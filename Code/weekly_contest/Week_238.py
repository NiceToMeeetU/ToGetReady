# coding   : utf-8 
# @Time    : 21/04/25 10:28
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : Week_238.py
# @Software: PyCharm

#
# class Solution:
#     def sumBase(self, n: int, k: int) -> int:
#         res = 0
#         p = {2: 6, 3: 4, 4: 3, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2, 10: 2}
#         m = p[k]
#
#         while n > 0:
#             tmp = n // (k ** m)
#             if tmp > 0:
#                 res +=tmp
#                 n -= tmp * (k ** m)
#             m -= 1
#         return res
#
# if __name__ == '__main__':
#     solution = Solution()
#     print(solution.sumBase(100,3))

# class Solution:
#     def longestBeautifulSubstring(self, word: str) -> int:
#         n = len(word)
#
#         if n < 5:
#             return 0
#         t = ["a", "e", "i", "o", "u"]
#         for c in t:
#             if c not in word:
#                 return 0
#
#         res = 0
#         i, j = 0, 0
#         while j < n:
#             while i < n and word[i] != "a":
#                 i += 1
#             j = i
#             while j < n and i < n and word[j] == word[i]:
#                 j += 1
#             k = 1
#             while j < n and word[j] == t[k]:
#                 if k == 4:
#                     res = max(res, j - i + 1)
#                 if j < n - 1 and word[j] != word[j + 1]:
#                     k += 1
#                 j += 1
#                 if k == 5:
#                     res = max(res, j - i)
#                     break
#
#             i = j
#             j += 1
#
#         return res
#
#
# if __name__ == '__main__':
#     solution = Solution()
#     print(solution.longestBeautifulSubstring("aeiaaioaaaaeiiiiouuuooaauuaeiu"), 13)
#     print(solution.longestBeautifulSubstring("aeeeiiiioooauuuaeiou"), 5)
#     print(solution.longestBeautifulSubstring("aaaaa"), 0)
#     print(solution.longestBeautifulSubstring("aaaaaiiiooou"), 0)
#     print(solution.longestBeautifulSubstring("aaaaaeeeeeiouuuuuaeiuioaeiouuuuaeiouuuuu"), 17)
#     print(solution.longestBeautifulSubstring("a"), 0)


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        mid = len(nums) // 2
        while




if __name__ == '__main__':
    solution = Solution()
    print(solution.maxFrequency(nums=[1, 2, 4], k=5), 3)
    print(solution.maxFrequency(nums=[1,4,8,13], k=5), 2)
