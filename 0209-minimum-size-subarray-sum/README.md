<h2><a href="https://leetcode.com/problems/minimum-size-subarray-sum">209. Minimum Size Subarray Sum</a></h2><h3>Medium</h3><hr><p>Given an array of positive integers <code>nums</code> and a positive integer <code>target</code>, return <em>the <strong>minimal length</strong> of a </em><span data-keyword="subarray-nonempty"><em>subarray</em></span><em> whose sum is greater than or equal to</em> <code>target</code>. If there is no such subarray, return <code>0</code> instead.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> target = 7, nums = [2,3,1,2,4,3]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The subarray [4,3] has the minimal length under the problem constraint.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> target = 4, nums = [1,4,4]
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> target = 11, nums = [1,1,1,1,1,1,1,1]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= target &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> If you have figured out the <code>O(n)</code> solution, try coding another solution of which the time complexity is <code>O(n log(n))</code>.

# Approach
* Define left of window as 0 (leftmost window border), sum to check with target and min (minimal window size);
* In a loop through nums add each element to sum accumulator;
* Then in while loop by condition sum >= target update min window length, substract nums[left] from sum and shfit left by 1 forward (window narrowing from left border);

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        minLen = len(nums)
        totalSum = 0

        if sum(nums) < target:
            return 0

        for i in range(len(nums)):
            totalSum += nums[i]

            while totalSum >= target:
                totalSum -= nums[left]
                minLen = min(minLen, i+1-left)
                left += 1
                
        return minLen
```
---
```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        minLen = float('inf')
        totalSum = 0

        for i in range(len(nums)):
            totalSum += nums[i]

            while totalSum >= target:
                totalSum -= nums[left]
                minLen = min(minLen, i+1-left)
                left += 1
                
        return 0 if minLen == float('inf') else minLen
```
---
```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        curr = 0
        best = float('inf')

        for right, x in enumerate(nums):
            curr += x

            while curr >= target:
                best = min(best, right - left + 1)
                curr -= nums[left]
                left += 1
                
        return 0 if best == float('inf') else best
```
