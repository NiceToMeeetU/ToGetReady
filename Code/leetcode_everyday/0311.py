# coding   : utf-8 
# @Time    : 21/03/11 8:45
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0311.py
# @Software: PyCharm


from typing import List


class Solution:
    def calculate(self, s: str) -> int:
        """
        227. 基本计算器 II
        只有加减乘除
        先乘除再加减
        """
        stack = []
        sign = "+"
        num = 0
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord('0')
            if not s[i].isdigit() and s[i] != ' ' or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack[-1] *= num
                elif sign == "/":
                    stack[-1] /= num
                sign = s[i]
                num = 0
        return sum(stack)

    def openLock(self, deadends: List[str], target: str) -> int:
        """
        752. 打开转盘锁
        你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字：
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。
        每个拨轮可以自由旋转：例如把 '9' 变为 '0'，'0' 变为 '9' 。
        每次旋转都只能旋转一个拨轮的一位数字。
        锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。
        列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，
        这个锁将会被永久锁定，无法再被旋转。
        字符串 target 代表可以解锁的数字，
        你需要给出最小的旋转次数，如果无论如何不能解锁，返回 -1。
        :param deadends:["0201","0101","0102","1212","2002"]
        :param target:"0202"
        :return: 6
        BFS
        """
        # 单向BFS方法，很慢
        N = 10
        def move(s, loc, direction):
            return s[:loc] + str((int(s[loc]) + direction + N) % N) + s[loc + 1:]

        visited = set(deadends)
        step = 0
        queue = ["0"*len(target)]
        while queue:
            for _ in range(len(queue)):
                cur = queue.pop(0)
                # check
                if cur in visited:
                    continue
                if cur == target:
                    return step
                visited.add(cur)
                for i in range(len(target)):
                    t = move(cur, i, 1)
                    queue.append(t)
                    t = move(cur, i, -1)
                    queue.append(t)
            step += 1
        # return -1

        # 双向BFS，不需要使用队列，直接两个集合即可
        # 速度提升过于明显了！
        q1, q2, vis = set(), set(), set()
        q1.add("0"*len(target))
        q2.add(target)
        step = 0
        while q1:
            tmp = set()
            for cur in q1:
                if cur in deadends:
                    continue
                if cur in q2:
                    return step

                visited.add(cur)
                for i in range(len(target)):
                    t = move(cur, i, 1)
                    if t not in visited:
                        tmp.add(t)
                    t = move(cur, i, -1)
                    if t not in visited:
                        tmp.add(t)
            step += 1
            q1 = q2
            q2 = tmp
        return -1



if __name__ == '__main__':
    pass
