<h2><a href="https://leetcode.com/problems/find-triangular-sum-of-an-array">2324. Find Triangular Sum of an Array</a></h2><h3>Medium</h3><hr><p>You are given a <strong>0-indexed</strong> integer array <code>nums</code>, where <code>nums[i]</code> is a digit between <code>0</code> and <code>9</code> (<strong>inclusive</strong>).</p>

<p>The <strong>triangular sum</strong> of <code>nums</code> is the value of the only element present in <code>nums</code> after the following process terminates:</p>

<ol>
	<li>Let <code>nums</code> comprise of <code>n</code> elements. If <code>n == 1</code>, <strong>end</strong> the process. Otherwise, <strong>create</strong> a new <strong>0-indexed</strong> integer array <code>newNums</code> of length <code>n - 1</code>.</li>
	<li>For each index <code>i</code>, where <code>0 &lt;= i &lt;&nbsp;n - 1</code>, <strong>assign</strong> the value of <code>newNums[i]</code> as <code>(nums[i] + nums[i+1]) % 10</code>, where <code>%</code> denotes modulo operator.</li>
	<li><strong>Replace</strong> the array <code>nums</code> with <code>newNums</code>.</li>
	<li><strong>Repeat</strong> the entire process starting from step 1.</li>
</ol>

<p>Return <em>the triangular sum of</em> <code>nums</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/02/22/ex1drawio.png" style="width: 250px; height: 250px;" />
<pre>
<strong>Input:</strong> nums = [1,2,3,4,5]
<strong>Output:</strong> 8
<strong>Explanation:</strong>
The above diagram depicts the process from which we obtain the triangular sum of the array.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [5]
<strong>Output:</strong> 5
<strong>Explanation:</strong>
Since there is only one element in nums, the triangular sum is the value of that element itself.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 9</code></li>
</ul>

# Solution 
```python
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            nums = [(a + b) % 10 for a, b in zip(nums, nums[1:])]
        return nums[0]
```

# Optimal Solution 
* Each number in the array contributes to the final sum a certain number of times. We can visualize how to figure out factors for each number using Pascal's triangle:

```ini 
For test case [1, 2, 3, 4, 5], we will get 1 * 1 + 2 * 4 + 3 * 6 + 4 * 4 + 5 * 1 = 1 + 8 + 18 + 16 + 5 = 48, or 8 after modulo 10.

The bottom row of Pascal's triangle are binomial coefficients, which can be computed as nCr(n - 1, i)
```

```python
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        res, nCr, n = 0, 1, len(nums) - 1
        for r, num in enumerate(nums):
            res = (res + num  * nCr) % 10
            nCr = nCr * (n - r) // (r + 1)
        return res
```
