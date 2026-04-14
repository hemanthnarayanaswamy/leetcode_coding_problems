<h2><a href="https://leetcode.com/problems/max-consecutive-ones-iii">1046. Max Consecutive Ones III</a></h2><h3>Medium</h3><hr><p>Given a binary array <code>nums</code> and an integer <code>k</code>, return <em>the maximum number of consecutive </em><code>1</code><em>&#39;s in the array if you can flip at most</em> <code>k</code> <code>0</code>&#39;s.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
<strong>Output:</strong> 6
<strong>Explanation:</strong> [1,1,1,0,0,<u><strong>1</strong>,1,1,1,1,<strong>1</strong></u>]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
<strong>Output:</strong> 10
<strong>Explanation:</strong> [0,0,<u>1,1,<strong>1</strong>,<strong>1</strong>,1,1,1,<strong>1</strong>,1,1</u>,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>nums[i]</code> is either <code>0</code> or <code>1</code>.</li>
	<li><code>0 &lt;= k &lt;= nums.length</code></li>
</ul>

# Approach
* We don't have a fixed size window in this case. The window size can grow and shrink depending upon the number of zeros we have (we don't actually have to flip the zeros here!).

```python
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int: 
        numsFreq = Counter(nums)
        maxCount = count = 0
        freq = defaultdict(int)
        left = 0

        for right in range(len(nums)):
            freq[nums[right]] += 1

            while freq[0] > k:
                freq[nums[left]] -= 1
                left += 1
            
            count = freq[1]
            if count > maxCount:
                maxCount = count
        
        if k > numsFreq[0]:
            total = maxCount + numsFreq[0]
        else:
            total = maxCount + k

        return total
```
* We don't need other counter to compute the `total`
* Do a running `maxCount` by having the condition `if freq[0] <= k:`

```python
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int: 
        maxCount = 0
        freq = defaultdict(int)
        left = 0

        for right in range(len(nums)):
            freq[nums[right]] += 1

            while freq[0] > k:
                freq[nums[left]] -= 1
                left += 1
            
            if freq[0] <= k:
                maxCount = max(maxCount, freq[0]+freq[1])
       
        return maxCount
```
* We don't need the condition `if freq[0] <= k:` because it'll be always true as we are running `while loop` to maintain that.
* Since we have only `1 & 0` no need to use counter using `Array`

```python
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int: 
        maxCount = 0
        freq = [0, 0]
        left = 0

        for right in range(len(nums)):
            freq[nums[right]] += 1

            while freq[0] > k:
                freq[nums[left]] -= 1
                left += 1
            
            if sum(freq) > maxCount:
                maxCount = sum(freq)
       
        return maxCount
```
---
# OPtimal Solution

```python
class Solution:
    def longestOnes(self, nums, k):
        left, maxLength, zeroCount = 0, 0, 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeroCount += 1

            while zeroCount > k:
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1
            else:
                maxLength = max(maxLength, right - left + 1)

        return maxLength
```
---
```python
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
        
        return len(nums) - left
```
