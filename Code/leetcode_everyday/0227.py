# coding   : utf-8 
# @Time    : 21/02/27 19:00
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0227.py
# @Software: PyCharm


from typing import List


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        """
        给你一个字符串 s 和一个整数 k ，请你找出 s 中的最长子串， 要求该子串中的每一字符出现次数都不少于 k 。返回这一子串的长度。
        :param s:"aaabb"
        :param k:3
        :return:3
        求次数都大于k应该如何设置窗口滑动条件？
        如果只是小于k则明显好做的多，直接超过阈值后左移即可
        居然是特么考分治策略，完全不会啊

        如果字符串中某些字的出现次数小于k，则其一定不会出现在结果中，那么该字就可以将整个字符串拆分
        问题就得到了简化，再在拆分好的部分子串内继续迭代即可。
        python分割字符串的时候直接用split函数将参数传递进去即可，不要自己造轮子
        """
        if len(s) < k:
            return 0
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)

    def majorityElement(self, nums: List[int]) -> int:
        """
        紧接着赶紧做一道分治的简单题压压惊
        169-e
        给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
        你可以假设数组是非空的，并且给定的数组总是存在多数元素。
        :param nums:[3, 2, 3]
        :return:3
        如果直接模拟的话，需要遍历完整个数组，O(n)逃不了的。
        注意到题设的条件，一定存在多数元素。
        如果一个数组存在多数元素，那么其一半内必然也存在多数元素，这样就可以采用分治策略尝试

        思路是对的，但实际应该并不会降低时间复杂度，至少都得完整遍历一遍。
        1、直接遍历模拟，O(n)；
        2、排序，多数元素一定出现在中间位置，O(nlogn)；
        3、分治，
        4、摩尔投票，依次遍历，不一样的元素相互抵消，最后剩下的一定是多数元素
        """
        # 第一次写的强行相互抵消实在不行！
        # i = 0
        # while i > len(nums) - 1:
        #     if nums[i] != nums[i + 1]:
        #         nums.pop(i)
        #         nums.pop(i)
        #         i = 0
        #     else:
        #         i += 1
        #     print("---")
        # return nums[0]

        # 特么的好比想一想自己为啥会铁憨憨地真的去pop抵消
        count = 0
        res = nums[0]
        for i in range(len(nums)):
            if res == nums[i]:
                count += 1
            else:
                count -= 1

            if count == 0:
                res = nums[i + 1]
        return res




    def test(self):
        # ans = self.longestSubstring("aaabb", 3)
        ans = self.majorityElement([1,2,3,2,2,2,2,1,2,2,2,2,1,1])
        print(ans)

if __name__ == '__main__':
    solution = Solution()
    solution.test()


