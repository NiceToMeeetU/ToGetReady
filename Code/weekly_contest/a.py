# coding   : utf-8 
# @Time    : 21/02/28 10:30
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : a.py
# @Software: PyCharm
from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        """
        给你一个数组 items ，其中 items[i] = [typei, colori, namei] ，描述第 i 件物品的类型、颜色以及名称。
        另给你一条由两个字符串 ruleKey 和 ruleValue 表示的检索规则。
        如果第 i 件物品能满足下述条件之一，则认为该物品与给定的检索规则 匹配 ：
        ruleKey == "type" 且 ruleValue == typei 。
        ruleKey == "color" 且 ruleValue == colori 。
        ruleKey == "name" 且 ruleValue == namei 。
        统计并返回 匹配检索规则的物品数量 。
        :param items:
        :param ruleKey:
        :param ruleValue:
        :return:
        """
        res = 0
        for t, c, n in items:
            if ruleKey == "type" and ruleValue == t:
                res += 1
            elif ruleKey == "color" and ruleValue == c:
                res += 1
            elif ruleKey == "name" and ruleValue == n:
                res += 1
        return res

    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        """
        你打算做甜点，现在需要购买配料。目前共有 n 种冰激凌基料和 m 种配料可供选购。
        而制作甜点需要遵循以下几条规则：
            必须选择 一种 冰激凌基料。
            可以添加 一种或多种 配料，也可以不添加任何配料。
            每种类型的配料 最多两份 。
        给你以下三个输入：
        baseCosts ，一个长度为 n 的整数数组，其中每个 baseCosts[i] 表示第 i 种冰激凌基料的价格。
        toppingCosts，一个长度为 m 的整数数组，其中每个 toppingCosts[i] 表示 一份 第 i 种冰激凌配料的价格。
        target ，一个整数，表示你制作甜点的目标价格。
        你希望自己做的甜点总成本尽可能接近目标价格 target 。
        返回最接近 target 的甜点成本。如果有多种方案，返回 成本相对较低 的一种。
        :param baseCosts:
        :param toppingCosts:
        :param target:
        :return:
        最后的目标函数是从两个方向逼近target
        在距离相同的情况下才考虑选择更低价格的方案
        baseCosts最多10种，是否可以考虑全部遍历一遍？
        toppingCosts最多两份，那么直接将该数组扩充一倍后在内抽选组合即可。

        """
        n, m = len(baseCosts), len(toppingCosts)
        # toppingCosts = toppingCosts + toppingCosts  # 扩充配料表
        toppingCosts = [toppingCosts[idx // 2] for idx in range(2 * len(toppingCosts))]

        def flat(array, pos, flat_array):

            """
            param..
            array: 原数组
            pos  当前位置
            flat_array : 当前枚举数组的结果
            """
            if pos > len(array) - 1:
                return flat_array
            temp = flat_array + [ele + array[pos] for ele in flat_array]
            return flat(array, pos + 1, temp)

        left = flat(toppingCosts[:m], 0, [0])
        right = flat(toppingCosts[m:], 0, [0])
        print(f"{left=}")
        print(f"{right=}")
        res = float('inf')
        ans = float('inf')
        for base in baseCosts:
            left_id = 0
            right_id = 0
            print(f"{base = }")
            print("_______________")
            while left_id < len(left) and right_id < len(right):
                cur = left[left_id] + right[right_id] + base
                print("######")
                print(f"base={base}, topping={left[left_id] + right[right_id]}")
                if abs(cur - target) < ans:
                    ans = abs(cur - target)
                    res = cur
                # ans = min(abs(cur - target), ans)
                if abs(cur - target) == ans:
                    res = min(cur, res)

                if cur + base > target:
                    right_id += 1
                elif cur + base < target:
                    left_id += 1
                # else:
                #     return target + base
                # print(f"{ans=}")
                print(f"{res=}")
        return res

    def closestCost2(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        """
        你打算做甜点，现在需要购买配料。目前共有 n 种冰激凌基料和 m 种配料可供选购。
        而制作甜点需要遵循以下几条规则：
            必须选择 一种 冰激凌基料。
            可以添加 一种或多种 配料，也可以不添加任何配料。
            每种类型的配料 最多两份 。
        给你以下三个输入：
        baseCosts ，一个长度为 n 的整数数组，其中每个 baseCosts[i] 表示第 i 种冰激凌基料的价格。
        toppingCosts，一个长度为 m 的整数数组，其中每个 toppingCosts[i] 表示 一份 第 i 种冰激凌配料的价格。
        target ，一个整数，表示你制作甜点的目标价格。
        你希望自己做的甜点总成本尽可能接近目标价格 target 。
        返回最接近 target 的甜点成本。如果有多种方案，返回 成本相对较低 的一种。
        :param baseCosts:
        :param toppingCosts:
        :param target:
        :return:
        最后的目标函数是从两个方向逼近target
        在距离相同的情况下才考虑选择更低价格的方案
        baseCosts最多10种，是否可以考虑全部遍历一遍？
        toppingCosts最多两份，那么直接将该数组扩充一倍后在内抽选组合即可。

        """
        n, m = len(baseCosts), len(toppingCosts)
        toppingCosts.sort()
        # toppingCosts = toppingCosts + toppingCosts  # 扩充配料表
        toppingCosts = [toppingCosts[idx // 2] for idx in range(2 * len(toppingCosts))]

        def flat(array, pos, flat_array):
            if pos > len(array) - 1:
                return flat_array
            temp = flat_array + [ele + array[pos] for ele in flat_array]
            return flat(array, pos + 1, temp)

        left = flat(toppingCosts[:m], 0, [0])
        right = flat(toppingCosts[m:], 0, [0])
        print(f"{left=}")
        print(f"{right=}")
        res = float('inf')
        ans = float('inf')
        for base in baseCosts:
            i, j =0, 0
            for j in range(m):

        return res



    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        """
        给你两个长度可能不等的整数数组 nums1 和 nums2 。两个数组中的所有值都在 1 到 6 之间（包含 1 和 6）。
        每次操作中，你可以选择 任意 数组中的任意一个整数，将它变成 1 到 6 之间 任意 的值（包含 1 和 6）。
        请你返回使 nums1 中所有数的和与 nums2 中所有数的和相等的最少操作次数。如果无法使两个数组的和相等，请返回 -1 。
        :param nums1:
        :param nums2:
        :return:
        """


    def test(self):
        ans = self.closestCost([2,3], [4,5,100], 18)
        print(ans)

if __name__ == '__main__':
    solution = Solution()
    solution.test()