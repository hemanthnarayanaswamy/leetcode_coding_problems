<h2><a href="https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array">34. Find First and Last Position of Element in Sorted Array</a></h2><h3>Medium</h3><hr><p>Given an array of integers <code>nums</code> sorted in non-decreasing order, find the starting and ending position of a given <code>target</code> value.</p>

<p>If <code>target</code> is not found in the array, return <code>[-1, -1]</code>.</p>

<p>You must&nbsp;write an algorithm with&nbsp;<code>O(log n)</code> runtime complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [5,7,7,8,8,10], target = 8
<strong>Output:</strong> [3,4]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [5,7,7,8,8,10], target = 6
<strong>Output:</strong> [-1,-1]
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [], target = 0
<strong>Output:</strong> [-1,-1]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup>&nbsp;&lt;= nums[i]&nbsp;&lt;= 10<sup>9</sup></code></li>
	<li><code>nums</code> is a non-decreasing array.</li>
	<li><code>-10<sup>9</sup>&nbsp;&lt;= target&nbsp;&lt;= 10<sup>9</sup></code></li>
</ul>

# Solution 
* UseBinary Search to solve the problem in `O(logn)` complexity
* use two pointer to store all the index values into a result list `O(n)` as the pointer touchs all the input elements atleast once.
* Then if the result list is empty return -1 or the min and max values in the list 

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = []
        left, right = 0, len(nums)-1

        while left <= right:
            if nums[left] == target:
                result.append(left)
            
            if nums[right] == target:
                result.append(right)
            
            left += 1
            right -= 1
        
        if len(result):
            return [min(result), max(result)]
        else:
            return [-1, -1]
```

# Optimal Binary Search Solution
* We can improve the logic for storing the min and max values inside the while loop. 

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst():
            left, right = 0, len(nums) - 1
            first = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    first = mid
                    right = mid - 1  # Keep looking on the left
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return first

        def findLast():
            left, right = 0, len(nums) - 1
            last = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    last = mid
                    left = mid + 1  # Keep looking on the right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return last

        return [findFirst(), findLast()]
```
