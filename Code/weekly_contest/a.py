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

    def countMatches1(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        """
        高手写法，三个if可以直接将最后一个去掉，判断语句放到循环的外面，减少一半的运行时间
        """
        if ruleKey == "type":
            return sum(item[0] == ruleValue for item in items)
        elif ruleKey == "color":
            return sum(item[1] == ruleValue for item in items)
        return sum(item[2] == ruleValue for item in items)

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

        折腾了好久最后还是没有提交成功
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
    def closetCost1(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        """大神解法"""
        def dfs(start, i):
            nonlocal cost
            if (abs(start - target) < abs(cost < target)) or (start < cost and abs(start - target) == abs(cost - target)):
                cost = start
            if i >= len(toppingCosts):
                return
            for k in range(3):
                dfs(start + k * toppingCosts[i], i + 1)
        cost = float("inf")
        for base in baseCosts:
            dfs(base, 0)
        return cost

    def closetCost2(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        """
        居然还可以直接暴力穷举
        """
        import itertools
        n, m = len(baseCosts), len(toppingCosts)
        ans = baseCosts[0]

        # 神之一笔，因为m，n有限，直接构造完整的可选组合穷举
        # itertools.product()
        for choice in itertools.product(range(3), repeat=m):


            topping = sum(c1 * c2 for c1, c2 in zip(toppingCosts, choice))
            for b in baseCosts:
                cost = topping + b
                # 直接在ans的赋值判断语句中定义好条件，总的abs差异要小且选择更低的值
                # 一步到位，不用选择嵌套循环，用or比两个if来的实在的多。
                if abs(cost - target) < abs(ans - target) or (abs(cost-target) == abs(ans - target) and cost < ans):
                    ans = cost
        return ans
    def closetCost3(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        """
        枚举出所有子集的和后二分查找
        """
        import bisect
        toppingSum = {0, }
        for t in toppingCosts * 2:
            toppingSum |= set([s + t for s in toppingSum])
        toppingSum = sorted(toppingSum)
        l = len(toppingSum)

        # 二分
        ans = 1000000007
        for c in baseCosts:
            i = bisect.bisect_right(toppingSum, target - c)
            if i > 0 and abs(c + toppingSum[i - 1] - target) < abs(ans - target):
                ans = c + toppingSum[i - 1]
            if i < 1 and abs(c + toppingSum[i] - target) < abs(ans - target):
                ans = c + toppingSum[i]
        return ans

    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        """
        给你两个长度可能不等的整数数组 nums1 和 nums2 。两个数组中的所有值都在 1 到 6 之间（包含 1 和 6）。
        每次操作中，你可以选择 任意 数组中的任意一个整数，将它变成 1 到 6 之间 任意 的值（包含 1 和 6）。
        请你返回使 nums1 中所有数的和与 nums2 中所有数的和相等的最少操作次数。如果无法使两个数组的和相等，请返回 -1 。
        :param nums1:
        :param nums2:
        :return:
        两个数组的和是一定的，其差值也是一定的，想让其和相等无非是让小的数组更大一点，大的数组更小一点
        小数组能增大的量即sum(6 - i for i in nums1)
        大数组能减小的量即sum(i - 1 for i in nums2)
        即最大增量、最大减量是一定的
        如果所有的裕量全部用完都无法相等则肯定没有办法了
        如果裕量足够，只需在其中选取最少的次数即可
        """
        from collections import Counter
        s1 = sum(nums1)
        s2 = sum(nums2)
        if s1 == s2:
            return 0
        elif s1 > s2:
            return self.minOperations(nums2, nums1)

        diff = s2 - s1
        freq = Counter(6 - i for i in nums1) + Counter(i - 1 for i in nums2)
        ans = 0
        for i in range(5, 0, -1):
            if diff <= 0:
                break
            for _ in range(freq[i]):
                if diff <= 0:
                    break
                ans += 1
                freq[i] -= 1
                diff -= i
        return -1 if diff > 0 else ans

    def minOperations2(self, nums1: List[int], nums2: List[int]) -> int:
        """
        统计各位上可以贡献的差值，从大到小遍历
        """
        diff = sum(nums2) - sum(nums1)
        cost = [0] * 6
        # 不失一般性，假定num1 < nums2
        for num in nums1:
            cost[6 - (num - 1)] += 1
        for num in nums2:
            cost[num - 1] += 1






    def test(self):
        # ans = self.closestCost([2, 3], [4, 5, 100], 18)
        ans = self.minOperations([1,1,1,1,1,1,1],[6])
        print(ans)


if __name__ == '__main__':
    solution = Solution()
    solution.test()
