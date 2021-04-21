# coding   : utf-8 
# @Time    : 21/04/21 10:10
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : NetEase_kk.py
# @Software: PyCharm

import sys


def firstMethod(data: list[list[str]]):
    """
    不使用pandas包，不写类，纯python自带数据结构解决问题
    :param data:
    :return:
    """
    res = dict()

    for one in data:
        level_id = one[2]
        if level_id not in res:
            res[level_id] = {"pass_num": 0, "stop_num": 0, "using_time": 0}  # 每个level_id统计一下通过人数、未通过人数、用时
        if one[3] == "TRUE":  # 如果通过
            res[level_id]["pass_num"] += 1
            res[level_id]["using_time"] += float(one[4])
        else:  # 如果未通过
            res[level_id]["stop_num"] += 1
    for k, v in res.items():
        v["pass_ritho"] = v["pass_num"] / (v["pass_num"] + v["stop_num"])
    return res


if __name__ == '__main__':
    """
    ACM 模式需要自己读取测试用例输入。
    假定本题指定的输入格式如下：

    第一行输入一个整数n，表示后面有n条数据输入
    从第二行开始的n行，每一行为一条记录，分别是时间戳，玩家ID，新手节点ID，是否通过，节点用时。
    各字段用空格隔开
    """

    n = int(sys.stdin.readline().strip())
    raw_data = []
    for _ in range(n):
        line = sys.stdin.readline().strip().split()
        raw_data.append(line)

    test = """11:36:00	1	1001	TRUE	60
            12:36:00	1	1002	FALSE	30
            13:36:00	2	1001	TRUE	45
            14:36:00	2	1002	TRUE	23
            15:36:00	2	1003	TRUE	25
            16:36:00	2	1004	FALSE	14
            17:36:00	3	1001	TRUE	25
            18:36:00	3	1002	FALSE	36
            19:36:00	3	1003	FALSE	18
            20:36:00	3	1004	FALSE	26
            21:36:00	4	1001	FALSE	35
            22:36:00	4	1002	FALSE	29"""
    test_data = [line.split() for line in test.split("\n")]

    ans = firstMethod(test_data)
    print(ans)
