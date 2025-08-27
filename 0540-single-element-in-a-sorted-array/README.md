<h2><a href="https://leetcode.com/problems/single-element-in-a-sorted-array">540. Single Element in a Sorted Array</a></h2><h3>Medium</h3><hr><p>You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.</p>

<p>Return <em>the single element that appears only once</em>.</p>

<p>Your solution must run in <code>O(log n)</code> time and <code>O(1)</code> space.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,1,2,3,3,4,4,8,8]
<strong>Output:</strong> 2
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [3,3,7,7,10,11,11]
<strong>Output:</strong> 10
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>

# Solution 
```python
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        numsFreq = Counter(nums)

        for k, v in numsFreq.items():
            if v == 1:
                return k
```

# Optimal Solution
```ini
This question is very similar to Binary Search algorithm. If you look at the example below you will see that:

* If the number at index m is the same as the number at index m-1, the unique number cannot be on the right side of the middle, as there are an even number of numbers ((r-m) % 2 = 0) on that side (first example below). However, if we had an odd number of numbers, the unique number would have to be on the right side.
* If the number at index m is the same as the number at index m+1, the unique number must be on the right side of the middle, since there are an even number of numbers ((r-m) % 2 = 0) on that side (second example below). However, if we had an odd number of numbers, the unique number would have to be on the left side from the middle.
* If the number at index m is different from the numbers at indexes m+1 and m-1, it is the unique number.
```
```python
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)//2 
            if mid + 1 < len(nums):
                if mid % 2 == 0 and nums[mid] == nums[mid+1]:
                    l = mid + 1
                elif mid % 2 and nums[mid] == nums[mid+1]:
                    r = mid - 1
                elif mid % 2 and nums[mid] == nums[mid-1]:
                    l = mid + 1
                elif mid % 2 == 0 and nums[mid] == nums[mid - 1]:
                    r = mid - 1
                else:
                    return nums[mid]
            else:
                return nums[mid]

        return nums[mid]
```

`In a sorted array where every element appears twice except one, the single element disrupts the pairing pattern.`

```ini
# Normal pairing (without single element):
[1,1,2,2,3,3,4,4] 
# Indices: 0,1,2,3,4,5,6,7
# Pairs: (0,1), (2,3), (4,5), (6,7)

# With single element:
[1,1,2,3,3,4,4]
# Indices: 0,1,2,3,4,5,6  
# Before single: (0,1) - pairs start at even indices
# After single: (3,4), (5,6) - pairs start at odd indices
```

```ini
- Before the single element:
       Pairs start at even indices: (0,1), (2,3), (4,5)...
       nums[even] == nums[even+1]

- After the single element:
       Pairs start at odd indices: (1,2), (3,4), (5,6)...
       nums[odd] == nums[odd+1]
```
---
# Optimal Solution
```python
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (right + left) // 2
            
            if mid % 2 == 1:
                mid -= 1
            
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid
        
        return nums[left]
```

```ini
# Iteration 1:
left=0, right=8, mid=4
mid % 2 == 0, so mid stays 4
nums[4]=3, nums[5]=4 → 3 ≠ 4 (pair broken)
right = mid = 4

# Iteration 2:  
left=0, right=4, mid=2
mid % 2 == 0, so mid stays 2
nums[2]=2, nums[3]=3 → 2 ≠ 3 (pair broken)
right = mid = 2

# Iteration 3:
left=0, right=2, mid=1
mid % 2 == 1, so mid = 0
nums[0]=1, nums[1]=1 → 1 == 1 (pair intact)
left = mid + 2 = 2

# Now left == right == 2
# Return nums[2] = 2 ✅
```
