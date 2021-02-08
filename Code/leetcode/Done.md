# All Programming Questions Done in my interview

1. 【字节】给定一个无序整数数组， 判断这个数组是否可以重新分组，使得每个组内的元素个数为w，且这些数字是连续的数字。

   如数组`nums = [1,2,3,6,2,3,4,7,8]`，`w = 3`，返回`True`，可分为`[[1,2,3],[2,3,4],[6,7,8]]`

   ```python
   class Solution:
       def repartition(self, nums: list(int), w: int):
           
           return True
   ```

2. 【滴滴】`student`表含有三个字段，`stu_id`，`course_id`，`score`，球每个学生的最高分，每个人分数排第二的课程。

   ```mysql
   -- top 1 score of each student
   select 
   ```

3. 【依图】给定一个二维整数数组，内容是某图片上各像素点是否为人脸的0，1标签，相邻的1标签可认为是同一张脸，求该张照片里面积最大的人脸的像素点数。

   ```python
   class Solution:
       def maxFace(self, labels : list(list(int))):
           
           return 1
   ```

4. 【快手】给定整数数组`nums`，其中有一个元素出现了一次，其他元素都出现了偶数次，找出这个出现一次的元素

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

   

5. 【】

