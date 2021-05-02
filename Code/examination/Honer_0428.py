# coding   : utf-8 
# @Time    : 21/04/28 18:55
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : Honer_0428.py
# @Software: PyCharm


import sys


class Solution:
    def str2int(self, c: str) -> int:
        if "0" <= c <= "9":
            return int(c)
        elif "a" <= c <= "z":
            return ord(c) - ord("a") + 10
        elif "A" <= c <= "Z":
            return ord(c) - ord("A") + 36
        elif c == "@":
            return 62
        elif c == "_":
            return 63
        else:
            return "ERROR"

    def bash10(self, s: str) -> int:
        res = 0
        s = s.split("#")
        if len(s) == 1:  # 没有基数#部分
            s = s[0]
            if s.startswith("0x") or s.startswith("0X"):  # 八进制
                k = 16
                s = s[2:]
            elif s.startswith("0"):
                k = 8
                s = s[1:]
            else:
                k = 10
        elif len(s) == 2:  # 有基数#部分
            k = int(s[0])
            if k > 64:
                return "ERROR"
            s = s[1]
        else:  # 格式有误
            return "ERROR"

        for i, j in enumerate(s[::-1]):
            j = self.str2int(j)
            if j == "ERROR" or j >= k:
                return "ERROR"
            res += j * (k ** i)
        return res


if __name__ == '__main__':
    # s_in = sys.stdin.readline().strip()
    solution = Solution()
    # ans = solution.bash10(s_in)
    # print(ans)
    # print(solution.bash10("10"), 10)
    # print(solution.bash10("090"), "ERROR")
    print(solution.bash10("63#11"), 64)


#######################################################


# import sys
#
# class Solution:
#     def matchInterview(self, t: list[list[str]], s:[list[str]], x: int):
#         m, n = len(t), len(s)
#         match = [[0 for _ in range(n)] for _ in range(m)]
#
#
#
#         return 1,2
#
#
# if __name__ == '__main__':
#     M, N, x_ = list(map(int, sys.stdin.readline().strip().split()))
#     t_ = []
#     s_ = []
#     for _ in range(M):
#         t_.append(sys.stdin.readline().strip().split())
#     for _ in range(N):
#         s_.append(sys.stdin.readline().strip())
#     solution = Solution()
#     ans1, ans2 = solution.matchInterview(t_, s_, x_)
#     print(ans1)
#     for line in ans2:
#         print(" ".join(list(map(str, line))))


#################################################


# import sys
#
#
# class Solution:
#     def isEven(self, num):
#         return num % 2 == 0
#
#     def isPrime(self, num):
#         if num == 0 or num == 1:
#             return False
#         elif num == 2:
#             return True
#         else:
#             for i in range(2, int(num ** 0.5)):
#                 if num % i == 0:
#                     return False
#             return True
#
#     def goldbach(self, num: int):
#         if num < 6 or num % 2 != 0:
#             return 0
#         mid = num // 2
#         i, j = 0, 0
#         while mid - i >= 0 and mid + j <= num:
#             l = mid - i
#             r = mid + j
#             if not self.isPrime(l):
#                 i += 1
#                 continue
#             if not self.isPrime(r):
#                 j += 1
#                 continue
#             if l + r == num:
#                 return l, r
#         return 0
#
#
# if __name__ == '__main__':
#     num_ = int(sys.stdin.readline().strip())
#     solution = Solution()
#     ans = solution.goldbach(num_)
#     if ans == 0:
#         print(0)
#     else:
#         print(ans[0], ans[1])
#     # print(solution.goldbach(26), 13, 13)
