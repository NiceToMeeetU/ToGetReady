# coding   : utf-8 
# @Time    : 21/03/11 12:57
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : BinarySearch.py
# @Software: PyCharm


class BinarySearch:
    def typicalBF(self, nums, target):
        """
        最常规的经典写法，注意：
        - 加法变减法避免溢出
        - 边界条件！
        - elif写清楚，不要else
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                return mid

        return -1

    def left_bount_BF(self, nums, target):
        """
        只找左边界的写法
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                right = mid - 1     # 找到后不急着返回，将右侧边界往左压缩
        if left >= len(nums) or nums[left] != target:
            return -1
        return left

    def right_bound_BF(self, nums, target):
        """
        只找右侧边界的写法
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                left = mid + 1
        if right < 0 or nums[right] != target:
            return -1
        return right

if __name__ == '__main__':
    bf = BinarySearch()
    print(bf.typicalBF([1, 2, 2, 2, 3, 4, 4, 5, 5], 2))         # 1
    print(bf.left_bount_BF([1, 2, 2, 2, 3, 4, 4, 5, 5], 2))     # 1
    print(bf.right_bound_BF([1, 2, 2, 2, 3, 4, 4, 5, 5], 2))    # 3
