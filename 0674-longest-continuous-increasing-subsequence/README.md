<h2><a href="https://leetcode.com/problems/longest-continuous-increasing-subsequence">674. Longest Continuous Increasing Subsequence</a></h2><h3>Easy</h3><hr><p>Given an unsorted array of integers <code>nums</code>, return <em>the length of the longest <strong>continuous increasing subsequence</strong> (i.e. subarray)</em>. The subsequence must be <strong>strictly</strong> increasing.</p>

<p>A <strong>continuous increasing subsequence</strong> is defined by two indices <code>l</code> and <code>r</code> (<code>l &lt; r</code>) such that it is <code>[nums[l], nums[l + 1], ..., nums[r - 1], nums[r]]</code> and for each <code>l &lt;= i &lt; r</code>, <code>nums[i] &lt; nums[i + 1]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,5,4,7]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The longest continuous increasing subsequence is [1,3,5] with length 3.
Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element
4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,2,2,2,2]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The longest continuous increasing subsequence is [2] with length 1. Note that it must be strictly
increasing.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

# Solution
* We need to track two Length `max Len` and `current Len`. 
* When ever the condition `nums[i] < nums[i+1]`, fail, we find the `maxLen` and reset the `current Length`. 

```python
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        maxLen = 1
        currLen = 1

        for i in range(len(nums) - 1):
            if nums[i] < nums[i+1]:
                currLen += 1
            else:
                maxLen = max(maxLen, currLen)
                currLen = 1
                
        maxLen = max(maxLen, currLen)
        
        return maxLen
```
---
# Optimal Solution 
* Use `Prefix Sum` method to track the longest subsequence Length at each index.
```python
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                prefix[i] = prefix[i - 1] + 1
        
        return max(prefix)
```
