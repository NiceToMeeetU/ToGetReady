# coding   : utf-8 
# @Time    : 21/02/16 19:24
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : _TOOL.py
# @Software: PyCharm


import time


def cal_time(func):
    """
    程序计时简单装饰器
    """
    def wrapper(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        t2 = time.time()
        print(f"###     Func {func.__name__} running time: {t2 -t1:0.4f} s")
        return res
    return wrapper

