<h2><a href="https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element">1586. Longest Subarray of 1's After Deleting One Element</a></h2><h3>Medium</h3><hr><p>Given a binary array <code>nums</code>, you should delete one element from it.</p>

<p>Return <em>the size of the longest non-empty subarray containing only </em><code>1</code><em>&#39;s in the resulting array</em>. Return <code>0</code> if there is no such subarray.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,0,1]
<strong>Output:</strong> 3
<strong>Explanation:</strong> After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1&#39;s.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,1,1,1,0,1,1,0,1]
<strong>Output:</strong> 5
<strong>Explanation:</strong> After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1&#39;s is [1,1,1,1,1].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> You must delete one element.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>nums[i]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>

# Solution 
* We need to compute the total number of ones of the left and right side for each zeros. 
* Next find the longest subsequence for each zero position by computing the sum of left and right zeros. 
* Handle all zeros and all ones edge cases.

```python
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        leftOnes = [0] * len(nums)
        rightOnes = [0] * len(nums)

        numsFreq = Counter(nums)

        count1 = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count1 += 1
            else:
                leftOnes[i] = count1
                count1 = 0
        
        count1 = 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 1:
                count1 += 1
            else:
                rightOnes[i] = count1
                count1 = 0
        
        longestLen = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                tmp = leftOnes[i] + rightOnes[i]
                if tmp > longestLen:
                    longestLen = tmp
        
        if numsFreq.get(0, 0) == 0:
            return len(nums) - 1
        elif numsFreq.get(1, 0) == 0:
            return 0
        else:
            return longestLen
```
---
# Improved Solution 
```python
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res = [0] * n
        numsSum = sum(nums)

        if numsSum == n:
            return n-1
        elif numsSum == 0:
            return 0

        count1 = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count1 += 1
            else:
                res[i] += count1
                count1 = 0
        
        count1 = 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 1:
                count1 += 1
            else:
                res[i] += count1
                count1 = 0
        
        return max(res)
```

# Sliding Window Technique 
```python
def longestSubarray(nums):
    left = 0
    zeros = 0
    maxLen = 0
    
    for right in range(len(nums)):
        # Expand window
        if nums[right] == 0:
            zeros += 1
        
        # Contract window if we have more than 1 zero
        while zeros > 1:
            if nums[left] == 0:
                zeros -= 1
            left += 1
        
        # Update max length (subtract 1 because we must delete exactly one element)
        maxLen = max(maxLen, right - left + 1 - 1)
    
    return maxLen
```
