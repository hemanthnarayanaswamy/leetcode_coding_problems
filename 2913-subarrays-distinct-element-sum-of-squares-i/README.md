<h2><a href="https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i">3163. Subarrays Distinct Element Sum of Squares I</a></h2><h3>Easy</h3><hr><p>You are given a <strong>0-indexed </strong>integer array <code>nums</code>.</p>

<p>The <strong>distinct count</strong> of a subarray of <code>nums</code> is defined as:</p>

<ul>
	<li>Let <code>nums[i..j]</code> be a subarray of <code>nums</code> consisting of all the indices from <code>i</code> to <code>j</code> such that <code>0 &lt;= i &lt;= j &lt; nums.length</code>. Then the number of distinct values in <code>nums[i..j]</code> is called the distinct count of <code>nums[i..j]</code>.</li>
</ul>

<p>Return <em>the sum of the <strong>squares</strong> of <strong>distinct counts</strong> of all subarrays of </em><code>nums</code>.</p>

<p>A subarray is a contiguous <strong>non-empty</strong> sequence of elements within an array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,1]
<strong>Output:</strong> 15
<strong>Explanation:</strong> Six possible subarrays are:
[1]: 1 distinct value
[2]: 1 distinct value
[1]: 1 distinct value
[1,2]: 2 distinct values
[2,1]: 2 distinct values
[1,2,1]: 2 distinct values
The sum of the squares of the distinct counts in all subarrays is equal to 1<sup>2</sup> + 1<sup>2</sup> + 1<sup>2</sup> + 2<sup>2</sup> + 2<sup>2</sup> + 2<sup>2</sup> = 15.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1]
<strong>Output:</strong> 3
<strong>Explanation:</strong> Three possible subarrays are:
[1]: 1 distinct value
[1]: 1 distinct value
[1,1]: 1 distinct value
The sum of the squares of the distinct counts in all subarrays is equal to 1<sup>2</sup> + 1<sup>2</sup> + 1<sup>2</sup> = 3.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>

# Solution
```python
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        for i in range(n):
            distinct = set()
            for j in range(i, n):
                distinct.add(nums[j])
                count += len(distinct)**2
        
        return count
```
---
```python
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        for i in range(n):
            distinct = set()
            l = 0  # To track lenght instead of re calculating everytime
            for j in range(i, n):
                if nums[j] not in distinct:
                    distinct.add(nums[j])
                    l += 1
                count += l*l
        
        return count
```
---
```python
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        count = 0

        for i in range(len(nums)):
            distinct = set()
            l = 0  # To track lenght instead of re calculating everytime
            for c in nums[i:]:
                if c not in distinct:
                    distinct.add(c)
                    l += 1
                count += l*l
        
        return count
```
