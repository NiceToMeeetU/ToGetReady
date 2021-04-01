# coding   : utf-8 
# @Time    : 21/03/31 18:56
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : Huawei_0331.py
# @Software: PyCharm

import sys


def football(scores):
    """
    足球积分排序程序
    :param scores: 各场比赛具体分值str
    :return: 各参赛队积分排名
    """
    res = dict()
    for line in scores:
        team, score = line.split()
        team_0, team_1 = team.split("-")
        score = list(map(int, score.split(":")))
        if score[0] > score[1]:
            res[team_0] = res.get(team_0, 0) + 3
        elif score[0] < score[1]:
            res[team_1] = res.get(team_1, 0) + 3
        elif score[0] == score[1]:
            res[team_0] = res.get(team_0, 0) + 1
            res[team_1] = res.get(team_1, 0) + 1
    res = sorted(res.items(), key=lambda x: (-x[1], x[0]), reverse=False)
    # res = sorted(res.items(), key = lambda x:-x[1], reverse=False)

    return res


if __name__ == '__main__':
    scores_ = ["a-b 3:0", "z-s 2:2", "b-a 1:1", "s-a 3:2"]
    # scores_ = []
    # while True:
    #     line_ = sys.stdin.readline().strip()
    #     if not line_:
    #         break
    #     scores_.append(line_)
    ans = football(scores_)
    print(",".join([t + " " + str(s) for t, s in ans]))

####################################################
# import sys
#
#
def minHats(info):
    """
    :param info: 每个员工反馈的帽子颜色相同的帽子数量
    :return: 员工帽子的最少数量
    """
    if not info:
        return 0
    dic = dict()
    res = 0
    for c in info:
        if c == 0:
            res += 1
        if c not in dic:
            dic[c] = 1
        elif dic[c] < c:
            dic[c] += 1
        elif dic[c] == c:
            res += c + 1
            dic.pop(c)
    for k, v in dic.items():
        res += k + 1

    return res


if __name__ == '__main__':
    # line = sys.stdin.readline().strip()
    line = "[1, 2,3,4]"
    if line == "[]":
        print(0)
    else:
        info_ = line[1:-1].split(",")
        print(info_)
        info_ = list(map(int, info_))
        print(info_)
        ans = minHats(info_)
        print(ans)
print(minHats([1, 1, 2]))
####################################################
import sys


def minStep(s, t, pos):
    """
    :param s: 输入的完整字符串
    :param t: 需要匹配的子字符串
    :param pos: 起始位置
    :return: 找到该子字符串的最少步数
    """
    if not s or not t:
        return
    m, n = len(s), len(t)
    idx, valit, step = 0, 0, 0
    while True:
        left, right = pos, pos
        stepLeft, stepRight = 0, 0
        if t[idx] == s[pos]:
            step += 0
            valit += 1
            idx += 1
            if valit == n:
                break
    #     if t[idx] != s[pos]:
    #         while 0 <=
    # (pos + i + n) % n
    # (pos - i + n) % n

    return 1


if __name__ == '__main__':
    s_in = sys.stdin.readline().strip()
    t_in = sys.stdin.readline().strip()
    i_in = int(sys.stdin.readline().strip())
    # ans = minStep(s_in, t_in, i_in)
    ans = minStep("aemoyn", "amo", 0)
    print(ans)
