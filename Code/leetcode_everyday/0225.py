# coding   : utf-yi
# @Time    : 21/02/25 9:19
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0225.py
# @Software: PyCharm


from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        给你一个二维整数数组 matrix， 返回 matrix 的 转置矩阵 。
        矩阵的 转置 是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引
        :param matrix: [[1,2,3],[4,5,6],[7,8,9]]
        :return:[[1,4,7],[2,5,8],[3,6,9]]
        """
        m, n = len(matrix), len(matrix[0])
        res = [[0] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                res[j][i] = matrix[i][j]
        return res

    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) ->  bool:
        """
        490-m
        由空地和墙组成的迷宫中有一个球。球可以向上下左右四个方向滚动，但在遇到墙壁前不会停止滚动。当球停下时，可以选择下一个方向。
        给定球的起始位置，目的地和迷宫，判断球能否在目的地停下。
        迷宫由一个0和1的二维数组表示。 1表示墙壁，0表示空地。你可以假定迷宫的边缘都是墙壁。起始位置和目的地的坐标通过行号和列号给出。
        :param maze:[[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
        :param start:[0,4]
        :param destination:[4,4]
        :return:true
        """
        # m, n = len(maze), len(maze[0])
        # directions = [
        #     lambda point:[max(0, point[0] - 1), point[1]],
        #     lambda point:[min(m, point[0] + 1), point[1]],
        #     lambda point:[point[0], max(0, point[1] - 1)],
        #     lambda point:[point[0], min(n, point[1] + 1)]
        # ]
        # stack = [start]
        # while stack:
        #     curPoint = stack[-1]
        #     for dirs in directions:
        #         nextPoint = dirs(curPoint)
        #         if nextPoint == curPoint or maze[nextPoint[0]][nextPoint[1]] == 1:
        #             if curPoint == destination:
        #                 return True
        #
        #         if maze[nextPoint[0]][nextPoint[1]] == 0:
        #             stack.append(nextPoint)
        #             maze[nextPoint[0]][nextPoint[1]] = 2
        #             break
        #     else:
        #         maze[nextPoint[0]][nextPoint[1]] = 2
        #         stack.pop()
        # return False
        m, n = len(maze), len(maze[0])
        inRange = lambda x0, y0: 0 <= x0 < m and 0 <= y0 < n
        dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        stack = [tuple(start)]
        visited = set()
        while stack:
            x, y = stack.pop()
            if [x, y] == destination:
                return True
            visited.add((x, y))
            for d1, d2 in dirs:
                tmp_x, tmp_y = x, y
                while inRange(tmp_x + d1, tmp_y + d2) and maze[tmp_x + d1][tmp_y + d2]:
                    tmp_x += d1
                    tmp_y += d2
                if tmp_x == x and tmp_y == y:
                    continue

                if (tmp_x, tmp_y) not in visited:
                    stack.append((tmp_x, tmp_y))
        return False

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        剑指 Offer 59
        给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。
        队列
        :param nums:
        :param k:
        :return:
        """
        res = []
        queue = []
        if not nums or k == 0:
            return res
        for idx, num in enumerate(nums):
            if idx >= k and queue[0] <= idx - k:
                queue.pop(0)
            while queue and nums[queue[-1]] <= num:
                queue.pop()
            queue.append(idx)
            if idx >= k - 1:
                res.append(nums[queue[0]])
        return res

    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        """
        239 换方法 大根堆
        给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。
        队列
        :param nums:
        :param k:
        :return:
        """
        if not nums or k == 0:
            return []
        q = [(-nums[i], i) for i in range(k)]
        import heapq
        heapq.heapify(q)
        res = [-q[0][0]]
        for i in range(k, len(nums)):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            res.append(-q[0][0])
        return res

    def maxSlidingWindow3(self, nums: List[int], k: int) -> List[int]:
        """
        239 换方法 优先队列
        给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。
        :param nums:
        :param k:
        :return:
        """
        from collections import deque
        q = deque()
        n = len(nums)
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
        res = [nums[q[0]]]
        for i in range(k, n):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            while q[0] < i - k:
                q.pop(0)    # 等价 q.popleft()
            res.append(nums[q[0]])
        return res

    
    def test(self):
        ans = self.hasPath([[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], [0, 4], [4, 4])
        # ans = self.hasPath([[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], [0, 4], [3, 2])
        # ans = self.transpose([[1,2,3],[4,5,6],[7,8,9]])
        print(ans)


if __name__ == '__main__':
    solution = Solution()
    solution.test()
