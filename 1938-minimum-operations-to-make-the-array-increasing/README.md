<h2><a href="https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing">1938. Minimum Operations to Make the Array Increasing</a></h2><h3>Easy</h3><hr><p>You are given an integer array <code>nums</code> (<strong>0-indexed</strong>). In one operation, you can choose an element of the array and increment it by <code>1</code>.</p>

<ul>
	<li>For example, if <code>nums = [1,2,3]</code>, you can choose to increment <code>nums[1]</code> to make <code>nums = [1,<u><b>3</b></u>,3]</code>.</li>
</ul>

<p>Return <em>the <strong>minimum</strong> number of operations needed to make</em> <code>nums</code> <em><strong>strictly</strong> <strong>increasing</strong>.</em></p>

<p>An array <code>nums</code> is <strong>strictly increasing</strong> if <code>nums[i] &lt; nums[i+1]</code> for all <code>0 &lt;= i &lt; nums.length - 1</code>. An array of length <code>1</code> is trivially strictly increasing.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,1]
<strong>Output:</strong> 3
<strong>Explanation:</strong> You can do the following operations:
1) Increment nums[2], so nums becomes [1,1,<u><strong>2</strong></u>].
2) Increment nums[1], so nums becomes [1,<u><strong>2</strong></u>,2].
3) Increment nums[2], so nums becomes [1,2,<u><strong>3</strong></u>].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,5,2,4,1]
<strong>Output:</strong> 14
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [8]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 5000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>

# Solution 
* The solution works but the logic can be even more refactored Instread of performing the logic only perform logic for `num[i] < num[i-1]`
```
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        n = len(nums)

        if n <= 1:
            return 0

        for i in range(1,n):
            current, previous = nums[i], nums[i-1]
            diff = previous - current 

            if diff >= 0:
                nums[i] += diff+1
                operations += diff+1
        
        return operations
```

# Refactored Code 
```python
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0

        for i in range(1,len(nums)):
            current, previous = nums[i], nums[i-1]

            if current <= previous:
                increment = nums[i - 1] - nums[i] + 1
                nums[i] += increment
                operations += increment 
        
        return operations
```
# Improved Further Code 
```python
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0

        for i in range(1,len(nums)):
            current, previous = nums[i], nums[i-1]

            if current <= previous:
                nums[i] = previous + 1
                operations += previous - current + 1
        
        return operations
```
