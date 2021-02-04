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