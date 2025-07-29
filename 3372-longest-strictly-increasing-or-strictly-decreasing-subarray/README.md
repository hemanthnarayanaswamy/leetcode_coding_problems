<h2><a href="https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray">3372. Longest Strictly Increasing or Strictly Decreasing Subarray</a></h2><h3>Easy</h3><hr><p>You are given an array of integers <code>nums</code>. Return <em>the length of the <strong>longest</strong> <span data-keyword="subarray-nonempty">subarray</span> of </em><code>nums</code><em> which is either <strong><span data-keyword="strictly-increasing-array">strictly increasing</span></strong> or <strong><span data-keyword="strictly-decreasing-array">strictly decreasing</span></strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,4,3,3,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>The strictly increasing subarrays of <code>nums</code> are <code>[1]</code>, <code>[2]</code>, <code>[3]</code>, <code>[3]</code>, <code>[4]</code>, and <code>[1,4]</code>.</p>

<p>The strictly decreasing subarrays of <code>nums</code> are <code>[1]</code>, <code>[2]</code>, <code>[3]</code>, <code>[3]</code>, <code>[4]</code>, <code>[3,2]</code>, and <code>[4,3]</code>.</p>

<p>Hence, we return <code>2</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,3,3,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>The strictly increasing subarrays of <code>nums</code> are <code>[3]</code>, <code>[3]</code>, <code>[3]</code>, and <code>[3]</code>.</p>

<p>The strictly decreasing subarrays of <code>nums</code> are <code>[3]</code>, <code>[3]</code>, <code>[3]</code>, and <code>[3]</code>.</p>

<p>Hence, we return <code>1</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,2,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>The strictly increasing subarrays of <code>nums</code> are <code>[3]</code>, <code>[2]</code>, and <code>[1]</code>.</p>

<p>The strictly decreasing subarrays of <code>nums</code> are <code>[3]</code>, <code>[2]</code>, <code>[1]</code>, <code>[3,2]</code>, <code>[2,1]</code>, and <code>[3,2,1]</code>.</p>

<p>Hence, we return <code>3</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 50</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 50</code></li>
</ul>

# Solution
* When elements are in decreasing order (nums[i-1] > nums[i]), the code increments res_inc but resets res_dec. 
* Similarly, when elements are in increasing order (nums[i-1] < nums[i]), the code increments res_dec but resets res_inc. 
* For each iteration it gathers the maximum result values.
```python
def longestMonotonicSubarray(self, nums: List[int]) -> int:
    if not nums:
        return 0
        
    res, res_inc, res_dec = 1, 1, 1

    for i in range(1, len(nums)):
        if nums[i-1] > nums[i]:  # Decreasing sequence
            res_dec += 1
            res_inc = 1
        elif nums[i-1] < nums[i]:  # Increasing sequence
            res_inc += 1
            res_dec = 1
        else:  # Equal elements
            # For a strictly monotonic definition, reset both
            # For non-strict monotonic, you would increment both
            res_dec = 1
            res_inc = 1
        
        res = max(res, res_dec, res_inc)
    
    return res
```

# Optimal Solution
```python
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        result, currinc, currdec, prev = 0, 0, 0, nums[0]
        for num in nums:
            if num > prev:
                currinc += 1
            else:
                currinc = 1
            
            if num < prev:
                currdec += 1
            else:
                currdec = 1
            
            result = max(result, currinc, currdec)
            prev = num
        return result
```
