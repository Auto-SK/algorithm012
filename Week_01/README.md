# 学习笔记

## 双指针法总结

所谓双指针，指的是在遍历对象的过程中，不是使用一个指针单向进行访问，而是使用两个指针从相同方向或相反方向进行扫描，从而达到相应的目的。

[1. 两数之和](https://leetcode-cn.com/problems/two-sum/)

在该题中，使用两个指针==i==和==j==，一前一后扫描整个数组，当元素和为==target==时返回两个元素的索引。

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i, j]
```

[11. 盛水最多的容器](https://leetcode-cn.com/problems/container-with-most-water/)

在该题中，使用两个指针==left==和==right==，分别指向数组的最左端和最右端。此时，两条垂直线的距离是最短的，若要使下一个矩形的面积比当前的更大，必须使==height[left]==和==height[right]==中较短的垂直线向中间移动，寻找更长的垂直线。

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        left, right = 0, len(height) - 1
        while (left < right):
            if height[l] < height[r]:
                ans = max(ans, height[l] * (right - left))
                left += 1
            else:
                ans = max(ans, height[r] * (right - left))
                right -= 1
        return ans
```

 [42. 接雨水](https://leetcode-cn.com/problems/trapping-rain-water/)

在该题中，使用两个指针==left==和==right==，分别指向数组的最左端和最右端。使用==left_max==记录左边最大值，==right_max==记录右边最大值，当左边的高度小于右边的高度时，说明可以盛水，更新左边指针和结果，否则更新右边的指针和结果，直至相遇。

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        ans, left_max, right_max = 0, 0, 0
        while (left < right):
            if (height[left] < height[right]):
                left_max = max(left_max, height[left])
                ans += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                ans += right_max - height[right]
                right -= 1
        return ans
```

[15. 三数之和](https://leetcode-cn.com/problems/3sum/)

在该题中，先将数组==nums==排序，然后使用三个索引==k==、==l==、==r==，分别用来遍历数组、指向左端、指向右端。因为==nums[r]>nums[l]>nums[k]==，如果 ==nums[k]==大于 0，则三数之和必然无法等于 0，结束循环。如果 ==nums[i] == nums[i-1]==，则说明该数字重复，会导致结果重复，所以应该跳过。如果==nums[k] + nums[l] + nums[r] == 0==，则添入结果，移动两个指针。如果==nums[k] + nums[l] + nums[r] < 0==，向右移动左指针，否则向左移动右指针。

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        ans = []
        if (not nums or length < 3):
            return ans
        nums.sort()
        for k in range(length - 2):
            # 如果当前数字大于0，则三数之和一定大于0，所以结束循环
            if (nums[k] > 0):
                return ans
            # 去重
            if (k > 0 and nums[k] == nums[k - 1]): 
                continue
            l, r = k + 1, length - 1
            while (l < r):
                if (nums[k] + nums[l] + nums[r] == 0):
                    ans.append([nums[k], nums[l], nums[r]])
                    # 去重
                    while (l < r and nums[l] == nums[l + 1]):
                        l += 1
                    # 去重
                    while (l < r and nums[r] == nums[r - 1]):
                        r -= 1
                    l += 1
                    r -= 1
                elif (nums[k] + nums[l] + nums[r] < 0):
                    l += 1
                else:
                    r -= 1
        return ans
```
