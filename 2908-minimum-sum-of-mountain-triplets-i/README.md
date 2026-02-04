<h2><a href="https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i">3176. Minimum Sum of Mountain Triplets I</a></h2><h3>Easy</h3><hr><p>You are given a <strong>0-indexed</strong> array <code>nums</code> of integers.</p>

<p>A triplet of indices <code>(i, j, k)</code> is a <strong>mountain</strong> if:</p>

<ul>
	<li><code>i &lt; j &lt; k</code></li>
	<li><code>nums[i] &lt; nums[j]</code> and <code>nums[k] &lt; nums[j]</code></li>
</ul>

<p>Return <em>the <strong>minimum possible sum</strong> of a mountain triplet of</em> <code>nums</code>. <em>If no such triplet exists, return</em> <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [8,6,1,5,3]
<strong>Output:</strong> 9
<strong>Explanation:</strong> Triplet (2, 3, 4) is a mountain triplet of sum 9 since: 
- 2 &lt; 3 &lt; 4
- nums[2] &lt; nums[3] and nums[4] &lt; nums[3]
And the sum of this triplet is nums[2] + nums[3] + nums[4] = 9. It can be shown that there are no mountain triplets with a sum of less than 9.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,4,8,7,10,2]
<strong>Output:</strong> 13
<strong>Explanation:</strong> Triplet (1, 3, 5) is a mountain triplet of sum 13 since: 
- 1 &lt; 3 &lt; 5
- nums[1] &lt; nums[3] and nums[5] &lt; nums[3]
And the sum of this triplet is nums[1] + nums[3] + nums[5] = 13. It can be shown that there are no mountain triplets with a sum of less than 13.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [6,5,4,3,4,5]
<strong>Output:</strong> -1
<strong>Explanation:</strong> It can be shown that there are no mountain triplets in nums.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 50</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 50</code></li>
</ul>

# Brute Force 
```python
class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        res = float('inf')
        n = len(nums)

        for i in range(n-2):
            for j in range(i+1, n-1):
                a, b = nums[i], nums[j]
                if a >= b:
                    break
                for k in range(j+1, n):
                    c = nums[k]
                    if c >= b or (a+b+c) >= res:
                        continue
                    res = a+b+c
        
        return -1 if res == float('inf') else res
```
---
# Optimal Solution
1. we'll use the prefix technique to precompute the minmum at the each index on the left side and precompute the minimum for each index on the right side. 
2. Then we'll do a final iteration, where we check the current condition.

```python
class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)

        left_min = [0] * n
        left_min[0] = nums[0]

        for i in range(1, n):
            left_min[i] = min(nums[i], left_min[i-1])
        
        right_min = [0] * n
        right_min[n-1] = nums[n-1]

        for i in range(n-2, -1, -1):
            right_min[i] = min(nums[i], right_min[i+1])
        
        res = float('inf')

        for i in range(1, n-1):
            left = left_min[i-1]
            right = right_min[i+1]
            current = nums[i]

            if current > left and current > right:
                res = min(res, left + current + right)
                
        return -1 if res == float('inf') else res
```
