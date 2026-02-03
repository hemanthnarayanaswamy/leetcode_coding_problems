<h2><a href="https://leetcode.com/problems/smallest-absent-positive-greater-than-average">4011. Smallest Absent Positive Greater Than Average</a></h2><h3>Easy</h3><hr><p>You are given an integer array <code>nums</code>.</p>

<p>Return the <strong>smallest absent positive</strong> integer in <code>nums</code> such that it is <strong>strictly greater</strong> than the <strong>average</strong> of all elements in <code>nums</code>.</p>
The <strong>average</strong> of an array is defined as the sum of all its elements divided by the number of elements.
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,5]</span></p>

<p><strong>Output:</strong> <span class="example-io">6</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The average of <code>nums</code> is <code>(3 + 5) / 2 = 8 / 2 = 4</code>.</li>
	<li>The smallest absent positive integer greater than 4 is 6.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [-1,1,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>​​​​​​​The average of <code>nums</code> is <code>(-1 + 1 + 2) / 3 = 2 / 3 = 0.667</code>.</li>
	<li>The smallest absent positive integer greater than 0.667 is 3.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [4,-1]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The average of <code>nums</code> is <code>(4 + (-1)) / 2 = 3 / 2 = 1.50</code>.</li>
	<li>The smallest absent positive integer greater than 1.50 is 2.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

# Solution 
* The Average needs to in float, then `num = floor(avg) + 1` **Instead of using the int, floor the avg and add 1**
* The Question is asking for the missing positive number, if `num <= 0`, we reset that to `num = 1`, before stating the search in the while loop.
* Compute the average, `set x = floor(avg) + 1` (the smallest integer greater than the average).

```python
class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        total = sum(nums)
        avg = total / len(nums)
        numsPresent = set(nums)
        num = floor(avg) + 1 # Instead of using the int, floor the avg and add 1
        
        if num <= 0:
            num = 1

        while num in numsPresent:
            num += 1
        
        return num
```
---
```python
class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        avg = sum(nums) / len(nums)
        num = max(1, floor(avg) + 1) #Instead of using the int, floor the avg and add 1
        numsPresent = set(nums) # if num is negative we are resetting its start value to 1
        
        while num in numsPresent:
            num += 1
        
        return num
```
					

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code>​​​​​​​</li>
</ul>
