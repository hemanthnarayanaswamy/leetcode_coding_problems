<h2><a href="https://leetcode.com/problems/maximum-erasure-value">1813. Maximum Erasure Value</a></h2><h3>Medium</h3><hr><p>You are given an array of positive integers <code>nums</code> and want to erase a subarray containing&nbsp;<strong>unique elements</strong>. The <strong>score</strong> you get by erasing the subarray is equal to the <strong>sum</strong> of its elements.</p>

<p>Return <em>the <strong>maximum score</strong> you can get by erasing <strong>exactly one</strong> subarray.</em></p>

<p>An array <code>b</code> is called to be a <span class="tex-font-style-it">subarray</span> of <code>a</code> if it forms a contiguous subsequence of <code>a</code>, that is, if it is equal to <code>a[l],a[l+1],...,a[r]</code> for some <code>(l,r)</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,2,4,5,6]
<strong>Output:</strong> 17
<strong>Explanation:</strong> The optimal subarray here is [2,4,5,6].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,2,1,2,5,2,1,2,5]
<strong>Output:</strong> 8
<strong>Explanation:</strong> The optimal subarray here is [5,2,1] or [1,2,5].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>

<img width="726" height="789" alt="image" src="https://github.com/user-attachments/assets/13221d9c-08ab-4b50-ad61-b7c01c618709" />

# Solution 
```ini 
Say, nums = [4,2,4,5,6]

Start with left = 0, right = 0, window is [4]

seen = {4}, currentSum = 4

right = 1, window becomes [4,2]

No duplicate → update sum → currentSum = 6, seen = {2,4}

right = 2, element is 4 (duplicate!)

Slide left to remove the first 4 → window becomes [2,4]

Continue expanding → [2,4,5], then [2,4,5,6]

This is the best subarray with sum = 17

The sliding window automatically adjusts, ensuring:

Only unique values stay in the window

Sum is updated dynamically
```
---

```python
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        maxSum = 0
        left = 0
        currentSum = 0
        seen = set()

        for right in range(len(nums)):
            num = nums[right]
            while num in seen:
                numx = nums[left]
                seen.remove(numx)
                currentSum -= numx
                left += 1
            
            currentSum += num
            seen.add(num)
            maxSum = max(maxSum, currentSum)
        
        return maxSum
```
