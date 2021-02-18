## 02.03-滑动窗口中位数问题

https://leetcode-cn.com/problems/sliding-window-median/

不要被困难吓倒，仔细想一想先用暴力法来一发，然后慢慢优化

```python
import bisect
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        median = lambda a: (a[(len(a)-1)//2] + a[len(a)//2])/2
        a = sorted(nums[:k])
        res = [median(a)]
        for i,j in zip(nums[:-k], nums[k:]):
            a.remove(i)
            a.insert(bisect.bisect_left(a,j), j)
            res.append(median(a))
        return res 
        
```

- 二分查找，直接用`bisect`包即可，高效插入；

- 滑动窗口遍历的骚操作，直接对初始窗口之后每一个添加和删除的元素做遍历

  `for i, j in zip(nums[:-k], nums[k:])`

### 02.04-滑动窗口平均值问题



- 自己写二分查找的话，一定注意
  - 不要写`mid = (left+right)/2`太低级；
  - 写成`mid = left + (right-left)/2`用减法替代加法更鲁棒。







双指针滑动窗口时，注意是要求最大子串长度还是最小子串长度，这在内层循环确定如何移动左指针时是完全相反的判别



链表问题可以考虑迭代法和递归法



用栈实现队列，不要简单地用两个list做栈来回倒腾，pop和peek的时间复杂度过高，可以直接设置一个front变量存储入栈的栈底元素，作为队列的first元素用于弹出。s_in为空时同时将front置空即可，两个栈互不牵连。



优先队列的实现机制：

- heap堆
- 二叉搜索树





![image-20210218131819713](http://wy-typora-img.oss-cn-chengdu.aliyuncs.com/img/image-20210218131819713.png)

![image-20210218131836118](http://wy-typora-img.oss-cn-chengdu.aliyuncs.com/img/image-20210218131836118.png)





按着换的排序方法都是稳定的

否则都是不稳定排序