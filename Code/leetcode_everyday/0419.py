# coding   : utf-8 
# @Time    : 21/04/19 15:06
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0419.py
# @Software: PyCharm


class Solution:
    def isDigit(self, c: str) -> bool:
        return "0" <= c <= "9"

    def isNumber(self, s: str) -> bool:
        # heiheihei
        # try:
        #     ans = float(s)
        #     return True
        # except:
        #     return False

        # 好无聊的题呀
        sign = False
        science = False
        point = False
        n = len(s)
        for i, c in enumerate(s):
            if c == "-" or c == "+":
                if sign:
                    return False
                elif i < n - 1 and not self.isDigit(s[i + 1]):
                    return False
                sign = True

            elif c == "e" or c == "E":
                if science:
                    return False
                elif i == 0 or i == n - 1:
                    return False
                elif i < n - 1 and not self.isDigit(s[i + 1]):
                    if s[i + 1] == "-" or s[i + 1] == "+":
                        return True
                    return False
                science = True
                sign = False
                point = False
            elif c == ".":
                if point:
                    return False
                elif i == 0 or i == n - 1:
                    return False
                elif i < n - 1 and not self.isDigit(s[i + 1]):
                    return False
                point = True
            elif ord("0") <= ord(c) <= ord("9"):
                continue
            else:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    strs = [".1",
            "e2",
            "+e-"]
    ans = [False, False, False]

    for s, a in zip(strs, ans):
        print(solution.isNumber(s), a)
