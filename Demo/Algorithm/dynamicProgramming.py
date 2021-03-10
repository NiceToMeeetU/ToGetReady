# coding   : utf-8 
# @Time    : 21/03/10 10:54
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : dynamicProgramming.py
# @Software: PyCharm


"""
动态规划问题
一种算法思想：若要解一个给定问题，我们需要解其不同部分（即子问题），再根据子问题的解以得到原问题的解。
- 子问题与原问题的关系 对应最优子结构问题
- 子问题之间的关系  对应重复子问题


考虑能否将问题规模缩小：
- 数组上常用思路：
    - 每次减少一半
    - 每次减少一个

问题解法从三个方向考虑选择：
- 递归
- top-down 记忆化
- bottom-up 迭代

动态规划和分治的区别：
动态规划有子问题【重复】出现
"""

from typing import List










