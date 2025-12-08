<h2><a href="https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer">2614. Maximum Count of Positive Integer and Negative Integer</a></h2><h3>Easy</h3><hr><p>Given an array <code>nums</code> sorted in <strong>non-decreasing</strong> order, return <em>the maximum between the number of positive integers and the number of negative integers.</em></p>

<ul>
	<li>In other words, if the number of positive integers in <code>nums</code> is <code>pos</code> and the number of negative integers is <code>neg</code>, then return the maximum of <code>pos</code> and <code>neg</code>.</li>
</ul>

<p><strong>Note</strong> that <code>0</code> is neither positive nor negative.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [-2,-1,-1,1,2,3]
<strong>Output:</strong> 3
<strong>Explanation:</strong> There are 3 positive integers and 3 negative integers. The maximum count among them is 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [-3,-2,-1,0,0,1,2]
<strong>Output:</strong> 3
<strong>Explanation:</strong> There are 2 positive integers and 3 negative integers. The maximum count among them is 3.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,20,66,1314]
<strong>Output:</strong> 4
<strong>Explanation:</strong> There are 4 positive integers and 0 negative integers. The maximum count among them is 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2000</code></li>
	<li><code>-2000 &lt;= nums[i] &lt;= 2000</code></li>
	<li><code>nums</code> is sorted in a <strong>non-decreasing order</strong>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Can you solve the problem in <code>O(log(n))</code> time complexity?</p>

# Solution 
* We only count the negative numbers and when we find our first positive number, we break the loop. 
```python
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        negative = positive = 0
        n = len(nums)

        for i in range(n):
            if nums[i] > 0:
                positive = n - i
                break
            elif nums[i] < 0:
                negative += 1
        
        return max(negative, positive)
```
# Binary Search
**You’re off by one because your searches use a closed interval `[0, n-1]` but then you return an index even when no element matches. For this problem you need functions that can legally return `n`**

```ini 
if l, r = 0, len(nums) then while loop should be l < r
if l, r = 0, len(nums)-1 then while loop should be l <= r
```

```python
class Solution:
    def upperBound(self, nums):
        n = len(nums)
        l, r = 0, n

        while l < r:
            m = (l + r) // 2
            if nums[m] <= 0:
                l = m + 1
            else:
                r = m
        
        return l
    
    def lowerBound(self, nums):
        n = len(nums)
        l, r = 0, n

        while l < r:
            m = (l + r) // 2
            if nums[m] < 0:
                l = m + 1
            else:
                r = m
        
        return l
        
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        print(self.upperBound(nums), self.lowerBound(nums))
        positive = n - self.upperBound(nums)
        negative = self.lowerBound(nums)
        
        return max(positive, negative)
```
