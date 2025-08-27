<h2><a href="https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum">1514. Minimum Value to Get Positive Step by Step Sum</a></h2><h3>Easy</h3><hr><p>Given an array of integers&nbsp;<code>nums</code>, you start with an initial <strong>positive</strong> value <em>startValue</em><em>.</em></p>

<p>In each iteration, you calculate the step by step sum of <em>startValue</em>&nbsp;plus&nbsp;elements in <code>nums</code>&nbsp;(from left to right).</p>

<p>Return the minimum <strong>positive</strong> value of&nbsp;<em>startValue</em> such that the step by step sum is never less than 1.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [-3,2,-3,4,2]
<strong>Output:</strong> 5
<strong>Explanation: </strong>If you choose startValue = 4, in the third iteration your step by step sum is less than 1.
<strong>step by step sum</strong>
<strong>startValue = 4 | startValue = 5 | nums</strong>
  (4 <strong>-3</strong> ) = 1  | (5 <strong>-3</strong> ) = 2    |  -3
  (1 <strong>+2</strong> ) = 3  | (2 <strong>+2</strong> ) = 4    |   2
  (3 <strong>-3</strong> ) = 0  | (4 <strong>-3</strong> ) = 1    |  -3
  (0 <strong>+4</strong> ) = 4  | (1 <strong>+4</strong> ) = 5    |   4
  (4 <strong>+2</strong> ) = 6  | (5 <strong>+2</strong> ) = 7    |   2
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2]
<strong>Output:</strong> 1
<strong>Explanation:</strong> Minimum start value should be positive. 
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,-2,-3]
<strong>Output:</strong> 5
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
</ul>

# Solution 
* the stepsum they're calculating is actually prefix sum
* now at any point of time, prefix sum should be above 1, so we find min prefix sum and add a value x to it so it becomes >= 1, that x is our answer
hope this helps.

```ini
- So compute the prefix sum for that array and find the minimum prefix sum in that
- Then compute the diff between that and 1 
- That way when we start with that number the prefix will always be positive.
```
```python
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefixSum = [nums[0]]

        for i in range(1, len(nums)):
            prefixSum.append(prefixSum[-1] + nums[i])
        
        minPrefix = min(prefixSum)

        if minPrefix < 0:
            return 1 + abs(minPrefix)
        else:
            return 1
```

```python
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefixSum = [nums[0]]
    
        for i in range(1, len(nums)):
            prefixSum.append(prefixSum[-1] + nums[i])
        
        minPrefix = min(prefixSum)
        
        return max(1, 1 - minPrefix)
```            
---
```python
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_sum = 0
        current_sum = 0
        
        for num in nums:
            current_sum += num
            min_sum = min(min_sum, current_sum)
        
        return 1 - min_sum if min_sum < 0 else 1
```

```ini
🧠 Key Insights
1. Step-by-Step Sum Tracking
- Need to track cumulative sum at each position
- The sum after adding each element must be ≥ 1
- Not just the final sum - every intermediate step matters

2. Critical Observation
- The "worst case" occurs at the lowest cumulative sum
- If we can handle the worst case, all other cases are automatically satisfied
- Find where the cumulative sum reaches its minimum value

3. Mathematical Relationship
** startValue + minimumCumulativeSum ≥ 1 **

- If minimum cumulative sum is negative, we need extra start value ( minPrefix + x = 1) compute x
- If minimum cumulative sum is positive, start value = 1 is sufficient
```
