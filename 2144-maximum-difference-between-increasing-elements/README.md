<h2><a href="https://leetcode.com/problems/maximum-difference-between-increasing-elements">2144. Maximum Difference Between Increasing Elements</a></h2><h3>Easy</h3><hr><p>Given a <strong>0-indexed</strong> integer array <code>nums</code> of size <code>n</code>, find the <strong>maximum difference</strong> between <code>nums[i]</code> and <code>nums[j]</code> (i.e., <code>nums[j] - nums[i]</code>), such that <code>0 &lt;= i &lt; j &lt; n</code> and <code>nums[i] &lt; nums[j]</code>.</p>

<p>Return <em>the <strong>maximum difference</strong>. </em>If no such <code>i</code> and <code>j</code> exists, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [7,<strong><u>1</u></strong>,<strong><u>5</u></strong>,4]
<strong>Output:</strong> 4
<strong>Explanation:</strong>
The maximum difference occurs with i = 1 and j = 2, nums[j] - nums[i] = 5 - 1 = 4.
Note that with i = 1 and j = 0, the difference nums[j] - nums[i] = 7 - 1 = 6, but i &gt; j, so it is not valid.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [9,4,3,2]
<strong>Output:</strong> -1
<strong>Explanation:</strong>
There is no i and j such that i &lt; j and nums[i] &lt; nums[j].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [<strong><u>1</u></strong>,5,2,<strong><u>10</u></strong>]
<strong>Output:</strong> 9
<strong>Explanation:</strong>
The maximum difference occurs with i = 0 and j = 3, nums[j] - nums[i] = 10 - 1 = 9.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>2 &lt;= n &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

# Solution
```python
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxDiff = -1
        n = len(nums)

        l , r = 0, 1 

        while r < n:
            if nums[r] > nums[l]:
                d = nums[r] - nums[l]
                if d > maxDiff:
                    maxDiff = d
            else:
                l = r
            
            r += 1
        
        return maxDiff
```

"""
	•	Goal: Find the maximum nums[j] - nums[i] with j > i, or return -1 if no positive difference exists.
	•	Two‐pointer setup:
	•	l tracks the index of the smallest candidate “buy” price seen so far.
	•	r scans ahead as the “sell” pointer.
	•	Loop invariant: At each step, l < r and nums[l] is the minimum of nums[0…r-1].
	•	Core logic:
	1.	If nums[r] > nums[l], compute diff = nums[r] - nums[l] and update maxDiff if larger.
	2.	Else (nums[r] ≤ nums[l]), move l = r to start a new “buy” at index r.
	3.	Always increment r until end.
	•	Result: maxDiff holds the best positive difference or stays -1.
	•	Complexity:
	•	Time: O(n) single pass
	•	Space: O(1) extra variables
	•	Why it works:
	•	By always keeping l at the smallest seen so far, any time you find a higher nums[r], you automatically get the best possible profit from that buy.
	•	Resetting l when you see a new low ensures you never miss a better starting point.
"""

# Optimal Solution
```python
from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        # best difference found so far (or -1 if none)
        max_diff = -1
        # smallest value seen up to the current point
        min_val   = nums[0]

        # scan the rest of the array
        for x in nums[1:]:
            if x > min_val:
               
                diff = x - min_val
                if diff > max_diff:
                    max_diff = diff
            else:
                
                min_val = x

        return max_diff
```
