<h2><a href="https://leetcode.com/problems/search-insert-position">35. Search Insert Position</a></h2><h3>Easy</h3><hr><p>Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.</p>

<p>You must&nbsp;write an algorithm with&nbsp;<code>O(log n)</code> runtime complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,5,6], target = 5
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,5,6], target = 2
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,5,6], target = 7
<strong>Output:</strong> 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>nums</code> contains <strong>distinct</strong> values sorted in <strong>ascending</strong> order.</li>
	<li><code>-10<sup>4</sup> &lt;= target &lt;= 10<sup>4</sup></code></li>
</ul>

### MY Solution 
```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for index, value in enumerate(nums):
            if value >= target: ### Return the index 
                return index
        return len(nums) #####
```
---
```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        preMid = 0

        if nums[l] == target: return l
        if nums[r] == target: return r

        while l <= r:
            mid = (l+r)//2
            if mid == preMid:
                break
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid
            else:
                r = mid
            
            preMid = mid
        
        if target > nums[r]:
            return r + 1
        elif target < nums[l]:
            return l
        else:
            return l + 1
```
---
# Optimal Solution
```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left  
```

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        if target<nums[left]:
            return left
        if target>nums[right]:
           return right+1

        while left <= right:
            mid = (right + left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left  
```
