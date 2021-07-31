# coding   : utf-8 
# @Time    : 21/05/21 15:55
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : K.py
# @Software: PyCharm


import json
import sys


def str2form(json_str: str):
    """
    将Leetcode中SQL题的Str式输入输出转换为直观的表格形式
    :param json_str:
    :return: None
    """
    data = json.loads(json_str)  # 解析json_str
    keys = list(data.keys())

    headers = data[keys[0]]
    values = data[keys[1]]

    if keys[1] == "rows":
        for h, v in zip(headers.items(), values.items()):
            table_name = h[0]
            print(f"\n[{table_name}]：")
            table = [h[1]] + v[1]
            columns = list(zip(*table))
            max_weights = [max(list(map(lambda x: len(str(x)), c))) for c in columns]  # 找各列的最宽值

            for row, line in enumerate(table):
                print("|", end=" ")
                for c, item in enumerate(line):
                    print(" " * (max_weights[c] - len(str(item))) + str(item) + " |", end=" ")
                print()
                if row == 0:  # 打印了表头后输出一行横线
                    print("—" * (sum(max_weights) + 3 * len(max_weights) + 1))

    elif keys[1] == "values":
        table = [headers] + values
        columns = list(zip(*table))
        max_weights = [max(list(map(lambda x: len(str(x)), c))) for c in columns]  # 找各列的最宽值

        for row, line in enumerate(table):
            print("|", end=" ")
            for c, item in enumerate(line):
                print(" " * (max_weights[c] - len(str(item))) + str(item) + " |", end=" ")
            print()
            if row == 0:  # 打印了表头后输出一行横线
                print("—" * (sum(max_weights) + 3 * len(max_weights) + 1))


if __name__ == '__main__':
    # args = sys.argv
    # # str2form(args[1])
    # print(args)
    # print()
    # print(args[1])
    # print()
    # print("""{"headers": {"Tasks": ["task_id", "subtasks_count"], "Executed": ["task_id", "subtask_id"]}, "rows": {"Tasks": [[1, 3], [2, 2], [3, 4]], "Executed": [[1, 2], [3, 1], [3, 2], [3, 3], [3, 4]]}}""")
    # str2form("""{"headers": {"Tasks": ["task_id", "subtasks_count"], "Executed": ["task_id", "subtask_id"]}, "rows": {"Tasks": [[1, 3], [2, 2], [3, 4]], "Executed": [[1, 2], [3, 1], [3, 2], [3, 3], [3, 4]]}}""")
    
    while True:
	    s = input()
	    str2form(s.strip())