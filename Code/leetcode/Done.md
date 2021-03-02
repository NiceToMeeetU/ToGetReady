# All Programming Questions Done in my Interview



### 哈希表问题:x:

2021.01.25-字节-大数据开发

```python
class Solution:
   def seg(self, nums, w):
        """
        字节面试题
        给定一个无序整数数组， 判断这个数组是否可以重新分组，使得每个组内的元素个数为w，且这些数字是连续的数字
        :param nums:[1,2,3,6,2,3,4,7,8]
        :param w:3
        :return:True, ([[1,2,3],[2,3,4],[6,7,8]])
        时间空间都是O(n)
        """
        n = len(nums)
        if n % w != 0:
            return False
        from collections import Counter
        hash_nums = Counter(nums)
        # print(f"{hash_nums=}")
        for k in sorted(hash_nums.keys()):
            # print(k)
            if hash_nums[k] == 0:
                continue
            i = 0
            while i < w:
                # print(f"{k=}, {i=}, {hash_nums=}")
                if hash_nums[k + i] == 0:
                    return False
                hash_nums[k + i] -= 1
                i += 1
        return True
```

### TopN问题:x:

2021.01.28-滴滴货运-数据分析

`student`表含有三个字段，`stu_id`，`course_id`，`score`，求每个学生的最高分，每个人分数排第二的课程。

```mysql
-- top 1 score of each student
select 
	s1.stu_id
	s1.score
from
    student as s1
where
	(select count (distinct s2.score) 
     from
    	student as s2
     where
    	s1.stu_id = s2.stu_id
     and 
    	s2.score > s1.score
    ) = 0
------
select
	s1.stu_id
	s1.course_id
	s1.score
from
    student as s1
where
	(select count (distinct s2.score) 
     from
    	student as s2
     where
    	s1.stu_id = s2.stu_id
     and 
    	s2.score > s1.score
    ) = 1
	
```

### BFS问题:x:

2021.02.02-依图-算法

```python
class Solution:
    def maxFace(self, labels: List[List[int]]):
        """
        依图面试题
        给定一个二维整数数组，内容是某图片上各像素点是否为人脸的0，1标签，相邻的1标签可认为是同一张脸，求该张照片里面积最大的人脸的像素点数。
        :param labels:
        :return:
        BFS 经典解法
        """
        m, n = len(labels), len(labels[0])
        import collections
        res = 0
        for i in range(m):
            for j in range(n):
                if labels[i][j] == 1:
                    tmp = collections.deque()
                    tmp_count = 1
                    labels[i][j] = -1
                    tmp.append([i, j])
                    while len(tmp) > 0:
                        x, y = tmp.popleft()
                        for new_x, new_y in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]:
                            if 0 <= new_x < m and 0 <= new_y < n and labels[new_x][new_y] == 1:
                                tmp_count += 1
                                labels[new_x][new_y] = -1
                                tmp.append([new_x, new_y])
                    res = max(res, tmp_count)
        return res
```

### 位运算/哈希表:heavy_check_mark:

2020.02.08-快手-算法

给定整数数组`nums`，其中有一个元素出现了一次，其他元素都出现了偶数次，找出这个出现一次的元素

```python
class Solution:
    def singleNumber_1(self, nums: List[int]) -> int:
        """
        紧紧抓住偶数次的条件，看到后要及时想到偶数次的异或结果都是1
        空间复杂度：O(1)
        """
        res = 0
        for num in nums:
            res ^= num
        return res
   	
    def singleNumber_2(self, nums: list(int)) -> int:
        """
        巧妙地不使用多余空间的方法，删除多空出现的元素，通过报错跳出循环
        空间复杂度：O(1)
        """
        while True:
            d = nums[0]
            nums.remove(d)
            try:
                nums.remove(d)
            except:
                return d
            
    def singleNumber_3(self, nums: list(int)) -> int:
        """
        基本的哈希表方法
        """
        

```

### 留存矩阵:x:

2021.03.01-知乎-数分

`Log`表，`user_id`, `log_date`字段，求从`2020-03-01`起一整个月的30日留存矩阵

```mysql
-- 
```



